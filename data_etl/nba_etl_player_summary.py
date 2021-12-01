# use command to run:
# ${SPARK_HOME}/bin/spark-submit data_analytics/nba_salary_analysis.py data/clean_data/salary_etl

import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+

from pyspark.sql import SparkSession, functions, types
from pyspark.sql.types import DateType
from pyspark.sql.functions import avg, sum, count, when

# add more functions as necessary

@functions.udf(returnType=types.DoubleType())
def to_sec(minute):
    sec_result = 0
    if (minute != None) & (len(str(minute).split(":")) == 2):
        mins, secs = str(minute).split(":")
        sec_result = float(mins) * 60 + float(secs)
    if (minute != None) & (len(str(minute).split(":")) == 1):
        sec_result = float(minute)
    return sec_result


def main(games_path, gmDetail_path, output1, output2):
    # main logic starts here

    # input should be a csv
    #games_path = "/Users/sarahhu/Desktop/SFUgrad/CMPT732/732Project/Project/732-project/data/nba/games.csv"
    games = spark.read.option("delimiter", ",").option("header", "true").csv(games_path)

    #gmDetail_path = "/Users/sarahhu/Desktop/SFUgrad/CMPT732/732Project/Project/732-project/data/nba/games_details.csv"
    gmDetail = spark.read.option("delimiter", ",").option("header", "true").csv(gmDetail_path)

    #games2 = games.withColumn('GAME_DATE',functions.to_date(games["GAME_DATE_EST"]))
    #games2 = games2.filter((games2['GAME_DATE']>="2010-01-01") & (games2['GAME_DATE']<"2021-01-01"))
    games2 = games.filter((games['SEASON'] >= "2010") & (games['SEASON'] < "2021"))

    gmDetail = gmDetail.withColumn("ifminute", when(gmDetail["MIN"].isNull(), 0).otherwise(1))
    gamesDate = games2.groupBy('SEASON', 'GAME_ID').count()
    #gmDetail2 = gmDetail.drop('FG_PCT', 'FG3_PCT', 'FT_PCT')
    gamesAvg = gamesDate.join(gmDetail,['GAME_ID'],'inner')

    gamesAvg = gamesAvg.withColumn("seconds", to_sec(gamesAvg['MIN']))

    gamesAvg2 = gamesAvg.groupBy('SEASON','TEAM_ID','PLAYER_ID', 'PLAYER_NAME').agg(avg('FGM'),avg('FGA'),\
                avg('FG3M'),avg('FG3A'),avg('FTM'),avg('FTA'),avg('OREB'),avg('DREB'),avg('REB'),avg('AST'),avg('STL'),avg('BLK'),\
                avg('TO'),avg('PF'),avg('PTS'),avg('PLUS_MINUS'),sum('FGM'),sum('FGA'),sum('FG3M'),sum('FG3A'),sum('FTM'),sum('FTA'),\
                sum('OREB'),sum('DREB'),sum('REB'),sum('AST'),sum('STL'),sum('BLK'),sum('TO'),sum('PF'),sum('PTS'),sum('PLUS_MINUS'),\
                sum('ifminute'), avg('seconds'), sum('seconds'))
    gamesAvg2 = gamesAvg2.withColumnRenamed("SEASON", "year")

    gamesAvg3 = gamesAvg.groupBy('SEASON', 'PLAYER_ID', 'PLAYER_NAME').agg(avg('FGM'), avg('FGA'), \
                avg('FG3M'), avg('FG3A'), avg('FTM'), avg('FTA'), avg('OREB'), avg('DREB'), avg('REB'), avg('AST'), avg('STL'),avg('BLK'), \
                avg('TO'), avg('PF'), avg('PTS'), avg('PLUS_MINUS'), sum('FGM'), sum('FGA'), sum('FG3M'), sum('FG3A'),sum('FTM'), sum('FTA'), \
                sum('OREB'), sum('DREB'), sum('REB'), sum('AST'), sum('STL'), sum('BLK'), sum('TO'), sum('PF'), sum('PTS'),sum('PLUS_MINUS'), \
                sum('ifminute'), avg('seconds'), sum('seconds'))
    gamesAvg3 = gamesAvg3.withColumnRenamed("SEASON", "year")

    gamesAvg2.write.partitionBy("year") \
        .mode("overwrite") \
        .option("header", "true").option("sep", ",") \
        .csv(output1)

    gamesAvg3.write.partitionBy("year") \
        .mode("overwrite") \
        .option("header", "true").option("sep", ",") \
        .csv(output2)

if __name__ == '__main__':
    games_path = sys.argv[1]
    gmDetail_path = sys.argv[2]
    output1 = sys.argv[3]
    output2 = sys.argv[4]
    spark = SparkSession.builder.appName('NBA ETL process').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(games_path, gmDetail_path, output1, output2)
