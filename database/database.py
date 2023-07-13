import mysql.connector
from mysql.connector import Error

import csv
import os
import time

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            autocommit = True,
            pool_reset_session=True,
            pool_size = 32
        )
        print("Connection to MySQL Database successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query, multi=True)
        # connection.commit()
        #print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_formatted_table_query(table_name, header):
    create_table_query = f"""
    USE yfinance;
    CREATE TABLE {table_name} (
        {header[0]} DATE,
        {header[1]} DECIMAL(6, 2),
        {header[2]} DECIMAL(6, 2),
        {header[3]} DECIMAL(6, 2),
        {header[4]} DECIMAL(6, 2),
        {header[5]} INT,
        {header[6]} DECIMAL(6, 2),
        {header[7].replace(" ", "_")} DECIMAL(6, 2)
    );
    """
    return create_table_query

def create_formatted_insert_query(table_name, values):
    insert_query = f'''
    USE yfinance;
    INSERT INTO {table_name} (Date,Open,High,Low,Close,Volume,Dividends,Stock_Splits) VALUES (
        "{values[0].split(' ')[0]}", 
        {float(values[1]):.2f},
        {float(values[2]):.2f},
        {float(values[3]):.2f},
        {float(values[4]):.2f},
        {int(values[5])},
        {float(values[6]):.2f},
        {float(values[7]):.2f}
    );
    '''
    return insert_query

def write_csv_to_db(connection, file_path):
    """
    Reads .csv file from file_path and creates a set of queries to insert table data
        
        Parameters:
            connection PooledMySQLConnection: Database connection object
            file_path (str): path to a .csv file
    """
    symbol = os.path.split(file_path)[-1].split("_")[0]
    with open(file_path, 'r') as infile:
        csvreader = csv.reader(infile)
        for index, row in enumerate(csvreader):
            if index == 0:
                connection.reconnect()
                formatted_table_query = create_formatted_table_query(symbol, row)
                # print(formatted_table_query)
                execute_query(connection, formatted_table_query)
            else:
                connection.reconnect()
                insert_query = create_formatted_insert_query(symbol, row)
                # print(insert_query)
                execute_query(connection, insert_query)

def get_csv_file_dir(dir_path) -> list:
    """
    Reads the directory at dir_path and returns a list of paths to .csv files
        
        Parameters:
            dir_path (str): path to a directory containing .csv files
        Returns:
            A list of .csv file paths
    """
    csv_list = []
    if os.path.isdir(dir_path):
        csv_list = os.listdir(dir_path)
        csv_list = [os.path.join(dir_path,csv) for csv in csv_list if csv.endswith('.csv')]
    return csv_list

if __name__ == "__main__":

    connection = create_connection('localhost', 'root', 'password')
    csv_list = get_csv_file_dir('.\csv_data')

    #TODO : BUG Fatal Python error: none_dealloc: deallocating None: bug likely caused by a refcount error in a C extension
    for index, csv_path in enumerate(csv_list):
            write_csv_to_db(connection, csv_path)
    
    connection.close()
    
