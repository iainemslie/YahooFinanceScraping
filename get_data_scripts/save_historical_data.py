import yfinance as yf
import sqlalchemy as sql
import os

def save_historical_data_as_csv(symbol_path, output_dir, time_period):
    """
    Reads list of ticker symbols from .txt file, gets data from yfinance and saves it to .csv files
        
        Parameters:
            symbol_path (str): path to .txt file at symbol_path containing one ticker symbol per line
            output_dir (str): path to the output directory that stores .csv files
            time_period (str): time period to get data for e.g. 1m, 1y, 1d
    """

    symbol_list = []
    with open(symbol_path, 'r') as infile:
        for line in infile:
            symbol_list.append(line.strip())
            
    for symbol in symbol_list:
        file_path = f'{output_dir}/{symbol}_{time_period}.csv'
        if not os.path.isfile(file_path):
            try:
                ticker = yf.Ticker(symbol)
                ticker_history = ticker.history(period=time_period)
                ticker_history.to_csv(file_path)
            except Exception as e:
                print(f"Error for {symbol}:")
                print(e)

def save_historical_data_to_db(symbol_path, time_period, connection):
    """
    Reads list of ticker symbols from .txt file, gets data from yfinance and saves it to .csv files
        
        Parameters:
            symbol_path (str): path to .txt file at symbol_path containing one ticker symbol per line
            time_period (str): time period to get data for e.g. 1m, 1y, 1d
            connection (obj): SQLAlchemy connection object 
    """

    symbol_list = []
    with open(symbol_path, 'r') as infile:
        for line in infile:
            symbol_list.append(line.strip())
            
    for symbol in symbol_list:
            try:
                ticker = yf.Ticker(symbol)
                ticker_history = ticker.history(period=time_period)
                ticker_history.to_sql(name=symbol.lower(), con=connection, if_exists='replace', index=False)
                print(f"Successfully created table for {symbol}")
            except Exception as e:
                print(f"Error for {symbol}:")
                print(e)

# save_historical_data_as_csv('ticker_symbols\S&P\s&p_symbols.txt', 'csv_data', '1y')

# SQL
url_string = "mysql+pymysql://root:password@127.0.0.1/yfinance"
engine = sql.create_engine(url = url_string, echo = False, connect_args=dict(host='localhost', port=3306))
connection = engine.connect()
save_historical_data_to_db('ticker_symbols\S&P\s&p_symbols.txt', 'csv_data', '1y', connection=connection)
connection.close()