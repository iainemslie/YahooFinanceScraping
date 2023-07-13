import yfinance as yf
import sqlalchemy as sql
import os

def save_historical_data(symbol_path, time_period, connection = None, output_dir = None):
    """
    Reads list of ticker symbols from .txt file, gets data from yfinance and saves it to sql database or csv file
        
        Parameters:
            symbol_path (str): path to .txt file at symbol_path containing one ticker symbol per line
            time_period (str): time period to get data for e.g. 1m, 1y, 1d
            connection (obj): SQLAlchemy connection object - if connection is None then don't write to DB
            output_dir (str): if output_dir is not None then write .csv file to the path
    """

    symbol_list = []
    with open(symbol_path, 'r') as infile:
        for line in infile:
            symbol_list.append(line.strip())

    if connection is None and output_dir is None:
        print("No connection or output directory provided: nothing to do")
        return
            
    for symbol in symbol_list:
            try:
                ticker = yf.Ticker(symbol)
                ticker_history = ticker.history(period=time_period)

                if output_dir is not None:
                    file_path = f'{output_dir}/{symbol}_{time_period}.csv'
                    ticker_history.to_csv(file_path)
                    print(f"Successfully created .csv file {file_path}")

                if connection is not None:
                    ticker_history.to_sql(name=symbol.lower(), con=connection, if_exists='replace')
                    print(f"Successfully created table for {symbol}")
                
            except Exception as e:
                print(f"Error for {symbol}:")
                print(e)

# save_historical_data_as_csv('ticker_symbols\S&P\s&p_symbols.txt', 'csv_data', '1y')

# SQL
url_string = "mysql+pymysql://root:password@127.0.0.1/yfinance"
engine = sql.create_engine(url = url_string, echo = False, connect_args=dict(host='localhost', port=3306))
connection = engine.connect()
save_historical_data('ticker_symbols\S&P\s&p_symbols.txt', '1y', connection=connection)
connection.close()