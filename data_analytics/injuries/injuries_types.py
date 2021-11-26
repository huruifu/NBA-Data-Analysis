import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
from plot_tools import plot_wordfrequency
from pyspark.sql import SparkSession, functions, types

# add more functions as necessary
@functions.udf(returnType=types.StringType())
def format_injury_name(injury_name):
    if "placed on IL with" in injury_name:
        injury_name = injury_name.replace("placed on IL with", "")
    elif "placed on IL for" in injury_name:
        injury_name = injury_name.replace("placed on IL for", "")
    elif "placed on IL recovering from" in injury_name:
        injury_name = injury_name.replace("placed on IL recovering from", "")
    elif "placed on IL recoverimg from" in injury_name:
        injury_name = injury_name.replace("placed on IL recoverimg from", "")
    elif "placed on IL frecovering from" in injury_name:
        injury_name = injury_name.replace("placed on IL frecovering from", "")
    elif injury_name is None:
        return None    
    return injury_name.strip()    


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
                .load(inputs)
                .where((functions.col("injury_name") != "placed on IL") & (functions.col("injury_name") != "fined $50,000 by NBA for using inappropriate language during game"))
                # .withColumn("injury_name", format_injury_name(functions.col("injury_name")))
                # .withColumn("status",
                #             functions.when(functions.col("status").isNull(), "do not rest").otherwise(functions.col("status")))
                # .withColumn("year", functions.year(functions.col("Date")))
                # .withColumn("month", functions.month(functions.col("Date")))
                # # 2019 season is a special season
                # .withColumn("played_season",
                #             functions.when(functions.col("year")
                #                            == 2020, functions.col("year") - 1)
                #             .when(functions.col("month") >= 10, functions.col("year"))
                #             .otherwise(functions.col("year") - 1))
                # .drop("year")
                # .drop("month")
                .drop("Date")
                # .orderBy("Relinquished", "Date")
                )
    injuries.show()
    # print(injuries.head())
    plot_wordfrequency(injuries.collect())

if __name__ == '__main__':
    inputs = sys.argv[1]
    spark = SparkSession.builder.appName('example code').getOrCreate()
    assert spark.version >= '3.0' # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(inputs)