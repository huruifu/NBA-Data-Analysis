# use command to run:
# ${SPARK_HOME}/bin/spark-submit data_analysis/nba_salary_analysis.py data/clean_data/salary_etl

import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+

from pyspark.sql import SparkSession, functions, types
from pyspark.sql.types import DateType
from pyspark.sql.functions import avg, sum, count, when
from pyspark.sql.functions import avg, col, when
from pyspark.sql.window import Window

from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler, SQLTransformer
from pyspark.ml.regression import GBTRegressor, RandomForestRegressor, DecisionTreeRegressor, GeneralizedLinearRegression, LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pip
pip.main(['install','seaborn'])
import seaborn as sns
from IPython.display import display

salary_schema = types.StructType([
    types.StructField('PLAYER_NAME', types.StringType()),
    types.StructField('season', types.FloatType()),
    types.StructField('PLAYER_ID', types.StringType()),
    types.StructField('avg(FGM)', types.FloatType()),
    types.StructField('avg(FGA)', types.FloatType()),
    types.StructField('avg(FG3M)', types.FloatType()),
    types.StructField('avg(FG3A)', types.FloatType()),
    types.StructField('avg(FTM)', types.FloatType()),
    types.StructField('avg(FTA)', types.FloatType()),
    types.StructField('avg(OREB)', types.FloatType()),
    types.StructField('avg(DREB)', types.FloatType()),
    types.StructField('avg(REB)', types.FloatType()),
    types.StructField('avg(AST)', types.FloatType()),
    types.StructField('avg(STL)', types.FloatType()),
    types.StructField('avg(BLK)', types.FloatType()),
    types.StructField('avg(TO)', types.FloatType()),
    types.StructField('avg(PF)', types.FloatType()),
    types.StructField('avg(PTS)', types.FloatType()),
    types.StructField('avg(PLUS_MINUS)', types.FloatType()),
    types.StructField('sum(FGM)', types.FloatType()),
    types.StructField('sum(FGA)', types.FloatType()),
    types.StructField('sum(FG3M)', types.FloatType()),
    types.StructField('sum(FG3A)', types.FloatType()),
    types.StructField('sum(FTM)', types.FloatType()),
    types.StructField('sum(FTA)', types.FloatType()),
    types.StructField('sum(OREB)', types.FloatType()),
    types.StructField('sum(DREB)', types.FloatType()),
    types.StructField('sum(REB)', types.FloatType()),
    types.StructField('sum(AST)', types.FloatType()),
    types.StructField('sum(STL)', types.FloatType()),
    types.StructField('sum(BLK)', types.FloatType()),
    types.StructField('sum(TO)', types.FloatType()),
    types.StructField('sum(PF)', types.FloatType()),
    types.StructField('sum(PTS)', types.FloatType()),
    types.StructField('sum(PLUS_MINUS)', types.FloatType()),
    types.StructField('sum(ifminute)', types.FloatType()),
    types.StructField('avg(seconds)', types.FloatType()),
    types.StructField('sum(seconds)', types.FloatType()),
    types.StructField('age', types.FloatType()),
    types.StructField('player_height', types.FloatType()),
    types.StructField('player_weight', types.FloatType()),
    types.StructField('injuries', types.FloatType()),
    types.StructField('salary', types.FloatType())
])

def plot_validation_result(predicts, actuals):
    predicts_np = np.array(predicts)
    actuals_np = np.array(actuals)
    plt.figure(figsize=(10,10))
    plt.scatter(predicts_np, actuals_np, c='crimson')
    plt.yscale('log')
    plt.xscale('log')
    p1 = max(max(predicts_np), max(actuals_np))
    p2 = min(min(predicts_np), min(actuals_np))
    plt.plot([p1, p2], [p1, p2], 'b-')
    plt.xlabel('Salary Predictions', fontsize=15)
    plt.ylabel('True Values', fontsize=15)
    plt.axis('equal')

def main(salary_path):
    # main logic starts here
    #salary_path = "/Users/sarahhu/Desktop/SFUgrad/CMPT732/732Project/732-project/data/clean_data/salary_etl"
    salary = spark.read.option("delimiter", ",").option("header", "true").csv(salary_path, schema=salary_schema)
    salary = salary.drop('PLAYER_ID','PLAYER_NAME')
    salary = salary.na.fill(value=0)

    salary_df = salary.toPandas()
    print(salary_df.corr())
    plt.figure()
    sns.set_style("white")
    sns.heatmap(salary_df.corr())
    plt.savefig('web-presentation/front-end/public/salary_correlation.png')

    plt.figure()
    print(salary_df['salary'].describe())
    plt.hist(salary_df['salary'], density=True, bins=60)
    plt.xlabel('NBA player Salary')
    plt.ylabel('Density')
    plt.savefig('web-presentation/front-end/public/salary_histogram.png')

    plt.figure()
    salary_df.boxplot('salary', by="season")
    plt.ylabel('salary')
    plt.savefig('web-presentation/front-end/public/salary_boxplot_byyear.png')

    train, validation = salary.randomSplit([0.75, 0.25])
    train = train.cache()
    validation = validation.cache()

    assembler = VectorAssembler(
    inputCols=['season', 'avg(FGM)', 'avg(FGA)', 'avg(FG3M)', 'avg(FG3A)', 'avg(FTM)', 'avg(FTA)', 'avg(OREB)',\
                   'avg(DREB)', 'avg(REB)', 'avg(AST)', 'avg(STL)', 'avg(BLK)', 'avg(TO)', 'avg(PF)', 'avg(PTS)',\
                   'avg(PLUS_MINUS)', 'sum(FGM)', 'sum(FGA)', 'sum(FG3M)', 'sum(FG3A)', 'sum(FTM)', 'sum(FTA)',\
                   'sum(OREB)', 'sum(DREB)', 'sum(REB)', 'sum(AST)', 'sum(STL)', 'sum(BLK)', 'sum(TO)', 'sum(PF)',\
                   'sum(PTS)', 'sum(PLUS_MINUS)', 'sum(ifminute)', 'avg(seconds)', 'sum(seconds)', 'age',\
                   'player_height', 'player_weight', 'injuries'], outputCol='features')
    # indexer1 = StringIndexer(inputCol="PLAYER_NAME", outputCol="PLAYER_NAME_index", handleInvalid="keep")
    # regressor = RandomForestRegressor(featuresCol='features', labelCol='salary', numTrees=3, maxDepth=5, seed=42)
    # regressor = GeneralizedLinearRegression(featuresCol="features", labelCol="salary", regParam=2, maxIter=5) #0.56
    # regressor = GBTRegressor(featuresCol='features', labelCol='salary') #0.52
    regressor = RandomForestRegressor(featuresCol='features', labelCol='salary', numTrees=4, maxDepth=6, seed=42)  # 0.60
    nba_pipeline = Pipeline(stages=[assembler, regressor])
    nba_model = nba_pipeline.fit(train)
    predictions = nba_model.transform(validation)
    r2_evaluator = RegressionEvaluator(predictionCol='prediction', labelCol='salary', metricName='r2')
    rmse_evaluator = RegressionEvaluator(predictionCol='prediction', labelCol='salary', metricName='rmse')
    r2 = r2_evaluator.evaluate(predictions)
    rmse = rmse_evaluator.evaluate(predictions)
    print('Validation score (R*2) for salary model:', r2)
    print('Validation score (RMSE) for salary model:', rmse)
    print('parameters:', nba_model.stages[-1])
    print('importance:', nba_model.stages[-1].featureImportances)

    feature_list = []
    for col in salary.columns:
        if col == 'salary':
            continue
        else:
            feature_list.append(col)
    importances = nba_model.stages[-1].featureImportances
    x_values = list(range(len(importances)))
    plt.figure()
    plt.bar(x_values, importances, orientation='vertical')
    plt.xticks(x_values, feature_list, rotation=40)
    plt.ylabel('Importance')
    plt.xlabel('Feature')
    plt.title('Feature Importances')
    plt.savefig('web-presentation/front-end/public/salary_featureImportance.png')

    #display(nba_model.stages[-1])
    #plt.savefig(nba_model.stages[-1])

    plot_validation_result(predictions.select("prediction").collect(), predictions.select("salary").collect())
    plt.savefig('web-presentation/front-end/public/salary_predictions.png')


if __name__ == '__main__':
    salary_path = sys.argv[1]
    #output = sys.argv[2]
    spark = SparkSession.builder.appName('NBA ETL process').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(salary_path)

