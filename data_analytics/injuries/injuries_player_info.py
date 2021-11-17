from pyspark.sql import SparkSession, functions, types
from plot_tools import plot_players_most_injury_bargraph
import sys
assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+

# add more functions as necessary


def main(injuries_inputs, player_info_inputs):
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
                .load(injuries_inputs))
    most_injury_player = (injuries
                          .groupBy(functions.col("Relinquished"))
                          .agg(functions.count("*").alias("injuries_times"))
                          .orderBy(functions.col("injuries_times").desc())
                          .select(functions.col("Relinquished").alias("playerName"), functions.col("injuries_times")))
    most_injury_player.cache()
    print(f"number of rows in most_injury_player: {most_injury_player.count()}")
    # looking into is there any relationship between players who injury most and weight, height, position, age
    # load player_info dataset
    player_info_schema = types.StructType([
        types.StructField('player_name', types.StringType()),
        types.StructField('player_position', types.StringType()),
        types.StructField('team_abbreviation', types.StringType()),
        types.StructField('age', types.FloatType()),
        types.StructField('player_height', types.FloatType()),
        types.StructField('player_weight', types.FloatType()),
        types.StructField('season', types.StringType()),
        types.StructField('draft_year', types.StringType()),
        types.StructField('draft_round', types.StringType()),
        types.StructField('draft_number', types.StringType()),
        types.StructField('PLAYER_ID', types.StringType())
    ])
    player_info = (spark.read.format("csv")
                   .option("header", "true")
                   .schema(player_info_schema)
                   .load(player_info_inputs))
    player_info = (player_info
                   .groupBy(functions.col("player_name"))
                   .agg(
                       functions.avg("player_height").alias("height_avg"),
                       functions.avg("player_weight").alias("weight_avg"),
                       functions.max("age").alias("age"),
                       functions.first("player_position").alias(
                           "player_position")
                   ))
    joinedDF = (most_injury_player
                .join(player_info,
                      player_info["player_name"] == functions.regexp_replace(most_injury_player["playerName"], r'\.', ""))
                .select(functions.col("player_name"), functions.col("injuries_times"),
                        functions.col("player_position"), functions.col(
                            "age"), functions.col("height_avg"),
                        functions.col("weight_avg"))
                .orderBy(functions.col("injuries_times").desc()))
    print(f"number of rows in joinedDF: {joinedDF.count()}")
    joinedDF.show()


if __name__ == '__main__':
    injuries_inputs = sys.argv[1]
    player_info_inputs = sys.argv[2]
    spark = SparkSession.builder.appName('example code').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(injuries_inputs, player_info_inputs)
