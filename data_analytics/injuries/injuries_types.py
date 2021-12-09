from pyspark.sql import SparkSession, functions, types
from plot_tools import plot_wordfrequency
import sys
assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+

# add more functions as necessary


def main():
    # schema
    injuries_schema = types.StructType([
        types.StructField('Date', types.DateType()),
        types.StructField('Team', types.StringType()),
        types.StructField('Relinquished', types.StringType()),
        types.StructField('injury_name', types.StringType()),
        types.StructField('status', types.StringType()),
        types.StructField('year', types.IntegerType()),
        types.StructField('month', types.IntegerType()),
        types.StructField('played_season', types.IntegerType())
    ])
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

    # load data in dataframe
    injuries = (spark.read.format("csv")
                .option("header", "true")
                .schema(injuries_schema)
                .load(injury_inputs)
                .repartition(8))
    injuries.cache()

    player_info = (spark.read.format("csv")
                   .option("header", "true")
                   .schema(player_info_schema)
                   .load(player_info_inputs)
                   .repartition(8))

    # join two table frame
    player_injury = (injuries
                     .join(player_info,
                           (player_info["player_name"] == functions.regexp_replace(injuries["Relinquished"], r'\.', "")) &
                           (player_info["season"] == injuries["played_season"]))
                     .select("player_name", "player_position", "Team", "age", "player_height", "player_weight",
                             "season", "injury_name", "status"))

    # plot graphs

    # most injury type in pf
    pf = (player_injury
          .where(functions.col("player_position") == "PF")
          .select(functions.col("injury_name"), functions.col("player_position")))
    pf.show()
    plot_wordfrequency(pf.collect())

    # most injury type in f
    f = (player_injury
         .where(functions.col("player_position") == "F")
         .select(functions.col("injury_name"), functions.col("player_position")))
    f.show()
    plot_wordfrequency(f.collect())
    
    # most injury type in pg
    pg = (player_injury
          .where(functions.col("player_position") == "PG")
          .select(functions.col("injury_name"), functions.col("player_position")))
    pg.show()
    plot_wordfrequency(pg.collect())
    
    # most injury type in SF
    sf = (player_injury
          .where(functions.col("player_position") == "SF")
          .select(functions.col("injury_name"), functions.col("player_position")))
    sf.show()
    plot_wordfrequency(sf.collect())
    
    # most injury type in SG
    sg = (player_injury
          .where(functions.col("player_position") == "SG")
          .select(functions.col("injury_name"), functions.col("player_position")))
    sg.show()
    plot_wordfrequency(sg.collect())
    
    # most injury type in C
    c = (player_injury
          .where(functions.col("player_position") == "C")
          .select(functions.col("injury_name"), functions.col("player_position")))
    c.show()
    plot_wordfrequency(c.collect())
    
    # most injury type in G
    g = (player_injury
          .where(functions.col("player_position") == "G")
          .select(functions.col("injury_name"), functions.col("player_position")))
    g.show()
    plot_wordfrequency(g.collect())


if __name__ == '__main__':
    injury_inputs = sys.argv[1]
    player_info_inputs = sys.argv[2]
    spark = SparkSession.builder.appName('check which injury type is the most frequent').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main()
