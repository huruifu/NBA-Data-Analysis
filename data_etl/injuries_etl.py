from pyspark.sql import SparkSession, functions, types
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
    elif injury_name is None:
        return None
    return injury_name.strip()


def main(inputs, outputs):
    # main logic starts here
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
                .load(inputs)
                .repartition(8))
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
    acquired = (injuries
                .where(~functions.col("Acquired").isNull())
                .where(~functions.col("Date").isNull())
                .where(~functions.col("Team").isNull())
                .where(~functions.col("Notes").isNull()))
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
                    .drop(functions.col("Notes"))
                    .where((functions.col("injury_name") != "placed on IL") & (functions.col("injury_name") != "fined $50,000 by NBA for using inappropriate language during game"))
                    .withColumn("injury_name", format_injury_name(functions.col("injury_name")))
                    .withColumn("year", functions.year(functions.col("Date")))
                    .withColumn("month", functions.month(functions.col("Date")))
                    # 2019 season is a special season
                    .withColumn("played_season",
                                functions.when(functions.col("year")
                                               == 2020, functions.col("year") - 1)
                                .when(functions.col("month") >= 10, functions.col("year"))
                                .otherwise(functions.col("year") - 1)))

    relinquished.cache()
    relinquished.show()
    relinquished.coalesce(1).write.option(
        "header", "true").csv(outputs, mode='overwrite')


if __name__ == '__main__':
    inputs = sys.argv[1]
    outputs = sys.argv[2]
    spark = SparkSession.builder.appName('get clean injury data').getOrCreate()
    assert spark.version >= '3.0'  # make sure we have Spark 3.0+
    spark.sparkContext.setLogLevel('WARN')
    sc = spark.sparkContext
    main(inputs, outputs)
