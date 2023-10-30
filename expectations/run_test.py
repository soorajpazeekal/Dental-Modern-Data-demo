import great_expectations as gx
import configparser, logging as log

import findspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("mysql_elt_job") \
    .config("spark.jars.packages", "net.snowflake:snowflake-jdbc:3.13.22") \
    .config("spark.jars.packages", "net.snowflake:spark-snowflake_2.12:2.11.0-spark_3.3").getOrCreate()

log.basicConfig(level=log.INFO)
config = configparser.ConfigParser(); config.read('elt_jobs/.ini') #Run with main root ditectory
context = gx.get_context()

'''Snowflake connection options'''
sfOptions = {
  "sfURL" : config['sfOptions']['sfURL'],
  "sfUser" : config['sfOptions']['sfUser'],
  "sfPassword" : config['sfOptions']['sfPassword'],
  "sfDatabase" : config['sfOptions']['sfDatabase'],
  "sfSchema" : config['sfOptions']['sfSchema'],
  "sfWarehouse" : config['sfOptions']['sfWarehouse']
}

datasource = context.sources.add_spark("_spark_datasource")
data_asset = datasource.add_dataframe_asset(name="_df_asset")

def check_column_not_null(table_names):
    'This test will check if the importent columns are not null (i.e. not empty)'
    'After that, it will check if there are any null values'
    for table_name in table_names:
        df = spark.read.format("net.snowflake.spark.snowflake").options(**sfOptions).option("dbtable", table_name).load()
        my_batch_request = data_asset.build_batch_request(dataframe=df)
        context.add_or_update_expectation_suite("_expectation_suite")
        validator = context.get_validator(
            batch_request=my_batch_request,
            expectation_suite_name="_expectation_suite",
        )
        expectation_validation_result = validator.expect_column_values_to_not_be_null(
        column="PATIENT_ID")
        if expectation_validation_result["success"] == False:
            log.error("Column test case failed. null values in {}".format(table_name))
            return False
        log.info("Column test case passed. no null values in {}".format(table_name))
        expectation_validation_result = validator.expect_column_values_to_be_unique(
        column="PATIENT_ID")
        if expectation_validation_result["success"] == False:
            log.error("Column test case failed. duplicate values in {}".format(table_name))
            return False
        log.info("Column test case passed. no duplicate values in {}".format(table_name))
    return 'All tests passed'

def check_payment_column_for_kpi(table_names):
    for table_name in table_names:
        df = spark.read.format("net.snowflake.spark.snowflake").options(**sfOptions).option("dbtable", table_name).load()
        my_batch_request = data_asset.build_batch_request(dataframe=df)
        context.add_or_update_expectation_suite("_expectation_suite")
        validator = context.get_validator(
            batch_request=my_batch_request,
            expectation_suite_name="_expectation_suite",
        )
        expectation_validation_result = validator.expect_column_values_to_not_be_null(
        column="INVOICE_ID")
        if expectation_validation_result["success"] == False:
            log.error("Column test case failed. null values in {}".format(table_name))
            return False
        log.info("Column test case passed. no null values in {}".format(table_name))
        expectation_validation_result = validator.expect_column_values_to_be_unique(
        column="INVOICE_ID")
        if expectation_validation_result["success"] == False:
            log.error("Column test case failed. duplicate values in {}".format(table_name))
            return False
        log.info("Column test case passed. no duplicate values in {}".format(table_name))
    return 'All tests passed'

if __name__ == "__main__":
    check_column_not_null(table_names=['pi_informations','medical_history',
                                             'dental_records','insurance_information','invoices',
                                             'payment_records'])
    check_payment_column_for_kpi(table_names=['invoices','payment_records'])