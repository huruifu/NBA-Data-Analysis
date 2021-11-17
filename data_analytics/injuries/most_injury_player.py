import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
from plot_tools import plot_barhgraph
from pyspark.sql import SparkSession, functions, types

# add more functions as necessary

def main(inputs):
    # main logic starts here
    injuries_schema = types.StructType([
        types.StructField('Date', types.StringType()),
        types.StructField('Team', types.StringType()),
        types.StructField('Relinquished', types.StringType()),
        types.StructField('injury_name', types.StringType()),
        types.StructField('status', types.StringType())
    ])
    injuries = (spark.read.format("csv")
                .option("header", "true")
                .schema(injuries_schema)
                .load(inputs))
    # looking into players who get injuries most
    most_injury_player = (injuries
     .groupBy(functions.col("Relinquished"))
     .agg(functions.count("*").alias("injuries_times"))
     .orderBy(functions.col("injuries_times").desc())
     .select(functions.col("Relinquished").alias("playerName"), functions.col("injuries_times")))
    most_injury_player.cache()
    count_list = most_injury_player.head(40)
    plot_barhgraph(count_list, "playerName", "injuries_times", "players who get injury most")

if __name__ == '__main__':
    inputs = sys.argv[1]
    spark = SparkSession.builder.appName('example code').getOrCreate()
    assert spark.version >= '3.0' # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(inputs)