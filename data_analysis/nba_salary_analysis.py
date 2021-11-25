import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+

from pyspark.sql import SparkSession, functions, types
from pyspark.sql.types import DateType
from pyspark.sql.functions import avg, sum, count, when



def main(games_path, gmDetail_path, output):
    # main logic starts here



if __name__ == '__main__':
    games_path = sys.argv[1]
    gmDetail_path = sys.argv[2]
    output = sys.argv[3]
    spark = SparkSession.builder.appName('NBA ETL process').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(games_path, gmDetail_path, output)
