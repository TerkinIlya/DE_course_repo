from pyspark.sql import SparkSession
from dotenv import load_dotenv
from os import getenv

load_dotenv()

HOST = getenv('CH_HOST')
PORT = getenv('CH_PORT')

spark = (SparkSession.builder
         .appName("PySpark ClickHouse Connection")
         .config("spark.jars", "clickhouse-jdbc-0.4.6.jar")
         .getOrCreate()
         )

# Параметры подключения
url = f"jdbc:clickhouse://{HOST}:{PORT}/default"
properties = {
    "user": "default",  # Имя пользователя ClickHouse (по умолчанию "default")
    "password": "",     # Пароль (по умолчанию пустой)
    "driver": "com.clickhouse.jdbc.ClickHouseDriver"
}

df = spark.read.jdbc(url=url, table="employees", properties=properties)
df.show()

df.createOrReplaceTempView("employees_view")

spark.sql("SELECT name FROM employees_view").show()

data = [
    ("Alice", "Engineer", 75000, "2021-06-15"),
    ("Bob", "Manager", 90000, "2020-05-01"),
    ("Charlie", "HR", 60000, "2019-04-12"),
    ("Diana", "Sales", 50000, "2018-01-25")
]
columns = ["name", "position", "salary", "hire_date"]

df = spark.createDataFrame(data, columns)

df.write.jdbc(url=url,
              table="default.employees",
              mode="append",
              properties=properties)

print("Данные успешно записаны в таблицу employees")

spark.stop()
