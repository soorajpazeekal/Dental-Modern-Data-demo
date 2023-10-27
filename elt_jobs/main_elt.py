import findspark
findspark.init()

import configparser, logging as log
from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("mysql_elt_job") \
    .config("spark.jars", "./jars/mysql-connector-j-8.2.0.jar") \
    .config("spark.jars.packages", "net.snowflake:snowflake-jdbc:3.13.22") \
    .config("spark.jars.packages", "net.snowflake:spark-snowflake_2.12:2.11.0-spark_3.3").getOrCreate()
log.basicConfig(level=log.INFO)
config = configparser.ConfigParser(); config.read('.ini')

'''Snowflake connection options'''
sfOptions = {
  "sfURL" : config['sfOptions']['sfURL'],
  "sfUser" : config['sfOptions']['sfUser'],
  "sfPassword" : config['sfOptions']['sfPassword'],
  "sfDatabase" : config['sfOptions']['sfDatabase'],
  "sfSchema" : config['sfOptions']['sfSchema'],
  "sfWarehouse" : config['sfOptions']['sfWarehouse']
}

def read_cluster_02_count(spark):
    jdbc_url = config['cluster_02']['jdbc_url']
    connection_properties = {
    "user": config['global']['username'],
    "password": config['global']['password'],
    "driver": "com.mysql.cj.jdbc.Driver"
    }   
    tables = config['cluster_02']['tables']
    for item in tables.split(','):
        print(item)
        df = spark.read.jdbc(jdbc_url, table=item, properties=connection_properties)
        print(df.show(3))
        df.write.format("net.snowflake.spark.snowflake") \
            .options(**sfOptions) \
            .option("dbtable", item) \
            .mode("overwrite").save()
    spark.stop()

if __name__ == "__main__":
    read_cluster_02_count(spark)