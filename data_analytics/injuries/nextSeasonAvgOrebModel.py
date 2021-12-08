from pyspark.sql import SparkSession, functions, types
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, SQLTransformer
from pyspark.ml.regression import GBTRegressor, RandomForestRegressor, LinearRegression, DecisionTreeRegressor
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import RegressionEvaluator

from plot_tools import plot_validation_result, plot_corr, plot_scatter, plot_residual, plot_featureImportance

import re
import sys
assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+


def main():
    # load injury dataset
    player_schema = types.StructType([
        types.StructField('PLAYER_NAME', types.StringType()),
        types.StructField('year', types.IntegerType()),
        types.StructField('totalPts', types.FloatType()),
        types.StructField('totalPf', types.FloatType()),
        types.StructField('totalTo', types.FloatType()),
        types.StructField('totalBlk', types.FloatType()),
        types.StructField('totalStl', types.FloatType()),
        types.StructField('totalAst', types.FloatType()),
        types.StructField('totalReb', types.FloatType()),
        types.StructField('totalDreb', types.FloatType()),
        types.StructField('totalOreb', types.FloatType()),
        types.StructField('totalFta', types.FloatType()),
        types.StructField('totalFtm', types.FloatType()),
        types.StructField('totalFg3a', types.FloatType()),
        types.StructField('totalFg3m', types.FloatType()),
        types.StructField('totalFga', types.FloatType()),
        types.StructField('totalFgm', types.FloatType()),
        types.StructField('totalGames', types.FloatType()),
        types.StructField('totalEfficiency', types.FloatType()),
        types.StructField('injury_name', types.StringType()),
        types.StructField('status', types.StringType()),
        types.StructField('count', types.FloatType()),
        types.StructField('player_position', types.StringType()),
        types.StructField('team_abbreviation', types.StringType()),
        types.StructField('age', types.FloatType()),
        types.StructField('player_height', types.FloatType()),
        types.StructField('player_weight', types.FloatType())
    ])

    player = (spark.read
              .option("delimiter", ",")
              .option("header", "true")
              .schema(player_schema)
              .csv(player_inputs)
              .where(~functions.col("totalFga").isNull())
              .where(~functions.col("totalFgm").isNull())
              .repartition(8))

    train, validation = player.randomSplit([0.6, 0.4])
    print(train.count())
    print(validation.count())
    train = train.cache()
    validation = validation.cache()
    position_indexer = StringIndexer(
        inputCol="player_position", outputCol="player_position_index", stringOrderType="frequencyDesc",
        handleInvalid="skip")
    status_indexer = StringIndexer(
        inputCol="status", outputCol="status_index", stringOrderType="frequencyDesc",
        handleInvalid="skip")
    
    # position_encoder = OneHotEncoder(inputCol="player_position_index", outputCol="player_position_encoder")
    # status_encoder = OneHotEncoder(inputCol="status_index", outputCol="status_encoder")
    
    # predict next avg assistance
    vectorAssembler = VectorAssembler(inputCols=["player_position_index", "status_index", "count",
                                                "avgOreb", "nextSeasonAge", "nextSeasonHeight", "nextSeasonWeight"],
                                      outputCol="features")
    r2_evaluator = RegressionEvaluator(
        predictionCol="prediction", labelCol="nextSeasonAvgOreb", metricName="r2")
    sqlStatement = (
        """
    SELECT t0.age, t0.status, t0.count, t0.player_height AS height, t0.player_weight AS weight,
    (t0.totalOreb / t0.totalGames) AS avgOreb, t1.player_position, t1.age AS nextSeasonAge,
    t1.player_height AS nextSeasonHeight, t1.player_weight AS nextSeasonWeight,
    (t1.totalOreb / t1.totalGames) AS nextSeasonAvgOreb
    FROM __THIS__ as t0
    INNER JOIN __THIS__ as t1
    ON t0.year + 1 = t1.year
    AND t0.PLAYER_NAME = t1.PLAYER_NAME
    """)
    
    # tree regressor
    # gbtr = GBTRegressor(featuresCol="features", labelCol="nextSeasonAvgDreb", maxIter=8,
    #                     maxDepth=5, stepSize=0.1, seed=42, featureSubsetStrategy='all')
    # grid = (ParamGridBuilder()
    #         .baseOn({gbtr.labelCol: 'nextSeasonAvgDreb'}) 
    #         .baseOn([gbtr.featuresCol, "features"])
    #         .baseOn([gbtr.predictionCol, 'prediction']) 
    #         .build())
    rfr = RandomForestRegressor(featuresCol="features", labelCol="nextSeasonAvgOreb",
                        numTrees=5, maxDepth=5, seed=42)
    grid = (ParamGridBuilder()
            .baseOn({rfr.labelCol: 'nextSeasonAvgOreb'}) 
            .baseOn([rfr.featuresCol, "features"])
            .baseOn([rfr.predictionCol, 'prediction']) 
            .build())
    cv = CrossValidator(estimator=rfr, estimatorParamMaps=grid, evaluator=r2_evaluator, numFolds=10)
    pipelineCV = Pipeline(stages=[SQLTransformer(statement=sqlStatement), position_indexer, status_indexer,
                                    vectorAssembler, cv])
    rfrModelCV = pipelineCV.fit(train)
    trainDF = rfrModelCV.transform(train)
    r2_train = r2_evaluator.evaluate(trainDF)
    print(f"r2 training for predicting nextSeasonAvgOreb is {r2_train}")
    predDF = rfrModelCV.transform(validation)
    r2 = r2_evaluator.evaluate(predDF)
    print(f"r2 validation for predicting nextSeasonAvgOreb is {r2}")
    treeCV = rfrModelCV.stages[-1].bestModel
    # trainDF.groupBy("player_position", "player_position_index").agg(functions.count("*")).show()
    # print(predDF.count())
    # print(treeCV.featureImportances.toArray())
    plot_featureImportance(["player_position_index", "status_index", "count", "avgOreb", "nextSeasonAge",
                            "nextSeasonHeight", "nextSeasonWeight"],
                           treeCV.featureImportances.toArray())
    plot_validation_result(predDF.select("prediction").collect(), predDF.select("nextSeasonAvgOreb").collect())
    
    player = (player
              .withColumn("avgOreb", functions.col("totalOreb")/functions.col("totalGames")))
    player.cache()
    plot_scatter(player.select("count").collect(), player.select("avgOreb").collect(), "number of injuries",
                           "average offensive rebound")
    plot_scatter(player.select("age").collect(), player.select("avgOreb").collect(), "age",
                           "average offensive rebound")
    plot_scatter(player.select("player_height").collect(), player.select("avgOreb").collect(), "height",
                           "average offensive rebound")
    plot_scatter(player.select("player_weight").collect(), player.select("avgOreb").collect(), "weight",
                           "average offensive rebound")
    



if __name__ == '__main__':
    player_inputs = sys.argv[1]
    outputs = sys.argv[2]
    spark = SparkSession.builder.appName('example code').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main()
