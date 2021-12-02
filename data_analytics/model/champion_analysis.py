import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+

from pyspark.sql import SparkSession, functions, types

from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler, SQLTransformer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

import matplotlib.pyplot as plt


def champion_team(year, name):
    if (year == '2010' and name == 'Dallas') \
            or (year == '2011' and name == 'Miami') \
            or (year == '2012' and name == 'Miami') \
            or (year == '2013' and name == 'San Antonio') \
            or (year == '2014' and name == 'Golden State') \
            or (year == '2015' and name == 'Cleveland') \
            or (year == '2016' and name == 'Golden State') \
            or (year == '2017' and name == 'Golden State') \
            or (year == '2018' and name == 'Toronto') \
            or (year == '2019' and name == 'L.A. Lakers') \
            or (year == '2020' and name == 'Milwaukee'):
        return 'yes'
    else:
        return 'no'


def main(team_summary_path, team_rank_path, model_file):
    team_summary = spark.read.option("delimiter", ",").option("header", "true").csv(team_summary_path)
    team_summary = team_summary.withColumn('year', team_summary['year'].cast(types.StringType()))
    team_rank = spark.read.option("delimiter", ",").option("header", "true").csv(team_rank_path)
    team_rank = team_rank.withColumn('year', team_rank['year'].cast(types.StringType()))
    team_rank = team_rank.withColumnRenamed('TEAM_ID', 'dup_TEAM_ID') \
                            .withColumnRenamed('year', 'dup_year')
    team = team_summary.join(functions.broadcast(team_rank),
                             (team_summary.TEAM_ID == team_rank.dup_TEAM_ID)
                                          & (team_summary.year == team_rank.dup_year)) \
                        .drop('dup_TEAM_ID', 'dup_year','STANDINGSDATE', 'RETURNTOPLAY')
    team = team.dropna()
    set_champion = functions.udf(champion_team, types.StringType())
    team = team.withColumn('champion', set_champion(team.year, team.TEAM))
    team = team.withColumn('avg_PTS_home', team['avg_PTS_home'].cast(types.FloatType())) \
               .withColumn('avg_REB_home', team['avg_REB_home'].cast(types.FloatType())) \
               .withColumn('avg_AST_home', team['avg_AST_home'].cast(types.FloatType())) \
               .withColumn('avg_PTS_away', team['avg_PTS_away'].cast(types.FloatType())) \
               .withColumn('avg_REB_away', team['avg_REB_away'].cast(types.FloatType())) \
               .withColumn('avg_AST_away', team['avg_AST_away'].cast(types.FloatType())) \
               .withColumn('W', team['W'].cast(types.FloatType())) \
               .withColumn('W_PCT', team['W_PCT'].cast(types.FloatType())) \
               .withColumn('year', team['year'].cast(types.FloatType()))
    # display champion
    champion = team.where(team.champion == 'yes')
    champion.sort('year').show()
    team = team.select('avg_PTS_home', 'avg_REB_home', 'avg_AST_home', 'avg_PTS_away', 'avg_REB_away', \
                       'avg_AST_away', 'W', 'W_PCT', 'year', 'champion')
    train, validation = team.randomSplit([0.75, 0.25])
    train = train.cache()
    validation = validation.cache()
    assembler = VectorAssembler(
        inputCols=['avg_PTS_home', 'avg_REB_home', 'avg_AST_home', 'avg_PTS_away', 'avg_REB_away', 'avg_AST_away', 'W', 'W_PCT'],
        outputCol='features', handleInvalid="skip")
    indexer = StringIndexer(inputCol='champion', outputCol='label')
    classifier = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=10)
    pipeline = Pipeline(stages=[assembler, indexer, classifier])
    model = pipeline.fit(train)
    predictions = model.transform(validation)
    evaluator = MulticlassClassificationEvaluator(predictionCol="prediction", labelCol="label")
    score = evaluator.evaluate(predictions)
    print('Validation score for model: %g' % (score,))
    feature_list = ['avg_PTS_home', 'avg_REB_home', 'avg_AST_home', 'avg_PTS_away', 'avg_REB_away', 'avg_AST_away', 'W', 'W_PCT']
    importances = model.stages[-1].featureImportances
    x_values = list(range(len(importances)))
    plt.figure()
    plt.bar(x_values, importances, orientation='vertical')
    plt.xticks(x_values, feature_list, rotation='vertical', fontsize = 4.5)
    plt.ylabel('Importance')
    plt.xlabel('Feature')
    plt.title('Champion Feature Importances')
    plt.savefig('champion.png')


if __name__ == '__main__':
    team_summary = sys.argv[1]
    team_rank = sys.argv[2]
    model_file = sys.argv[3]
    spark = SparkSession.builder.appName('champion analysis').getOrCreate()
    spark.sparkContext.setLogLevel('WARN')
    assert spark.version >= '2.4'  # make sure we have Spark 2.4+
    main(team_summary, team_rank, model_file)
