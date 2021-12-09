from pyspark.sql import SparkSession, functions, types
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, SQLTransformer
from pyspark.ml.regression import GBTRegressor, RandomForestRegressor, LinearRegression, DecisionTreeRegressor
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import RegressionEvaluator

from plot_tools import plot_validation_result, plot_corr, plot_scatter, plot_residual

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
    player.cache()
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
    
    position_encoder = OneHotEncoder(inputCol="player_position_index", outputCol="player_position_encoder")
    status_encoder = OneHotEncoder(inputCol="status_index", outputCol="status_encoder")
    
    # predict next avg assistance
    # lr
    vectorAssembler = VectorAssembler(inputCols=["player_position_encoder", "status_encoder", "count",
                                                "avgBlk", "nextSeasonAge", "nextSeasonHeight", "nextSeasonWeight"],
                                      outputCol="features")
    r2_evaluator = RegressionEvaluator(
        predictionCol="prediction", labelCol="nextSeasonAvgBlk", metricName="r2")
    sqlStatement = (
        """
    SELECT t0.age, t0.status, LOG(t0.count) AS count, t0.player_height AS height, t0.player_weight AS weight,
    (t0.totalBlk / t0.totalGames) AS avgBlk, t1.player_position, t1.age AS nextSeasonAge,
    t1.player_height AS nextSeasonHeight, t1.player_weight AS nextSeasonWeight,
    (t1.totalBlk / t1.totalGames) AS nextSeasonAvgBlk
    FROM __THIS__ as t0
    INNER JOIN __THIS__ as t1
    ON t0.year + 1 = t1.year
    AND t0.PLAYER_NAME = t1.PLAYER_NAME
    """)
    
    lr = LinearRegression(featuresCol="features", labelCol="nextSeasonAvgBlk", maxIter=4)
    grid = (ParamGridBuilder()
            .addGrid(lr.maxIter, [1, 4])
            .addGrid(lr.regParam, [0.1, 0.01])
            .addGrid(lr.elasticNetParam, [0.0, 1.0])
            .build())
    cv = CrossValidator(estimator=lr, estimatorParamMaps=grid, evaluator=r2_evaluator, numFolds=10)
    pipelineCV = Pipeline(stages=[SQLTransformer(statement=sqlStatement), position_indexer, status_indexer,
                                    position_encoder, status_encoder, vectorAssembler, cv])
    lrModelCV = pipelineCV.fit(train)
    trainDF = lrModelCV.transform(train)
    r2_train = r2_evaluator.evaluate(trainDF)
    print(f"r2 training for predicting nextSeasonAvgBlk is {r2_train}")
    predDF = lrModelCV.transform(validation)
    r2 = r2_evaluator.evaluate(predDF)
    print(f"r2 validation for predicting nextSeasonAvgBlk is {r2}")
    lrCV = lrModelCV.stages[-1].bestModel
    lrModelCV.write().overwrite().save(outputs)
    # print(lrCV.coefficients)
    # print(lrCV.intercept)
    
    trainDF = (trainDF
               .withColumn("residual", functions.col("nextSeasonAvgBlk") - functions.col("prediction")))
    
    plot_residual(trainDF.select("count").collect(), trainDF.select("residual").collect(), "LOG(number of injuries)", "residual")
    plot_residual(trainDF.select("age").collect(), trainDF.select("residual").collect(), "age", "residual")
    plot_residual(trainDF.select("height").collect(), trainDF.select("residual").collect(), "height", "residual")
    plot_residual(trainDF.select("weight").collect(), trainDF.select("residual").collect(), "weight", "residual")
    plot_residual(trainDF.select("avgBlk").collect(), trainDF.select("residual").collect(), "avgBlk", "residual")
    
    player = (player
              .withColumn("avgBlk", functions.col("totalBlk")/functions.col("totalGames")))
    player.cache()
    plot_scatter(player.select("count").collect(), player.select("avgBlk").collect(), "number of injuries",
                           "average Block")
    plot_scatter(player.select("age").collect(), player.select("avgBlk").collect(), "age",
                           "average Block")
    plot_scatter(player.select("player_height").collect(), player.select("avgBlk").collect(), "height",
                           "average Block")
    plot_scatter(player.select("player_weight").collect(), player.select("avgBlk").collect(), "weight",
                           "average Block")
    
    plot_validation_result(predDF.select("prediction").collect(), predDF.select("nextSeasonAvgBlk").collect())    

 
    # df = trainDF.select("age", "count", "height", "weight", "avgAst", "nextSeasonAge",
    #                   "nextSeasonHeight", "nextSeasonWeight", "nextSeasonAvgAst").toPandas()
    # plot_corr(df)
    
    



if __name__ == '__main__':
    player_inputs = sys.argv[1]
    outputs = sys.argv[2]
    spark = SparkSession.builder.appName('example code').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main()
