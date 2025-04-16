from pyspark.sql import SparkSession
from dotenv import load_dotenv
from os import getenv

load_dotenv()

spark = (SparkSession.builder.appName("PySpark PostgreSQL Connection")
         .config("spark.jars", "postgresql-42.2.23.jar").getOrCreate())

DATABASE = getenv('PG_DATABASE')
USER = getenv('PG_USER')
PASSWORD = getenv('PG_PASSWORD')
HOST = getenv('PG_HOST')
PORT = getenv('PG_PORT')

url = f"jdbc:postgresql://{HOST}:{PORT}/{DATABASE}"
properties = {
    "user": USER,
    "password": PASSWORD,
    "driver": "org.postgresql.Driver"
}

df = spark.read.jdbc(url=url, table="employees", properties=properties)

df.show()

df.createOrReplaceTempView("my_temp_view")
query = """SELECT * FROM my_temp_view WHERE salary >= 65000"""

spark.sql(query).show()

data = [
    ("Alice", "Engineer", 75000, "2021-06-15"),
    ("Bob", "Manager", 90000, "2020-05-01"),
    ("Charlie", "HR", 60000, "2019-04-12"),
    ("Diana", "Sales", 50000, "2018-01-25")
]
columns = ["name", "position", "salary", "hire_date"]

df = spark.createDataFrame(data, columns)

filtered_df = df.filter(df.salary >= 60000)
df.show()
filtered_df.show()

filtered_df.write.jdbc(
    url=url,
    table="high_salary_employees",
    mode="overwrite",
    properties=properties
)

print("Усе записалось!")
spark.stop()
