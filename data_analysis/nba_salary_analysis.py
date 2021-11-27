import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+

from pyspark.sql import SparkSession, functions, types
from pyspark.sql.types import DateType
from pyspark.sql.functions import avg, sum, count, when
from pyspark.sql.functions import avg, col, when
from pyspark.sql.window import Window

from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler, SQLTransformer
from pyspark.ml.regression import GBTRegressor, RandomForestRegressor, DecisionTreeRegressor
from pyspark.ml.evaluation import RegressionEvaluator

import pandas as pd
import matplotlib.pyplot as plt

import pip
pip.main(['install','seaborn'])
import seaborn as sns


salary_schema = types.StructType([
    types.StructField('PLAYER_NAME', types.StringType()),
    types.StructField('season', types.IntegerType()),
    types.StructField('PLAYER_ID', types.StringType()),
    types.StructField('TEAM_ID', types.StringType()),
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

def main(salary_path):
    # main logic starts here
    #salary_path = "/Users/sarahhu/Desktop/SFUgrad/CMPT732/732Project/732-project/data/clean_data/salary_etl"
    salary = spark.read.option("delimiter", ",").option("header", "true").csv(salary_path, schema=salary_schema)

    salary_df = salary.toPandas()
    print(salary_df.corr())

    sns.set_style("white")
    sns.heatmap(salary_df.corr())
    plt.show()

if __name__ == '__main__':
    salary_path = sys.argv[1]
    #output = sys.argv[2]
    spark = SparkSession.builder.appName('NBA ETL process').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(salary_path)

