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

def read_cluster_and_write_sf(spark, cluster_id):
    """
    Reads data from a mysql database and writes it to Snowflake.

    Args:
        spark (SparkSession): The SparkSession object.
        cluster_id (list): A list of cluster IDs.

    Returns:
        str: The string 'ok' indicating the operation was successful.
    """
    for item in cluster_id:
        jdbc_url = config[item]['jdbc_url']
        connection_properties = {
        "user": config['global']['username'],
        "password": config['global']['password'],
        "driver": "com.mysql.cj.jdbc.Driver"
        }   
        tables = config[item]['tables']
        for item in tables.split(','):
            try:
                df = spark.read.jdbc(jdbc_url, table=item, properties=connection_properties)
                df.write.format("net.snowflake.spark.snowflake") \
                    .options(**sfOptions) \
                    .option("dbtable", item) \
                    .mode("overwrite").save()
            except Exception as e:
                log.error(e)
        log.info(f"Database {item} operations completed")
    return 'ok'


if __name__ == "__main__":
    read_cluster_and_write_sf(spark, cluster_id=['cluster_01'])
    spark.stop()
