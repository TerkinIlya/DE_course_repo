from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
        SparkSession.builder
        .appName("TTest_task_1")
        .getOrCreate()
        )

file_path = ("/home/ilya/github/"
             "DE_course_repo/python_projects/"
             "PySpark/data/weather_data.csv")

weather_df = spark.read.csv(file_path,
                            header=True,
                            inferSchema=True)


# weather_df = weather_df.withColumn("date", to_date("date", "yyyy-MM-dd"))

# weather_df = weather_df.na.fill()

weather_temp = weather_df.select(F.mean("temperature")).first()[0]
weather_df = weather_df.fillna(weather_temp)

weather_df.show(10)
weather_df.printSchema()

hotest_d = weather_df.orderBy(F.desc("temperature")).limit(5)
hotest_d.select("date", "temperature").show()

weather_df = weather_df.withColumn("year", F.year("date"))

max_year = weather_df.agg(F.max("year")).first()[0]


max_prec = (weather_df.filter(weather_df["year"] == max_year)
            .groupBy("station_id")
            .agg(F.sum("precipitation").alias("total_precipitation")))
max_prec = max_prec.orderBy(F.desc("total_precipitation")).limit(1)
max_prec.select("station_id", "total_precipitation").show()

spark.stop()
