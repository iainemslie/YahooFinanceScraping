import sqlalchemy as sql
import pandas as pd

def fetch_data(symbol_path, connection):
    """
    For every symbol in .txt file at symbol_path fetches corresponding table from database at connection
    """
    symbol_list = []
    with open(symbol_path, 'r') as infile:
        for line in infile:
            symbol_list.append(line.strip().lower())

    for index, symbol in enumerate(symbol_list):
        # For testing only do one
        if index > 0:
            return
        sql = f"SELECT * FROM {symbol}";
        df = pd.read_sql(sql, connection)
        print(list(df.columns))
       

if __name__ == "__main__":
    symbol_path = 'ticker_symbols\S&P\s&p_symbols.txt'
    url_string = "mysql+pymysql://root:password@127.0.0.1/yfinance"
    host_port = dict(host='localhost', port=3306)
    engine = sql.create_engine(url = url_string, echo = False, connect_args=host_port)
    connection = engine.connect()
    fetch_data(symbol_path, connection)
    connection.close()