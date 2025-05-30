from pyspark.sql import SparkSession

# Настройка сессии Spark
spark = SparkSession.builder \
    .appName("MyApp") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Пример данных
data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
df = spark.createDataFrame(data, ["name", "id"])
df.show()
