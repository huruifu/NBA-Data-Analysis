from pyspark.sql import SparkSession, functions, types
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler, SQLTransformer
from pyspark.ml.regression import GBTRegressor, RandomForestRegressor, GeneralizedLinearRegression, LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

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
              .repartition(8))

    train, validation = player.randomSplit([0.8, 0.2])
    train = train.cache()
    validation = validation.cache()
    position_indexer = StringIndexer(
        inputCol="player_position", outputCol="player_position_index", stringOrderType="frequencyDesc", handleInvalid="skip")
    status_indexer = StringIndexer(
        inputCol="status", outputCol="status_index", stringOrderType="frequencyDesc", handleInvalid="skip")
    
    # training models predicting total pts in the next season
    vectorAssembler = VectorAssembler(inputCols=["age1", "status_index", "count", "player_height", "player_weight",
                                                 "player_position_index", "age2", "totalPts"],
                                      outputCol="features")
    rmse_evaluator = RegressionEvaluator(
        predictionCol="prediction", labelCol="nextSeasonPts", metricName="rmse")
    r2_evaluator = RegressionEvaluator(
        predictionCol="prediction", labelCol="nextSeasonPts", metricName="r2")
    sqlStatement = (
        """
    SELECT t0.age AS age1, t0.status, t0.count, t1.player_height, t1.player_weight, t1.player_position,
    t1.age AS age2, t0.totalPts, t1.totalPts AS nextSeasonPts
    FROM __THIS__ as t0
    INNER JOIN __THIS__ as t1
    ON t0.year + 1 = t1.year
    AND t0.PLAYER_NAME = t1.PLAYER_NAME
    """)
    position_indexer = StringIndexer(
        inputCol="player_position", outputCol="player_position_index", stringOrderType="frequencyDesc", handleInvalid="skip")
    status_indexer = StringIndexer(
        inputCol="status", outputCol="status_index", stringOrderType="frequencyDesc", handleInvalid="skip")

    # gbtr = GBTRegressor(featuresCol="features", labelCol="nextSeasonPts", maxIter=10,
    #                     maxDepth=5, stepSize=0.1, seed=42, featureSubsetStrategy='all')
    # gbtrPipeline = Pipeline(stages=[SQLTransformer(statement=sqlStatement), position_indexer, status_indexer,
    #                                 vectorAssembler, gbtr])
    # gbtrPipelineModel = gbtrPipeline.fit(train)
    # trainDF = gbtrPipelineModel.transform(train)
    # rmse_train = rmse_evaluator.evaluate(trainDF)
    # r2_train = r2_evaluator.evaluate(trainDF)
    # print(f"RMSE training for predicting nextSeasonPts is {rmse_train}")
    # print(f"r2 training for predicting nextSeasonPts is {r2_train}")
    # predDF = gbtrPipelineModel.transform(validation)
    # rmse = rmse_evaluator.evaluate(predDF)
    # r2 = r2_evaluator.evaluate(predDF)
    # print(f"RMSE validation for predicting nextSeasonPts is {rmse}")
    # print(f"r2 validation for predicting nextSeasonPts is {r2}")
    # gbtrPipelineModel.write().overwrite().save(outputs)

    # rfr = RandomForestRegressor(featuresCol="features", labelCol="nextSeasonPts",
    #                     numTrees=8, maxDepth=5, seed=42)
    # rfrPipeline = Pipeline(stages=[SQLTransformer(statement=sqlStatement), position_indexer, status_indexer,
    #                                 vectorAssembler, rfr])
    # rfrPipelineModel = rfrPipeline.fit(train)
    # trainDF = rfrPipelineModel.transform(train)
    # rmse_train = rmse_evaluator.evaluate(trainDF)
    # r2_train = r2_evaluator.evaluate(trainDF)
    # print(f"RMSE training for predicting nextSeasonPts is {rmse_train}")
    # print(f"r2 training for predicting nextSeasonPts is {r2_train}")
    # predDF = rfrPipelineModel.transform(validation)
    # rmse = rmse_evaluator.evaluate(predDF)
    # r2 = r2_evaluator.evaluate(predDF)
    # print(f"RMSE validation for predicting nextSeasonPts is {rmse}")
    # print(f"r2 validation for predicting nextSeasonPts is {r2}")
    # rfrPipelineModel.write().overwrite().save(outputs)
    
    # training models predicting total To in the next season
    # vectorAssembler = VectorAssembler(inputCols=["age1", "status_index", "count", "player_height", "player_weight",
    #                                              "player_position_index", "age2", "totalTo"],
    #                                   outputCol="features")
    # rmse_evaluator = RegressionEvaluator(
    #     predictionCol="prediction", labelCol="nextSeasonTo", metricName="rmse")
    # r2_evaluator = RegressionEvaluator(
    #     predictionCol="prediction", labelCol="nextSeasonTo", metricName="r2")
    # sqlStatement = (
    #     """
    # SELECT t0.age AS age1, t0.status, t0.count, t1.player_height, t1.player_weight, t1.player_position,
    # t1.age AS age2, t0.totalTo, t1.totalTo AS nextSeasonTo
    # FROM __THIS__ as t0
    # INNER JOIN __THIS__ as t1
    # ON t0.year + 1 = t1.year
    # AND t0.PLAYER_NAME = t1.PLAYER_NAME
    # """)
    # rfr = RandomForestRegressor(featuresCol="features", labelCol="nextSeasonTo",
    #                     numTrees=8, maxDepth=5, seed=42)
    # rfrPipeline = Pipeline(stages=[SQLTransformer(statement=sqlStatement), position_indexer, status_indexer,
    #                                 vectorAssembler, rfr])
    # rfrPipelineModel = rfrPipeline.fit(train)
    # trainDF = rfrPipelineModel.transform(train)
    # rmse_train = rmse_evaluator.evaluate(trainDF)
    # r2_train = r2_evaluator.evaluate(trainDF)
    # print(f"Using GBTRegressor, RMSE training is {rmse_train}")
    # print(f"Using GBTRegressor, r2 training is {r2_train}")
    # predDF = rfrPipelineModel.transform(validation)
    # rmse = rmse_evaluator.evaluate(predDF)
    # r2 = r2_evaluator.evaluate(predDF)
    # print(f"Using GBTRegressor, RMSE validation is {rmse}")
    # print(f"Using GBTRegressor, r2 validation is {r2}")
    # rfrPipelineModel.write().overwrite().save(outputs)
    
    # gbtr = GBTRegressor(featuresCol="features", labelCol="nextSeasonTo", maxIter=8,
    #                     maxDepth=5, stepSize=0.1, seed=42, featureSubsetStrategy='all')
    # gbtrPipeline = Pipeline(stages=[SQLTransformer(statement=sqlStatement), position_indexer, status_indexer,
    #                                 vectorAssembler, gbtr])
    # gbtrPipelineModel = gbtrPipeline.fit(train)
    # trainDF = gbtrPipelineModel.transform(train)
    # rmse_train = rmse_evaluator.evaluate(trainDF)
    # r2_train = r2_evaluator.evaluate(trainDF)
    # print(f"RMSE training for predicting nextSeasonTo is {rmse_train}")
    # print(f"r2 training for predicting nextSeasonTo is {r2_train}")
    # predDF = gbtrPipelineModel.transform(validation)
    # rmse = rmse_evaluator.evaluate(predDF)
    # r2 = r2_evaluator.evaluate(predDF)
    # print(f"RMSE validation for predicting nextSeasonTo is {rmse}")
    # print(f"r2 validation for predicting nextSeasonTo is {r2}")
    # gbtrPipelineModel.write().overwrite().save(outputs)
    
    # predict number of injuries next season, does not have accurate model
    # vectorAssembler = VectorAssembler(inputCols=["age1", "status_index", "count", "player_height", "player_weight",
    #                                              "player_position_index", "age2"],
    #                                   outputCol="features")
    # rmse_evaluator = RegressionEvaluator(
    #     predictionCol="prediction", labelCol="nextSeasonCount", metricName="rmse")
    # r2_evaluator = RegressionEvaluator(
    #     predictionCol="prediction", labelCol="nextSeasonCount", metricName="r2")
    # sqlStatement = (
    #     """
    # SELECT t0.age AS age1, t0.status, t0.count, t1.player_height, t1.player_weight, t1.player_position,
    # t1.age AS age2, t0.totalTo, t1.count AS nextSeasonCount
    # FROM __THIS__ as t0
    # INNER JOIN __THIS__ as t1
    # ON t0.year + 1 = t1.year
    # AND t0.PLAYER_NAME = t1.PLAYER_NAME
    # """)
    
    # lr = LinearRegression(featuresCol="features", labelCol="nextSeasonCount", regParam=2, maxIter=5)
    # lrPipeline = Pipeline(stages=[SQLTransformer(statement=sqlStatement), position_indexer, status_indexer,
    #                                 vectorAssembler, lr])
    # lrPipelineModel = lrPipeline.fit(train)
    # trainDF = lrPipelineModel.transform(train)
    # rmse_train = rmse_evaluator.evaluate(trainDF)
    # r2_train = r2_evaluator.evaluate(trainDF)
    # print(f"RMSE training for predicting nextSeasonCount is {rmse_train}")
    # print(f"r2 training for predicting nextSeasonCount is {r2_train}")
    # predDF = lrPipelineModel.transform(validation)
    # rmse = rmse_evaluator.evaluate(predDF)
    # r2 = r2_evaluator.evaluate(predDF)
    # print(f"RMSE validation for predicting nextSeasonCount is {rmse}")
    # print(f"r2 validation for predicting nextSeasonCount is {r2}")
    # lrPipelineModel.write().overwrite().save(outputs)
    
    # rfr = RandomForestRegressor(featuresCol="features", labelCol="nextSeasonCount",
    #                     numTrees=10, maxDepth=10, seed=42)
    # rfrPipeline = Pipeline(stages=[SQLTransformer(statement=sqlStatement), position_indexer, status_indexer,
    #                                 vectorAssembler, rfr])
    # rfrPipelineModel = rfrPipeline.fit(train)
    # trainDF = rfrPipelineModel.transform(train)
    # rmse_train = rmse_evaluator.evaluate(trainDF)
    # r2_train = r2_evaluator.evaluate(trainDF)
    # print(f"RMSE training for predicting nextSeasonCount is {rmse_train}")
    # print(f"r2 training for predicting nextSeasonCount is {r2_train}")
    # predDF = rfrPipelineModel.transform(validation)
    # rmse = rmse_evaluator.evaluate(predDF)
    # r2 = r2_evaluator.evaluate(predDF)
    # print(f"RMSE validation for predicting nextSeasonCount is {rmse}")
    # print(f"r2 validation for predicting nextSeasonCount is {r2}")
    # rfrPipelineModel.write().overwrite().save(outputs)



if __name__ == '__main__':
    player_inputs = sys.argv[1]
    outputs = sys.argv[2]
    spark = SparkSession.builder.appName('example code').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main()
