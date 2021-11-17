from pyspark.sql import SparkSession, functions, types
import sys
assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+
from plot_tools import plot_players_most_injury_bargraph


# add more functions as necessary


def main(injuries_inputs, player_info_inputs, outputs):
    # loading injuries data in spark dataframe
    injuries_schema = types.StructType([
        types.StructField('Date', types.StringType()),
        types.StructField('Team', types.StringType()),
        types.StructField('Acquired', types.StringType()),
        types.StructField('Relinquished', types.StringType()),
        types.StructField('Notes', types.StringType())
    ])
    injuries = (spark.read.format("csv")
                .option("header", "true")
                .schema(injuries_schema)
                .load(injuries_inputs))
    # There are two data rows that Date, Team and Notes is null.
    # We can ignore these two rows.

    # looking into acquired data is not null
    # if acquired data is not null, it means that the player returned to the court soon after injuries
    # we can ignore these cases as these injuries have little affect to players.
    acquired = (injuries
                .where(~functions.col("Acquired").isNull())
                .where(~functions.col("Date").isNull())
                .where(~functions.col("Team").isNull())
                .where(~functions.col("Notes").isNull()))
    acquired.show()

    # looking into Relinquished data is not null
    # if relinquished data is not null, it means player get injuries in a specific date
    # For the note, in some rows, note has two components, one is injury name, another one is status
    # We need to separate these two components for further analytics
    relinquished = (injuries
                    .where(~functions.col("relinquished").isNull())
                    .where(~functions.col("Date").isNull())
                    .where(~functions.col("Team").isNull())
                    .where(~functions.col("Notes").isNull())
                    .withColumn("injury_name", functions.regexp_replace(functions.col("Notes"), r'\((.*?)\)', ""))
                    .withColumn("status", functions.regexp_extract(functions.col("Notes"), r'\((.*?)\)', 1))
                    .drop(functions.col("Acquired"))
                    .drop(functions.col("Notes")))
    relinquished.cache()
    # print(f"number of rows in relinquished: {relinquished.count()}")
    relinquished.show()
    # relinquished.coalesce(1).write.option("header", "true").csv(outputs, mode='overwrite')
    
    # looking into players who get injuries most
    most_injury_player = (relinquished
     .groupBy(functions.col("Relinquished"))
     .agg(functions.count("*").alias("injuries_times"))
     .orderBy(functions.col("injuries_times").desc())
     .select(functions.col("Relinquished").alias("playerName"), functions.col("injuries_times")))
    most_injury_player.cache()
    print(f"number of rows in most_injury_player: {most_injury_player.count()}")
    # count_list = most_injury_player.head(40)
    # plot_players_most_injury_bargraph(count_list, "playerName", "injuries_times", "players who get injury most")
    
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
                       functions.first("player_position").alias("player_position")
                   ))
    joinedDF = (most_injury_player
                .join(player_info,
                      player_info["player_name"] == functions.regexp_replace(most_injury_player["playerName"], r'\.', ""))
                .select(functions.col("player_name"), functions.col("injuries_times"),
                        functions.col("player_position"), functions.col("age"), functions.col("height_avg"),
                        functions.col("weight_avg"))
                .orderBy(functions.col("injuries_times").desc()))
    print(f"number of rows in joinedDF: {joinedDF.count()}")
    joinedDF.show()
    


if __name__ == '__main__':
    injuries_inputs = sys.argv[1]
    player_info_inputs = sys.argv[2]
    outputs = sys.argv[3]
    spark = SparkSession.builder.appName(
        'injuries and player stat data analytics').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(injuries_inputs, player_info_inputs, outputs)
