# use command to run:
# ${SPARK_HOME}/bin/spark-submit data_etl/nba_salary_etl.py data/nba/salary_1985to2018.csv data/nba/players_for_salary.csv data/etl_player_summary_output_noTeam data/clean_data/player_info.csv data/nba/injuries_2010-2020.csv data/clean_data/salary_etl

import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+

from pyspark.sql import SparkSession, functions, types
from pyspark.sql.types import DateType
from pyspark.sql.functions import avg, sum, count, when
from pyspark.sql.functions import avg, col, when
from pyspark.sql.window import Window


def main(salary_path, salary_player_path, player_summary_path, player_info_path, injury_path, output):
    # main logic starts here
    salary = spark.read.option("delimiter", ",").option("header", "true").csv(salary_path)
    salary_player = spark.read.option("delimiter", ",").option("header", "true").csv(salary_player_path)
    player_summary = spark.read.option("delimiter", ",").option("header", "true").csv(player_summary_path)
    player_info = spark.read.option("delimiter", ",").option("header", "true").csv(player_info_path)
    injury = spark.read.option("delimiter", ",").option("header", "true").csv(injury_path)

    salary = salary.select('player_id', 'salary', 'season_start')
    salary_player = salary_player.select('_id', 'name')
    salary_df = salary.join(salary_player, salary['player_id'] == salary_player['_id'], 'left')
    salary_df = salary_df.select('name', 'season_start', 'salary')
    player_info = player_info.withColumn("player_name", functions.translate(functions.col("player_name"), ".", ""))
    player_info = player_info.drop('player_position', 'team_abbreviation', 'player_name', 'draft_year', 'draft_round',
                                   'draft_number')
    salary_df = salary_df.withColumn("name", functions.translate(functions.col("name"), ".", ""))
    salary_df = salary_df.withColumnRenamed("name", "PLAYER_NAME").withColumnRenamed("season_start", "season")
    # player_info.filter(col("player_name").contains(".")).show() #check no more dots in name
    # salary_df.filter(col("name").contains(".")).show()

    player_summary = player_summary.withColumnRenamed("year", "season")
    joinedDF = player_summary.join(player_info, ['PLAYER_ID', 'season'], 'left')

    injury = injury.withColumn('Date', functions.substring('Date', 1, 4))
    injury = injury.withColumnRenamed("Date", "season")
    injury = injury.withColumn("Relinquished", functions.translate(functions.col("Relinquished"), ".", ""))
    injury = injury.withColumnRenamed("Relinquished", "PLAYER_NAME")
    injury = injury.withColumn("PLAYER_NAME", functions.translate(functions.col("PLAYER_NAME"), ".", ""))

    injury = injury.withColumn("if_injury", when(injury["Notes"].isNull(), 0).otherwise(1))
    injuryGP = injury.groupBy('season', 'PLAYER_NAME').agg(sum('if_injury').alias('injuries'))

    joinedDF = joinedDF.join(injuryGP, ['PLAYER_NAME', 'season'], 'left')
    joinedDF = joinedDF.join(salary_df, ['PLAYER_NAME', 'season'], 'left')
    # joinedDF = joinedDF.drop("player_name")
    joinedDF = joinedDF.orderBy('season', 'PLAYER_NAME')
    joinedDF = joinedDF.filter(joinedDF['avg(FGM)'].isNotNull() & joinedDF['salary'].isNotNull())
    # from pyspark.sql.types import DoubleType
    # joinedDF = joinedDF.withColumn("age",col("age").cast(DoubleType()))
    w = Window().partitionBy('PLAYER_NAME')
    joinedDF2 = joinedDF.withColumn('age', when(col('age').isNull(), avg(col('age')).over(w)).otherwise(col('age')))
    joinedDF2 = joinedDF2.withColumn('player_height',
                                     when(col('player_height').isNull(), avg(col('player_height')).over(w)).otherwise(
                                         col('player_height')))
    joinedDF2 = joinedDF2.withColumn('player_weight',
                                     when(col('player_weight').isNull(), avg(col('player_weight')).over(w)).otherwise(
                                         col('player_weight')))
    joinedDF2 = joinedDF2.na.fill(value=0, subset=["injuries"])
    joinedDF2.coalesce(1).write.option("header", "true").csv(output, mode='overwrite')


if __name__ == '__main__':
    salary_path = sys.argv[1]
    salary_player_path = sys.argv[2]
    player_summary_path = sys.argv[3]
    player_info_path = sys.argv[4]
    injury_path = sys.argv[5]
    output = sys.argv[6]
    spark = SparkSession.builder.appName('NBA ETL process').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(salary_path, salary_player_path, player_summary_path, player_info_path, injury_path, output)

