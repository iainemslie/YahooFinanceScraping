import mysql.connector
from mysql.connector import Error

import csv

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            autocommit=True
        )
        print("Connection to MySQL Database successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # connection.commit()
        print("Query executed successfully")
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

if __name__ == "__main__":
    connection = create_connection('localhost', 'root', 'password')

    # Create a new database
    # create_database_query = "CREATE DATABASE yfinance"
    # create_database(connection, create_database_query)

    # Create a new table

    # create_table_query = """
    # USE yfinance;
    # CREATE TABLE test2 (
    # employee_id INT,
    # employee_name VARCHAR(50)
    # );
    # """
    # print(create_table_query)
    # execute_query(connection, create_table_query)

    # drop_table_query = """
    # USE yfinance;
    # DROP TABLE test2;
    # """
    # execute_query(connection, drop_table_query)

    # insert_string = """
    # USE yfinance;
    # INSERT INTO test VALUES (
    #     "2023-07-07",
    #     168.23,
    #     168.64,
    #     166.00,
    #     167.14,
    #     1315400,
    #     0.00,
    #     0.00
    # );
    # """
    # execute_query(connection, insert_string)


    with open('csv_data\ZTS_1y.csv', 'r') as infile:
        csvreader = csv.reader(infile)
        for index, row in enumerate(csvreader):
            if index == 0:
                formatted_table_query = create_formatted_table_query('test', row)
                # print(formatted_table_query)
                execute_query(connection, formatted_table_query)
            else:
                connection.reconnect()
                insert_query = create_formatted_insert_query('test', row)
                # print(insert_query)
                execute_query(connection, insert_query)

    connection.close()
