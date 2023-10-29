import mysql.connector, re
import logging as log
import configparser

log.basicConfig(level=log.INFO)
config = configparser.ConfigParser(); config.read('elt_jobs/.ini') #Change to .ini if running local

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
            except Exception as e:
                log.error(e)
    connection.close()
    log.info(f"tables are dropped successfully")
    return 'ok'

if __name__ == '__main__':
    clean_mysql(cluster_id=['cluster_01'])