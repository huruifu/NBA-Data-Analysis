import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+

from pyspark.sql import SparkSession, functions, types

from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler, SQLTransformer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql.window import Window
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import numpy as np


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


def main(team_summary_path, team_rank_path):
    team_summary = spark.read.option("delimiter", ",").option("header", "true").csv(team_summary_path)
    team_summary = team_summary.withColumn('year', team_summary['year'].cast(types.StringType())).cache()
    team_rank = spark.read.option("delimiter", ",").option("header", "true").csv(team_rank_path)
    team_rank = team_rank.withColumn('year', team_rank['year'].cast(types.StringType()))
    team_rank = team_rank.withColumnRenamed('TEAM_ID', 'dup_TEAM_ID') \
                            .withColumnRenamed('year', 'dup_year').cache()
    set_champion = functions.udf(champion_team, types.StringType())
    team = team_summary.join(functions.broadcast(team_rank),
                             (team_summary.TEAM_ID == team_rank.dup_TEAM_ID)
                                          & (team_summary.year == team_rank.dup_year)) \
                        .drop('dup_TEAM_ID', 'dup_year','STANDINGSDATE', 'RETURNTOPLAY')
    team = team.dropna()
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

    # draw correlation graph
    team = team.select('avg_PTS_home', 'avg_REB_home', 'avg_AST_home', 'avg_PTS_away', 'avg_REB_away',
                       'avg_AST_away', 'W', 'W_PCT', 'year', 'champion')
    f, ax = plt.subplots(figsize=(8, 6))
    teampdf = team.toPandas()
    corr = teampdf.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), annot=True,
                cmap=sns.diverging_palette(220, 10, as_cmap=True),
                square=True, ax=ax)
    plt.savefig('correlation.png')
    # plt.show()

    # building model
    train, validation = team.randomSplit([0.75, 0.25])
    train = train.cache()
    validation = validation.cache()
    assembler = VectorAssembler(
        inputCols=['avg_PTS_home', 'avg_REB_home', 'avg_AST_home', 'avg_PTS_away',
                   'avg_REB_away', 'avg_AST_away', 'W_PCT'],
        outputCol='features', handleInvalid="skip")
    indexer = StringIndexer(inputCol='champion', outputCol='label')
    classifier = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=10)
    pipeline = Pipeline(stages=[assembler, indexer, classifier])
    model = pipeline.fit(train)
    predictions = model.transform(validation)
    evaluator = MulticlassClassificationEvaluator(predictionCol="prediction", labelCol="label")
    score = evaluator.evaluate(predictions)
    print('Validation score for model: %g' % (score,))
    feature_list = ['avg_PTS_home', 'avg_REB_home', 'avg_AST_home', 'avg_PTS_away',
                    'avg_REB_away', 'avg_AST_away', 'W_PCT']
    importances = model.stages[-1].featureImportances
    x_values = list(range(len(importances)))

    # draw feature importance graph
    plt.figure()
    plt.bar(x_values, importances, orientation='vertical')
    plt.xticks(x_values, feature_list, rotation='vertical', fontsize = 4.5)
    plt.ylabel('Importance')
    plt.xlabel('Feature')
    plt.title('Champion Feature Importances')
    plt.savefig('champion_feature.png')
    # plt.show()

    # draw feature importance graph in WordCloud
    frequency_table = {}
    for i in range(len(importances)):
        frequency_table[feature_list[i]] = int(importances[i] * 1000)
    wc = WordCloud(background_color='white',max_font_size=50, collocations=False)
    wc.generate_from_frequencies(frequency_table)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('champion_feature_WC.png')
    # plt.show()

    # draw rank and probability graph
    rank_champion = {}
    for i in range(8):
        k = str(1 + i)
        rank_champion[k] = 0

    for i in range(11):
        k = str(2010 + i)
        west = team_rank.where(team_rank.CONFERENCE == 'West')\
                        .where(team_rank.dup_year == k)
        w = Window().orderBy(functions.lit('A'))
        west = west.withColumn('rank', functions.row_number().over(w))

        east = team_rank.where(team_rank.CONFERENCE == 'East') \
                        .where(team_rank.dup_year == k)
        w = Window().orderBy(functions.lit('A'))
        east = east.withColumn('rank', functions.row_number().over(w))

        team_stats = west.union(east)
        team_stats = team_stats.withColumn('champion', set_champion(team_stats.dup_year, team_stats.TEAM))
        rk = team_stats.where(team_stats.champion == 'yes').select('rank').head()[0]
        rank_champion[str(rk)] += 1
    rk = []
    for i in range(8):
        k = str(1 + i)
        rk.append(rank_champion[k]/11)
    xlb = ['1','2','3','4','5','6','7','8']
    plt.bar(xlb, rk)
    plt.ylabel('Probability of winning championship')
    plt.xlabel('Regular Season Rank')
    plt.title('Probability plot of championship and regular season rankings')
    plt.savefig('rank_and_champion.png')
    # plt.show()


if __name__ == '__main__':
    team_summary = sys.argv[1]
    team_rank = sys.argv[2]
    spark = SparkSession.builder.appName('champion analysis').getOrCreate()
    spark.sparkContext.setLogLevel('WARN')
    assert spark.version >= '2.4'  # make sure we have Spark 2.4+
    main(team_summary, team_rank)
