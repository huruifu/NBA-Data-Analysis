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
                .load(inputs)
                .repartition(8))
    # looking into players who get injuries most
    # Bobcats change team name to Hornets, so we combine two rows into one
    most_injury_team = (injuries
     .groupBy(functions.col("Team"))
     .agg(functions.count("*").alias("injuries_times"))
     .orderBy(functions.col("injuries_times").desc()))
    most_injury_team.cache()
    bobcats = (most_injury_team
               .where(functions.col("Team") == "Bobcats"))
    bobcats_injuries_times = bobcats.head()["injuries_times"]
    print(f"bobcats team has {bobcats_injuries_times}")
    most_injury_team = (most_injury_team
                        .where(functions.col("Team") != "Bobcats")
                        .withColumn("injuries_times",
                                    functions.when(functions.col("Team") == "Hornets", functions.col("injuries_times") + bobcats_injuries_times)
                                    .otherwise(functions.col("injuries_times")))
                        .orderBy(functions.col("injuries_times").desc()))
    most_injury_team.cache()
    most_injury_team.show()
    count_list = most_injury_team.collect()
    plot_barhgraph(count_list, "Team", "injuries_times", "Teams which most injury event happened")

if __name__ == '__main__':
    inputs = sys.argv[1]
    spark = SparkSession.builder.appName('example code').getOrCreate()
    assert spark.version >= '3.0' # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(inputs)