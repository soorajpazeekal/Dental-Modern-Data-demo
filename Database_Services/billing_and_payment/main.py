import mysql.connector, os, logging as log

from dotenv import load_dotenv
from generate import *

load_dotenv()
log.basicConfig(level=log.INFO)

try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = os.getenv("MYSQL_ROOT_PASSWORD"),
        database = os.getenv("MYSQL_DATABASE")
    )
except mysql.connector.Error as err:
        conn = mysql.connector.connect(
        host = 'mysql',
        user = 'root',
        password = os.getenv("MYSQL_ROOT_PASSWORD"),
        database = os.getenv("MYSQL_DATABASE")
    )
        
def init_execute_sql(file_path = "sql/prepare.sql", connection = conn):
    with open(file_path, "r") as sql_file:
        commands = sql_file.read().split(";")
        cursor = connection.cursor()
        for command in commands:
            try:
                if command.strip():
                    cursor.execute(command)
                    connection.commit()
                    log.info("Sql table create successfully executed")
            except mysql.connector.Error as err:
                log.error(err)
                connection.rollback()
        cursor.close()

if __name__ == "__main__":
    init_execute_sql()
    invoice_id, patient_id, total_amount = tr_invoice(conn)
    tr_payment_records(conn, invoice_id, patient_id, total_amount)
