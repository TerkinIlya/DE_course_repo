from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("Tungsten Example") \
    .config("spark.sql.codegen.wholeStage", "true") \
    .getOrCreate()

data = [(i, f"Name_{i % 5}", i % 3, i % 2) for i in range(1, 1000001)]
df = spark.createDataFrame(data, ["id", "name", "mod3", "mod2"])

# Применяем фильтр и агрегацию, чтобы увидеть работу Tungsten
result = df.filter(col("mod2") == 1) \
           .groupBy("mod3") \
           .agg({"id": "sum"}) \
           .orderBy("mod3")

result.explain()
