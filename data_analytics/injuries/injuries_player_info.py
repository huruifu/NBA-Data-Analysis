from pyspark.sql import SparkSession, functions, types
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler, SQLTransformer
from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from plot_tools import plot_barhgraph
import sys
assert sys.version_info >= (3, 5)  # make sure we have Python 3.5+

# add more functions as necessary
@functions.udf(returnType=types.StringType())
def format_injury_name(injury_name):
    if "placed on IL with" in injury_name:
        injury_name = injury_name.replace("placed on IL with", "")
    elif "placed on IL for" in injury_name:
        injury_name = injury_name.replace("placed on IL for", "")
    elif "placed on IL recovering from" in injury_name:
        injury_name = injury_name.replace("placed on IL recovering from", "")
    elif "placed on IL recoverimg from" in injury_name:
        injury_name = injury_name.replace("placed on IL recoverimg from", "")
    elif "placed on IL frecovering from" in injury_name:
        injury_name = injury_name.replace("placed on IL frecovering from", "")
    return injury_name.strip()    


def main(injuries_inputs, player_info_inputs):
    # main logic starts here
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
                .withColumn("year", functions.year(functions.col("Date")))
                .withColumn("month", functions.month(functions.col("Date")))
                # 2019 season is a special season
                .withColumn("played_season", 
                            functions.when(functions.col("year") == 2020, functions.col("year") - 1)
                            .when(functions.col("month") >= 10, functions.col("year"))
                            .otherwise(functions.col("year") - 1)))
    # injuries.cache()
    # injuries.show()
    # print(injuries.count())
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
    player_injury = (injuries
                     .join(player_info,
                           (player_info["player_name"] == functions.regexp_replace(injuries["Relinquished"], r'\.', "")) & 
                           (player_info["season"] == injuries["played_season"]))
                     .select("player_name", "player_position", "Team", "age", "player_height", "player_weight", "season", "injury_name", "status"))
    # player_injury.cache()
    # player_injury.show()
    # print(player_injury.count())
    # player_injury.groupBy("player_position").agg(functions.count("*")).show()
    
    ##################################################################################
    # plot graphs
    ##################################################################################
    # most injury type in pf
    # pf = (player_injury
    #       .where(functions.col("player_position") == "PF")
    #       .groupBy(functions.col("injury_name"))
    #       .agg(functions.count("*").alias("n"))
    #       .orderBy(functions.col("n").desc()))
    # pf.cache()
    # pf.show()
    # plot_barhgraph(pf.head(40), "injury_name", "n", "most injury type in PF")
    
    # most injury type in f
    # f = (player_injury
    #       .where(functions.col("player_position") == "F")
    #       .groupBy(functions.col("injury_name"))
    #       .agg(functions.count("*").alias("n"))
    #       .orderBy(functions.col("n").desc()))
    # f.cache()
    # f.show()
    # plot_barhgraph(f.head(40), "injury_name", "n", "most injury type in F")
    
    # most injury type in pg
    # pg = (player_injury
    #       .where(functions.col("player_position") == "PG")
    #       .groupBy(functions.col("injury_name"))
    #       .agg(functions.count("*").alias("n"))
    #       .orderBy(functions.col("n").desc()))
    # pg.cache()
    # pg.show()
    # plot_barhgraph(pg.head(40), "injury_name", "n", "most injury type in PG")
    
    # most injury type in SF
    # sf = (player_injury
    #       .where(functions.col("player_position") == "SF")
    #       .groupBy(functions.col("injury_name"))
    #       .agg(functions.count("*").alias("n"))
    #       .orderBy(functions.col("n").desc()))
    # sf.cache()
    # sf.show()
    # plot_barhgraph(sf.head(40), "injury_name", "n", "most injury type in SF")
    
    # most injury type in SG
    # sg = (player_injury
    #       .where(functions.col("player_position") == "SG")
    #       .groupBy(functions.col("injury_name"))
    #       .agg(functions.count("*").alias("n"))
    #       .orderBy(functions.col("n").desc()))
    # sg.cache()
    # sg.show()
    # plot_barhgraph(sg.head(40), "injury_name", "n", "most injury type in SG")
    
    # most injury type in C
    # c = (player_injury
    #       .where(functions.col("player_position") == "C")
    #       .groupBy(functions.col("injury_name"))
    #       .agg(functions.count("*").alias("n"))
    #       .orderBy(functions.col("n").desc()))
    # c.cache()
    # c.show()
    # plot_barhgraph(c.head(40), "injury_name", "n", "most injury type in C")
    
    # most injury type in G
    # g = (player_injury
    #       .where(functions.col("player_position") == "G")
    #       .groupBy(functions.col("injury_name"))
    #       .agg(functions.count("*").alias("n"))
    #       .orderBy(functions.col("n").desc()))
    # g.cache()
    # g.show()
    # plot_barhgraph(g.head(40), "injury_name", "n", "most injury type in G")
    
    ##################################################################################
    # training model for predicting injury type
    # features: player_position, age, player_height, player_weight
    # label injury_name
    ##################################################################################
    player_injury = (player_injury
                     .where((functions.col("injury_name") != "placed on IL") & (functions.col("injury_name") != "fined $50,000 by NBA for using inappropriate language during game"))
                     .withColumn("injury_name", format_injury_name(functions.col("injury_name"))))
    
    print(player_injury.groupBy("injury_name").agg(functions.count("*")).count())
    #player_injury.groupBy("injury_name").agg(functions.count("*")).coalesce(1).write.option("header", "true").csv(output, mode='overwrite')
    
    # split data into train and validation part
    train, validation = player_injury.randomSplit([0.8, 0.2])
    train = train.cache()
    validation = validation.cache()
    
    # create a pipeline to predict injury
    injury_indexer = StringIndexer(inputCol="injury_name", outputCol="label", stringOrderType="frequencyDesc")
    position_indexer = StringIndexer(inputCol="player_position", outputCol="position")
    feature_assembler = VectorAssembler(inputCols=["position", "age", "player_height", "player_weight"],
                                        outputCol="features")
    classifier = MultilayerPerceptronClassifier(layers=[4, 30, 100, 500, 1000, 1500, 2000, 1537])
    pipeline = Pipeline(stages=[position_indexer, feature_assembler, injury_indexer, classifier])
    model = pipeline.fit(train)
    
    # training score
    trainDF = model.transform(train)
    evaluator = MulticlassClassificationEvaluator(predictionCol="prediction")
    train_score = evaluator.evaluate(trainDF)
    print('Training score for model: %g' % (train_score, )) 
    
    # validation score
    predDF = model.transform(validation)
    evaluator = MulticlassClassificationEvaluator(predictionCol="prediction")
    validation_score = evaluator.evaluate(predDF)
    print('Training score for model: %g' % (validation_score, )) 
    
    
    
if __name__ == '__main__':
    injuries_inputs = sys.argv[1]
    player_info_inputs = sys.argv[2]
    output = sys.argv[3]
    spark = SparkSession.builder.appName('example code').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(injuries_inputs, player_info_inputs)
