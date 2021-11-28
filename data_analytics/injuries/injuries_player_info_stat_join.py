from pyspark.sql import SparkSession, functions, types
import re
import sys
assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+


# add more functions as necessary
@functions.udf(returnType=types.BooleanType())
def is_name_same(name1, name2):
    name1 = re.sub('[^A-Za-z0-9]+', '', name1).lower()
    name2 = re.sub('[^A-Za-z0-9]+', '', name2).lower()
    return name1 == name2
    

def main():
    # load injury dataset
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
                .load(injuries_inputs)
                .where((functions.col("injury_name") != "placed on IL") & (functions.col("injury_name") != "fined $50,000 by NBA for using inappropriate language during game"))
                .withColumn("status",
                            functions.when(functions.col("status").isNull(), "do not rest").otherwise(functions.col("status")))
                .withColumn("year", functions.year(functions.col("Date")))
                .withColumn("month", functions.month(functions.col("Date")))
                # 2019 season is a special season
                .withColumn("played_season",
                            functions.when(functions.col("year")
                                           == 2020, functions.col("year") - 1)
                            .when(functions.col("month") >= 10, functions.col("year"))
                            .otherwise(functions.col("year") - 1))
                .drop("year")
                .drop("month")
                .orderBy("Relinquished", "Date"))
    # count how many injuries each player has in each season, and only show the last injury name and status in each season
    injuries = (injuries
                .groupBy(functions.col("Relinquished"), functions.col("played_season"))
                .agg(functions.count("injury_name").alias("count"), functions.first("injury_name").alias("injury_name"),
                     functions.first("status").alias("status"), functions.first("Date").alias("Date"))
                .orderBy(functions.col("Relinquished"), functions.col("played_season"))
                .repartition(8))
    # load player stat summary from 2010 to 2020 dataset
    player_stat_summary = (spark.read
                           .option("delimiter", ",")
                           .option("header", "true")
                           .csv(player_stat_summary_inputs)
                           .repartition(8))
    # load player general info from 2010 to 2020
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
                   .load(player_info_inputs)
                   .withColumnRenamed("player_name", "playerName")
                   .withColumnRenamed("PLAYER_ID", "playerID"))

    # join dataframes
    player = (player_stat_summary
              .join(injuries,
                    (functions.col("played_season") == functions.col("year")) &
                    (functions.regexp_replace(injuries["Relinquished"], r'\.', "") == functions.regexp_replace(
                        player_stat_summary["PLAYER_NAME"], r'\.', "")),
                    "Right"))
    player = (player
     .groupBy(functions.col("PLAYER_NAME"), functions.col("year"))
     .agg(functions.sum(functions.col("sum(PTS)")).alias("totalPts"),
          functions.sum(functions.col("sum(PF)")).alias("totalPf"),
          functions.sum(functions.col("sum(TO)")).alias("totalTo"),
          functions.sum(functions.col("sum(BLK)")).alias("totalBlk"),
          functions.sum(functions.col("sum(STL)")).alias("totalStl"),
          functions.sum(functions.col("sum(AST)")).alias("totalAst"),
          functions.sum(functions.col("sum(REB)")).alias("totalReb"),
          functions.sum(functions.col("sum(DREB)")
                        ).alias("totalDreb"),
          functions.sum(functions.col("sum(OREB)")
                        ).alias("totalOreb"),
          functions.sum(functions.col("sum(FTA)")).alias("totalFta"),
          functions.sum(functions.col("sum(FTM)")).alias("totalFtm"),
          functions.sum(functions.col("sum(FG3A)")
                        ).alias("totalFg3a"),
          functions.sum(functions.col("sum(FG3M)")
                        ).alias("totalFg3m"),
          functions.sum(functions.col("sum(FGA)")).alias("totalFga"),
          functions.sum(functions.col("sum(FGM)")).alias("totalFgm"),
          functions.sum(functions.col("sum(ifminute)")).alias("totalGames"),
          functions.first("injury_name").alias("injury_name"),
          functions.first("status").alias("status"),
          functions.first("count").alias("count"),
        #   functions.first("age"),
        #   functions.first("player_position"),
        #   functions.first("player_height"),
        #   functions.first("player_weight")
          )
     .orderBy(functions.col("PLAYER_NAME"), "year"))

    player = (player
              .join(player_info,
                    (player["year"].cast(types.StringType()) == player_info["season"]) &
                    is_name_same(player["PLAYER_NAME"], player_info["playerName"])
                    # (functions.regexp_replace(player["PLAYER_NAME"], r'\.', "") == functions.regexp_replace(player_info["playerName"], r'\.', ""))
                    )
              .drop(functions.col("season"))
              .drop(functions.col("TEAM_ID"))
              .drop(functions.col("draft_year"))
              .drop(functions.col("draft_round"))
              .drop(functions.col("draft_number"))
              .drop(functions.col("PLAYER_ID"))
              .drop(functions.col("playerName"))
              .drop(functions.col("playerID"))
              .drop(functions.col("Relinquished"))
              .where(~functions.col("status").isNull())
              .where(~functions.col("count").isNull())
              .where(~functions.col("player_position").isNull())
              .where(~functions.col("player_height").isNull())
              .where(~functions.col("player_weight").isNull())
              .where(~functions.col("age").isNull())
              .where(~functions.col("totalPts").isNull())
              .orderBy(functions.col("PLAYER_NAME"), functions.col("year")))
    # player.cache()
    # print(player.count())
    # player.show()
    player.coalesce(1).write.option("header", "true").csv(outputs, mode='overwrite')



if __name__ == '__main__':
    injuries_inputs = sys.argv[1]
    player_stat_summary_inputs = sys.argv[2]
    player_info_inputs = sys.argv[3]
    outputs = sys.argv[4]
    spark = SparkSession.builder.appName('example code').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main()
