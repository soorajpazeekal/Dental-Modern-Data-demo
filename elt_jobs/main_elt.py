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
                    .mode("append").save()
            except Exception as e:
                log.error(e)
        log.info(f"Database {item} operations completed")
    return 'ok'


def clean_mysql(cluster_id):
    """
    Cleans MySQL tables based on the provided cluster_id.

    Parameters:
    - cluster_id (list): A list of cluster IDs.

    Returns:
    - str: The string 'ok' indicating the operation was successful.

    Raises:
    - Exception: If an error occurs while dropping the tables.

    Notes:
    - This function uses the `mysql.connector` module to connect to the MySQL database.
    - The function iterates over each cluster ID in the `cluster_id` list.
    - For each cluster ID, the function extracts the IP address and database name from the `jdbc_url` property in the `config` dictionary.
    - The function establishes a connection to the MySQL database using the extracted IP address, database name, and global username and password from the `config` dictionary.
    - The function retrieves the list of tables to be dropped from the `tables` property in the `config` dictionary for the current cluster ID.
    - The function iterates over each table in the list of tables and drops the table using the `DROP TABLE` SQL statement.
    - If an error occurs while dropping a table, an exception is raised and logged.
    - After dropping all the tables for a cluster ID, the connection to the database is closed.
    - Finally, a success message is logged indicating that the tables have been dropped successfully.
    """
    import mysql.connector, re

    for item in cluster_id:
        match = re.search(r'jdbc:mysql://(.*?):\d+/(.*?)$', config[item]['jdbc_url'])
        ip_address = match.group(1); database_name = match.group(2)
        conn_properties = {
        'user': config['global']['username'],
        'password': config['global']['password'],
        'host': ip_address,
        'database': database_name
        }

        tabels = config[item]['tables']
        for item in tabels.split(','):
            try:
                connection = mysql.connector.connect(**conn_properties)
                with connection.cursor() as cursor:
                    queries_to_execute = f"""
                    SET FOREIGN_KEY_CHECKS=0;
                    DROP TABLE IF EXISTS {item};
                    """
                    cursor.execute(queries_to_execute, multi=True)
                    connection.commit()
                cursor.close()
            except Exception as e:
                log.error(e)
    connection.close()
    log.info(f"tables are dropped successfully")
    return 'ok'


if __name__ == "__main__":
    read_cluster_and_write_sf(spark, cluster_id=['cluster_01'])
    clean_mysql(cluster_id=['cluster_01'])
    spark.stop()
