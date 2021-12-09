import sys
assert sys.version_info >= (3, 5) # make sure we have Python 3.5+

from pyspark.sql import SparkSession, functions, types

from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler, SQLTransformer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
<<<<<<< HEAD

import matplotlib.pyplot as plt
=======
import matplotlib.pyplot as plt
from wordcloud import WordCloud
>>>>>>> d193685cc08bb9ef2bd73ccfd02fd4dc5a550186


def all_nba_team(year, name):
    if (year == '2010' and name == 'Kevin Durant') \
            or (year == '2010' and name == 'LeBron James') \
            or (year == '2010' and name == 'Dwight Howard') \
            or (year == '2010' and name == 'Kobe Bryant') \
            or (year == '2010' and name == 'Derrick Rose') \
            or (year == '2011' and name == 'LeBron James') \
            or (year == '2011' and name == 'Kevin Durant') \
            or (year == '2011' and name == 'Dwight Howard') \
            or (year == '2011' and name == 'Kobe Byrant') \
            or (year == '2011' and name == 'Chris Paul') \
            or (year == '2012' and name == 'LeBron James') \
            or (year == '2012' and name == 'Kevin Durant') \
            or (year == '2012' and name == 'Tim Duncan') \
            or (year == '2012' and name == 'Kobe Byrant') \
            or (year == '2012' and name == 'Chris Paul') \
            or (year == '2013' and name == 'Kevin Durant') \
            or (year == '2013' and name == 'LeBron James') \
            or (year == '2013' and name == 'Joakim Noah') \
            or (year == '2013' and name == 'James Harden') \
            or (year == '2013' and name == 'Chris Paul') \
            or (year == '2014' and name == 'LeBron James') \
            or (year == '2014' and name == 'Anthony Davis') \
            or (year == '2014' and name == 'Marc Gasol') \
            or (year == '2014' and name == 'James Harden') \
            or (year == '2014' and name == 'Stephen Curry') \
            or (year == '2015' and name == 'Kawhi Lenoard') \
            or (year == '2015' and name == 'LeBron James') \
            or (year == '2015' and name == 'DeAndre Jordan') \
            or (year == '2015' and name == 'Stephen Curry') \
            or (year == '2015' and name == 'Russell Westbrook') \
            or (year == '2016' and name == 'Kawhi Lenoard') \
            or (year == '2016' and name == 'LeBron James ') \
            or (year == '2016' and name == 'Anthony Davis') \
            or (year == '2016' and name == 'James Harden') \
            or (year == '2016' and name == 'Russell Westbrook') \
            or (year == '2017' and name == 'Kevin Durant') \
            or (year == '2017' and name == 'LeBron James') \
            or (year == '2017' and name == 'Anthony Davis') \
            or (year == '2017' and name == 'James Harden') \
            or (year == '2017' and name == 'Damian Lillard') \
            or (year == '2018' and name == 'Giannis Antetokounmpo') \
            or (year == '2018' and name == 'Paul George') \
            or (year == '2018' and name == 'Nikola Jokic') \
            or (year == '2018' and name == 'James Harden') \
            or (year == '2018' and name == 'Stephen Curry') \
            or (year == '2019' and name == 'LeBron James') \
            or (year == '2019' and name == 'Giannis Antetokounmpo') \
            or (year == '2019' and name == 'Anthony Davis') \
            or (year == '2019' and name == 'James Harden') \
            or (year == '2019' and name == 'Luka Doncic') \
            or (year == '2020' and name == 'Giannis Antetokounmpo') \
            or (year == '2020' and name == 'Kawhi Leonard') \
            or (year == '2020' and name == 'Nikola Jokic') \
            or (year == '2020' and name == 'Stephen Curry') \
            or (year == '2020' and name == 'Luka Doncic'):
                return '1'
    elif (year == '2010' and name == 'Pau Gasol') \
            or (year == '2010' and name == 'Dirk Nowizki') \
            or (year == '2010' and name == 'Amar\'s Stoudemire') \
            or (year == '2010' and name == 'Dwyane Wade') \
            or (year == '2010' and name == 'Russell Westbrook') \
            or (year == '2011' and name == 'Kevin Love') \
            or (year == '2011' and name == 'Blake Griffin') \
            or (year == '2011' and name == 'Andrew Bynum') \
            or (year == '2011' and name == 'Tony Parker') \
            or (year == '2011' and name == 'Russell Westbrook') \
            or (year == '2012' and name == 'Carmelo Anthony') \
            or (year == '2012' and name == 'Blake Griffin') \
            or (year == '2012' and name == 'Marc Gasol') \
            or (year == '2012' and name == 'Tony Parker') \
            or (year == '2012' and name == 'Russell Westbrook') \
            or (year == '2013' and name == 'Blake Griffin') \
            or (year == '2013' and name == 'Kevin Love') \
            or (year == '2013' and name == 'Dwight Howard') \
            or (year == '2013' and name == 'Stephen Curry') \
            or (year == '2013' and name == 'Tony Parker') \
            or (year == '2014' and name == 'LaMarcus Aldridge') \
            or (year == '2014' and name == 'Pau Gasol') \
            or (year == '2014' and name == 'DeMarcus Cousins') \
            or (year == '2014' and name == 'Russell Westbrook') \
            or (year == '2014' and name == 'Chris Paul') \
            or (year == '2015' and name == 'Kevin Durant') \
            or (year == '2015' and name == 'Draymond Green') \
            or (year == '2015' and name == 'DeMarcus Cousins') \
            or (year == '2015' and name == 'Damian Lillard') \
            or (year == '2015' and name == 'Chris Paul') \
            or (year == '2016' and name == 'Kevin Durant') \
            or (year == '2016' and name == 'Giannis Antetokounmpo') \
            or (year == '2016' and name == 'Rudy Gobert') \
            or (year == '2016' and name == 'Stephen Curry') \
            or (year == '2016' and name == 'Isaiah Thomas') \
            or (year == '2017' and name == 'LaMarcus Aldridge') \
            or (year == '2017' and name == 'Giannis Antetokounmpo') \
            or (year == '2017' and name == 'Joel Embiid') \
            or (year == '2017' and name == 'DeMar DeRozan') \
            or (year == '2017' and name == 'Russell Westbrook') \
            or (year == '2018' and name == 'Kevin Durant') \
            or (year == '2018' and name == 'Kawhi Leonard') \
            or (year == '2018' and name == 'Joel Embiid') \
            or (year == '2018' and name == 'Damian Lillard') \
            or (year == '2018' and name == 'Kyrie Irving') \
            or (year == '2019' and name == 'Kawhi Leonard') \
            or (year == '2019' and name == 'Pascal Siakam') \
            or (year == '2019' and name == 'Nikola Jokic') \
            or (year == '2019' and name == 'Damian Lillard') \
            or (year == '2019' and name == 'Chris Paul') \
            or (year == '2020' and name == 'LeBron James') \
            or (year == '2020' and name == 'Julius Randle') \
            or (year == '2020' and name == 'Joel Embiid') \
            or (year == '2020' and name == 'Damian Lillard') \
            or (year == '2020' and name == 'Chris Paul'):
        return '2'
    elif (year == '2010' and name == 'LaMarcus Aldridge') \
            or (year == '2010' and name == 'Zach Randolph') \
            or (year == '2010' and name == 'AI Horford') \
            or (year == '2010' and name == 'Manu Ginobili') \
            or (year == '2010' and name == 'Chris Paul') \
            or (year == '2011' and name == 'Carmelo Anthony') \
            or (year == '2011' and name == 'Dirk Nowitzki') \
            or (year == '2011' and name == 'Tyson Chandler') \
            or (year == '2011' and name == 'Dwyane Wade') \
            or (year == '2011' and name == 'Rajon Rondo') \
            or (year == '2012' and name == 'David Lee') \
            or (year == '2012' and name == 'Paul George') \
            or (year == '2012' and name == 'Dwight Howard') \
            or (year == '2012' and name == 'Dwyane Wade') \
            or (year == '2012' and name == 'James Harden') \
            or (year == '2013' and name == 'Paul George') \
            or (year == '2013' and name == 'LaMarcus Aldridge') \
            or (year == '2013' and name == 'AI Jefferson') \
            or (year == '2013' and name == 'Goran Dragic') \
            or (year == '2013' and name == 'Damian Lillard') \
            or (year == '2014' and name == 'Blake Griffin') \
            or (year == '2014' and name == 'Tim Duncan') \
            or (year == '2014' and name == 'DeAndre Jordan') \
            or (year == '2014' and name == 'Klay Thompson') \
            or (year == '2014' and name == 'Kyrie Irving') \
            or (year == '2015' and name == 'Paul George') \
            or (year == '2015' and name == 'LaMarcus Aldridge') \
            or (year == '2015' and name == 'Andre Drummond') \
            or (year == '2015' and name == 'Klay Thompson') \
            or (year == '2015' and name == 'Kyle Lowry') \
            or (year == '2016' and name == 'Jimmy Butler') \
            or (year == '2016' and name == 'Draymond Green') \
            or (year == '2016' and name == 'DeAndre Jordan') \
            or (year == '2016' and name == 'John Wall') \
            or (year == '2016' and name == 'DemMar DeRozan') \
            or (year == '2017' and name == 'Jimmy Butler') \
            or (year == '2017' and name == 'Paul George') \
            or (year == '2017' and name == 'Karl-Anthony Towns') \
            or (year == '2017' and name == 'Victor Oladipo') \
            or (year == '2017' and name == 'Stephen Curry') \
            or (year == '2018' and name == 'Blake Griffin') \
            or (year == '2018' and name == 'LeBron James') \
            or (year == '2018' and name == 'Rudy Gobert') \
            or (year == '2018' and name == 'Russell Westbrook') \
            or (year == '2018' and name == 'Kebma Walker') \
            or (year == '2019' and name == 'Jimmy Butler') \
            or (year == '2019' and name == 'Jayson Tatum') \
            or (year == '2019' and name == 'Rudy Gobert') \
            or (year == '2019' and name == 'Ben Simmons') \
            or (year == '2019' and name == 'Russell Westbrook') \
            or (year == '2020' and name == 'Jimmy Butler') \
            or (year == '2020' and name == 'Paul George') \
            or (year == '2020' and name == 'Rudy Gobert') \
            or (year == '2020' and name == 'Bradley Beal') \
            or (year == '2020' and name == 'Kyrie Irving'):
        return '3'
    else:
        return '4'


<<<<<<< HEAD
def main(player_summary_path, player_info_path, team_summary_path, team_rank_path, model_file):
    player_summary = spark.read.option("delimiter", ",").option("header", "true").csv(player_summary_path)
    player_summary = player_summary.withColumn('year', player_summary['year'].cast(types.StringType()))
    player_info = spark.read.option("header", "true").csv(player_info_path)
    team_summary = spark.read.option("delimiter", ",").option("header", "true").csv(team_summary_path)
    team_summary = team_summary.withColumn('year', team_summary['year'].cast(types.StringType()))
    team_rank = spark.read.option("delimiter", ",").option("header", "true").csv(team_rank_path)
    team_rank = team_rank.withColumn('year', team_rank['year'].cast(types.StringType()))
    player_info = player_info.withColumnRenamed('PLAYER_ID', 'dup_PLAYER_ID') \
        .withColumnRenamed('player_name', 'dup_PLAYER_NAME')
=======
def main(player_summary_path, player_info_path, team_summary_path, team_rank_path):
    player_summary = spark.read.option("delimiter", ",").option("header", "true").csv(player_summary_path)
    player_summary = player_summary.withColumn('year', player_summary['year'].cast(types.StringType())).cache()
    player_info = spark.read.option("header", "true").csv(player_info_path).cache()
    team_summary = spark.read.option("delimiter", ",").option("header", "true").csv(team_summary_path)
    team_summary = team_summary.withColumn('year', team_summary['year'].cast(types.StringType())).cache()
    team_rank = spark.read.option("delimiter", ",").option("header", "true").csv(team_rank_path)
    team_rank = team_rank.withColumn('year', team_rank['year'].cast(types.StringType())).cache()
    player_info = player_info.withColumnRenamed('PLAYER_ID', 'dup_PLAYER_ID') \
                  .withColumnRenamed('player_name', 'dup_PLAYER_NAME')
>>>>>>> d193685cc08bb9ef2bd73ccfd02fd4dc5a550186
    player_stats = player_summary.join(functions.broadcast(player_info),
                                       (player_info.dup_PLAYER_NAME == player_summary.PLAYER_NAME)
                                       & (player_info.season == player_summary.year)) \
        .drop('dup_PLAYER_NAME', 'dup_PLAYER_ID', 'season')
    team_summary = team_summary.withColumnRenamed('TEAM_ID', 'dup_TEAM_ID') \
        .withColumnRenamed('year', 'dup_year')
    player_team_stats = player_stats.join(functions.broadcast(team_summary),
                                          (player_stats.TEAM_ID == team_summary.dup_TEAM_ID)
                                          & (player_stats.year == team_summary.dup_year)) \
        .drop('dup_TEAM_ID', 'dup_year')
    team_rank = team_rank.withColumnRenamed('TEAM_ID', 'dup_TEAM_ID') \
        .withColumnRenamed('year', 'dup_year')
    player = player_team_stats.join(functions.broadcast(team_rank),
                                    (player_team_stats.TEAM_ID == team_rank.dup_TEAM_ID)
                                    & (player_team_stats.year == team_rank.dup_year)) \
        .drop('dup_TEAM_ID', 'STANDINGSDATE', 'G', 'L', 'RETURNTOPLAY', 'dup_year')
    player = player.dropna()
    set_all_nba_team = functions.udf(all_nba_team, types.StringType())
    player = player.withColumn('all_nba_team', set_all_nba_team(player.year, player.PLAYER_NAME))
    player = player.withColumn('avg(FGM)', player['avg(FGM)'].cast(types.FloatType())) \
        .withColumn('avg(FGA)', player['avg(FGA)'].cast(types.FloatType())) \
        .withColumn('avg(FG3M)', player['avg(FG3M)'].cast(types.FloatType())) \
        .withColumn('avg(FG3A)', player['avg(FG3A)'].cast(types.FloatType())) \
        .withColumn('avg(FTM)', player['avg(FTM)'].cast(types.FloatType())) \
        .withColumn('avg(FTA)', player['avg(FTA)'].cast(types.FloatType())) \
        .withColumn('avg(OREB)', player['avg(OREB)'].cast(types.FloatType())) \
        .withColumn('avg(DREB)', player['avg(DREB)'].cast(types.FloatType())) \
        .withColumn('avg(REB)', player['avg(REB)'].cast(types.FloatType())) \
        .withColumn('avg(AST)', player['avg(AST)'].cast(types.FloatType())) \
        .withColumn('avg(STL)', player['avg(STL)'].cast(types.FloatType())) \
        .withColumn('avg(BLK)', player['avg(BLK)'].cast(types.FloatType())) \
        .withColumn('avg(TO)', player['avg(TO)'].cast(types.FloatType())) \
        .withColumn('avg(PF)', player['avg(PF)'].cast(types.FloatType())) \
        .withColumn('avg(PTS)', player['avg(PTS)'].cast(types.FloatType())) \
        .withColumn('avg(PLUS_MINUS)', player['avg(PLUS_MINUS)'].cast(types.FloatType())) \
        .withColumn('sum(FGM)', player['sum(FGM)'].cast(types.FloatType())) \
        .withColumn('sum(FGA)', player['sum(FGA)'].cast(types.FloatType())) \
        .withColumn('sum(FG3M)', player['sum(FG3M)'].cast(types.FloatType())) \
        .withColumn('sum(FG3A)', player['sum(FG3A)'].cast(types.FloatType())) \
        .withColumn('sum(FTM)', player['sum(FTM)'].cast(types.FloatType())) \
        .withColumn('sum(FTA)', player['sum(FTA)'].cast(types.FloatType())) \
        .withColumn('sum(OREB)', player['sum(OREB)'].cast(types.FloatType())) \
        .withColumn('sum(DREB)', player['sum(DREB)'].cast(types.FloatType())) \
        .withColumn('sum(REB)', player['sum(REB)'].cast(types.FloatType())) \
        .withColumn('sum(AST)', player['sum(AST)'].cast(types.FloatType())) \
        .withColumn('sum(STL)', player['sum(STL)'].cast(types.FloatType())) \
        .withColumn('sum(BLK)', player['sum(BLK)'].cast(types.FloatType())) \
        .withColumn('sum(TO)', player['sum(TO)'].cast(types.FloatType())) \
        .withColumn('sum(PF)', player['sum(PF)'].cast(types.FloatType())) \
        .withColumn('sum(PTS)', player['sum(PTS)'].cast(types.FloatType())) \
        .withColumn('sum(PLUS_MINUS)', player['sum(PLUS_MINUS)'].cast(types.FloatType())) \
        .withColumn('sum(ifminute)', player['sum(ifminute)'].cast(types.FloatType())) \
        .withColumn('avg(seconds)', player['avg(seconds)'].cast(types.FloatType())) \
        .withColumn('sum(seconds)', player['sum(seconds)'].cast(types.FloatType())) \
        .withColumn('age', player['age'].cast(types.FloatType())) \
        .withColumn('player_height', player['player_height'].cast(types.FloatType())) \
        .withColumn('player_weight', player['player_weight'].cast(types.FloatType())) \
        .withColumn('draft_year', player['draft_year'].cast(types.FloatType())) \
        .withColumn('draft_round', player['draft_round'].cast(types.FloatType())) \
        .withColumn('draft_number', player['draft_number'].cast(types.FloatType())) \
        .withColumn('avg_PTS_home', player['avg_PTS_home'].cast(types.FloatType())) \
        .withColumn('avg_REB_home', player['avg_REB_home'].cast(types.FloatType())) \
        .withColumn('avg_AST_home', player['avg_AST_home'].cast(types.FloatType())) \
        .withColumn('avg_PTS_away', player['avg_PTS_away'].cast(types.FloatType())) \
        .withColumn('avg_REB_away', player['avg_REB_away'].cast(types.FloatType())) \
        .withColumn('avg_AST_away', player['avg_AST_away'].cast(types.FloatType())) \
        .withColumn('W', player['W'].cast(types.FloatType())) \
        .withColumn('W_PCT', player['W_PCT'].cast(types.FloatType())) \
        .withColumn('year', player['year'].cast(types.FloatType()))
<<<<<<< HEAD
    player = player.select('avg(FGM)', 'avg(FGA)', 'avg(FG3M)', 'avg(FG3A)', 'avg(FTM)', 'avg(FTA)', 'avg(OREB)', \
                           'avg(DREB)', 'avg(REB)', 'avg(AST)', 'avg(STL)', 'avg(BLK)', 'avg(TO)', 'avg(PF)',
                           'avg(PTS)', \
                           'avg(PLUS_MINUS)', 'sum(FGM)', 'sum(FGA)', 'sum(FG3M)', 'sum(FG3A)', 'sum(FTM)', 'sum(FTA)', \
                           'sum(OREB)', 'sum(DREB)', 'sum(REB)', 'sum(AST)', 'sum(STL)', 'sum(BLK)', 'sum(TO)',
                           'sum(PF)', \
                           'sum(PTS)', 'sum(PLUS_MINUS)', 'sum(ifminute)', 'avg(seconds)', 'sum(seconds)', 'year',
                           'age', \
                           'player_height', 'player_weight', 'draft_year', 'draft_round', 'draft_number',
                           'avg_PTS_home', \
                           'avg_REB_home', 'avg_AST_home', 'avg_PTS_away', 'avg_REB_away', 'avg_AST_away', 'W', 'W_PCT',
                           'all_nba_team')
=======
    player = player.select('avg(FGM)', 'avg(FGA)', 'avg(FG3M)', 'avg(FG3A)', 'avg(FTM)', 'avg(FTA)', 'avg(OREB)',
                           'avg(DREB)', 'avg(REB)', 'avg(AST)', 'avg(STL)', 'avg(BLK)', 'avg(TO)', 'avg(PF)',
                           'avg(PTS)',
                           'avg(PLUS_MINUS)', 'sum(FGM)', 'sum(FGA)', 'sum(FG3M)', 'sum(FG3A)', 'sum(FTM)', 'sum(FTA)',
                           'sum(OREB)', 'sum(DREB)', 'sum(REB)', 'sum(AST)', 'sum(STL)', 'sum(BLK)', 'sum(TO)',
                           'sum(PF)',
                           'sum(PTS)', 'sum(PLUS_MINUS)', 'sum(ifminute)', 'avg(seconds)', 'sum(seconds)', 'year',
                           'age', \
                           'player_height', 'player_weight', 'draft_year', 'draft_round', 'draft_number',
                           'avg_PTS_home',
                           'avg_REB_home', 'avg_AST_home', 'avg_PTS_away', 'avg_REB_away', 'avg_AST_away', 'W', 'W_PCT',
                           'all_nba_team')

>>>>>>> d193685cc08bb9ef2bd73ccfd02fd4dc5a550186
    train, validation = player.randomSplit([0.75, 0.25])
    train = train.cache()
    validation = validation.cache()
    assembler = VectorAssembler(
<<<<<<< HEAD
        inputCols=['avg(FGM)', 'avg(FGA)', 'avg(FG3M)', 'avg(FG3A)', 'avg(FTM)', 'avg(FTA)', 'avg(OREB)', \
                   'avg(DREB)', 'avg(REB)', 'avg(AST)', 'avg(STL)', 'avg(BLK)', 'avg(TO)', 'avg(PF)', 'avg(PTS)', \
                   'avg(PLUS_MINUS)', 'sum(FGM)', 'sum(FGA)', 'sum(FG3M)', 'sum(FG3A)', 'sum(FTM)', 'sum(FTA)', \
                   'sum(OREB)', 'sum(DREB)', 'sum(REB)', 'sum(AST)', 'sum(STL)', 'sum(BLK)', 'sum(TO)', 'sum(PF)', \
                   'sum(PTS)', 'sum(PLUS_MINUS)', 'sum(ifminute)', 'avg(seconds)', 'sum(seconds)', 'year', 'age', \
                   'player_height', 'player_weight', 'draft_year', 'draft_round', 'draft_number', 'avg_PTS_home', \
=======
        inputCols=['avg(FGM)', 'avg(FGA)', 'avg(FG3M)', 'avg(FG3A)', 'avg(FTM)', 'avg(FTA)', 'avg(OREB)',
                   'avg(DREB)', 'avg(REB)', 'avg(AST)', 'avg(STL)', 'avg(BLK)', 'avg(TO)', 'avg(PF)', 'avg(PTS)',
                   'avg(PLUS_MINUS)', 'sum(FGM)', 'sum(FGA)', 'sum(FG3M)', 'sum(FG3A)', 'sum(FTM)', 'sum(FTA)',
                   'sum(OREB)', 'sum(DREB)', 'sum(REB)', 'sum(AST)', 'sum(STL)', 'sum(BLK)', 'sum(TO)', 'sum(PF)',
                   'sum(PTS)', 'sum(PLUS_MINUS)', 'sum(ifminute)', 'avg(seconds)', 'sum(seconds)', 'year', 'age',
                   'player_height', 'player_weight', 'draft_year', 'draft_round', 'draft_number', 'avg_PTS_home',
>>>>>>> d193685cc08bb9ef2bd73ccfd02fd4dc5a550186
                   'avg_REB_home', 'avg_AST_home', 'avg_PTS_away', 'avg_REB_away', 'avg_AST_away', 'W', 'W_PCT'],
        outputCol='features', handleInvalid="skip")
    indexer = StringIndexer(inputCol='all_nba_team', outputCol='label')
    classifier = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=10)
    pipeline = Pipeline(stages=[assembler, indexer, classifier])
    model = pipeline.fit(train)
    predictions = model.transform(validation)
    evaluator = MulticlassClassificationEvaluator(predictionCol="prediction", labelCol="label")
    score = evaluator.evaluate(predictions)
    print('Validation score for model: %g' % (score,))
<<<<<<< HEAD
    feature_list = ['avg(FGM)', 'avg(FGA)', 'avg(FG3M)', 'avg(FG3A)', 'avg(FTM)', 'avg(FTA)', 'avg(OREB)', \
                   'avg(DREB)', 'avg(REB)', 'avg(AST)', 'avg(STL)', 'avg(BLK)', 'avg(TO)', 'avg(PF)', 'avg(PTS)', \
                   'avg(PLUS_MINUS)', 'sum(FGM)', 'sum(FGA)', 'sum(FG3M)', 'sum(FG3A)', 'sum(FTM)', 'sum(FTA)', \
                   'sum(OREB)', 'sum(DREB)', 'sum(REB)', 'sum(AST)', 'sum(STL)', 'sum(BLK)', 'sum(TO)', 'sum(PF)', \
                   'sum(PTS)', 'sum(PLUS_MINUS)', 'sum(ifminute)', 'avg(seconds)', 'sum(seconds)', 'year', 'age', \
                   'player_height', 'player_weight', 'draft_year', 'draft_round', 'draft_number', 'avg_PTS_home', \
                   'avg_REB_home', 'avg_AST_home', 'avg_PTS_away', 'avg_REB_away', 'avg_AST_away', 'W', 'W_PCT']
    importances = model.stages[-1].featureImportances
    x_values = list(range(len(importances)))
=======
    feature_list = ['avg(FGM)', 'avg(FGA)', 'avg(FG3M)', 'avg(FG3A)', 'avg(FTM)', 'avg(FTA)', 'avg(OREB)',
                   'avg(DREB)', 'avg(REB)', 'avg(AST)', 'avg(STL)', 'avg(BLK)', 'avg(TO)', 'avg(PF)', 'avg(PTS)',
                   'avg(PLUS_MINUS)', 'sum(FGM)', 'sum(FGA)', 'sum(FG3M)', 'sum(FG3A)', 'sum(FTM)', 'sum(FTA)',
                   'sum(OREB)', 'sum(DREB)', 'sum(REB)', 'sum(AST)', 'sum(STL)', 'sum(BLK)', 'sum(TO)', 'sum(PF)',
                   'sum(PTS)', 'sum(PLUS_MINUS)', 'sum(ifminute)', 'avg(seconds)', 'sum(seconds)', 'year', 'age',
                   'player_height', 'player_weight', 'draft_year', 'draft_round', 'draft_number', 'avg_PTS_home',
                   'avg_REB_home', 'avg_AST_home', 'avg_PTS_away', 'avg_REB_away', 'avg_AST_away', 'W', 'W_PCT']
    importances = model.stages[-1].featureImportances
    x_values = list(range(len(importances)))

    # draw feature importance graph
>>>>>>> d193685cc08bb9ef2bd73ccfd02fd4dc5a550186
    plt.figure()
    plt.bar(x_values, importances, orientation='vertical')
    plt.xticks(x_values, feature_list, rotation='vertical', fontsize=4.5)
    plt.ylabel('Importance')
    plt.xlabel('Feature')
    plt.title('All nba team Feature Importances')
<<<<<<< HEAD
    plt.savefig('allnba.png')
=======
    plt.savefig('allnba_feature.png')
    # plt.show()

    # draw feature importance graph in WordCloud
    frequency_table = {}
    for i in range(len(importances)):
        frequency_table[feature_list[i]] = int(importances[i] * 1000)
    wc = WordCloud(background_color='white',max_font_size=50, collocations=False)
    wc.generate_from_frequencies(frequency_table)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('allnba_feature_WC.png')
    # plt.show()
>>>>>>> d193685cc08bb9ef2bd73ccfd02fd4dc5a550186


if __name__ == '__main__':
    player_summary = sys.argv[1]
    player_info = sys.argv[2]
    team_summary = sys.argv[3]
    team_rank = sys.argv[4]
<<<<<<< HEAD
    model_file = sys.argv[5]
    spark = SparkSession.builder.appName('mvp').getOrCreate()
    spark.sparkContext.setLogLevel('WARN')
    assert spark.version >= '2.4'  # make sure we have Spark 2.4+
    main(player_summary, player_info, team_summary, team_rank, model_file)
=======
    spark = SparkSession.builder.appName('mvp').getOrCreate()
    spark.sparkContext.setLogLevel('WARN')
    assert spark.version >= '2.4'  # make sure we have Spark 2.4+
    main(player_summary, player_info, team_summary, team_rank)
>>>>>>> d193685cc08bb9ef2bd73ccfd02fd4dc5a550186
