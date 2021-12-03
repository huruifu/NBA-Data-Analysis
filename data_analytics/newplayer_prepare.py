import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+

from pyspark.sql import SparkSession, functions, types
from pyspark.sql.functions import *
import numpy
spark = SparkSession.builder.appName('new player analyst').getOrCreate()
assert spark.version >= '2.3' # make sure we have Spark 2.3+
spark.sparkContext.setLogLevel('WARN')

from pyspark.ml import PipelineModel
from pyspark.ml.evaluation import RegressionEvaluator





def main(inputs1,input2, output):
    # inputs = spark.read.option("header","true").csv("c/file/YEAR=/CONFERENCE=")
    # inputs1 = '/mnt/c/Users/cathy/PycharmProjects/finalNBA/player_info.csv'
    data_player = spark.read.csv(inputs1,header='true')
    # find_null = data.filter(data.player_position.isNull())
    fill_null= data_player.na.fill(value="PF-F-PG-SF-C-SG-G", subset=["player_position"])
    # player_name == 'Nicole Melli' position =0
    fill_zero = fill_null.withColumn('player_position', regexp_replace('player_position', '0', 'PF-F-PG-SF-C-SG-G'))
    # split all possible position to be separate rows
    tmp_result = fill_zero.withColumn('player_position', explode(split('player_position', '-')))
    # fill_zero.select('player_position').distinct().show() : 7 outputs: PF;F;PG;SF;C;SG;G

    input2 = spark.read.option("delimiter", ",").option("header", "true").csv(input2)
       #  '/mnt/c/Users/cathy/Desktop/732/etl_player_summary_output')
    # inputs = spark.read.option("header","true").csv("c/file/YEAR=/CONFERENCE=")
    # input2='/mnt/c/Users/cathy/PycharmProjects/finalNBA/output_S/YEAR=.csv'
    input2 = input2.withColumnRenamed("PLAYER_ID", "P_ID")
    input2 = input2.withColumnRenamed("PLAYER_NAME","P_NAME")
    joinedDF = input2.join(tmp_result, (input2.P_ID == tmp_result.PLAYER_ID) & (input2.year == tmp_result.season))
    # joinedDF.printSchema()
    dropedDF = joinedDF.drop("P_ID", "P_NAME", "season")

    # dropedDF.coalesce(1).write.option("header", "true").csv('/mnt/c/Users/cathy/Desktop/732/output_tmp1', mode='overwrite')
    dropedDF.coalesce(1).write.option("header", "true").csv(output,mode='overwrite')

if __name__ == '__main__':
    player_basis_information = sys.argv[1]
    player_score_information = sys.argv[2]
    output = sys.argv[3]
    spark = SparkSession.builder.appName(
        'Player Information Join ').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(player_basis_information,player_score_information,output)
    # salary_df = salary_df.withColumn("name", functions.translate(functions.col("name"), ".", ""))
    # joinedDF =input2.join(tmp_result, ['PLAYER_ID', 'season'], 'left')



