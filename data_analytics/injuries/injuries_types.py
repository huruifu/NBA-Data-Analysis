import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+

from pyspark.sql import SparkSession, functions, types

# add more functions as necessary

def main(inputs):
    injuries_schema = types.StructType([
        types.StructField('Date', types.DateType()),
        types.StructField('Team', types.StringType()),
        types.StructField('Relinquished', types.StringType()),
        types.StructField('injury_name', types.StringType()),
        types.StructField('status', types.StringType())
    ])
    injuries = (spark.read.format("csv")
                .option("header", "true")
                .schema(injuries_schema)
                .load(inputs))
    injuries.cache()
    positions = injuries.groupBy()
    injuries.show()

if __name__ == '__main__':
    inputs = sys.argv[1]
    spark = SparkSession.builder.appName('example code').getOrCreate()
    assert spark.version >= '3.0' # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(inputs)