import yfinance as yf
import sqlalchemy as sql
import os

def save_historical_data(symbol_path, period, interval, prepost, connection = None, output_dir = None):
    """
    Reads list of ticker symbols from .txt file, gets data from yfinance and saves it to sql database or csv file
        
        Parameters:
            symbol_path : str
                Path to .txt file at symbol_path containing one ticker symbol per line
            period : str
                Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                Either Use period parameter or use start and end
            interval : str
                Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                Intraday data cannot extend last 60 days
            prepost : bool
                Include Pre and Post market data in results?
                Default is False
            connection : (obj)
                SQLAlchemy connection object - if connection is None then don't write to DB
            output_dir : (str)
                If output_dir is not None then write .csv file to the path
    """

    symbol_list = []
    with open(symbol_path, 'r') as infile:
        for line in infile:
            symbol_list.append(line.strip())

    if not connection and not output_dir:
        print("No connection or output directory provided: nothing to do")
        return
            
    for symbol in symbol_list:
            try:
                ticker = yf.Ticker(symbol)
                ticker_history = ticker.history(period=period, interval=interval, rounding=True, prepost=prepost)

                if output_dir:
                    file_path = f'{output_dir}/{symbol}_{period}.csv'
                    ticker_history.to_csv(file_path)
                    print(f"Successfully created .csv file {file_path}")

                if connection:
                    ticker_history.to_sql(name=symbol.lower(), con=connection, if_exists='append',)
                    print(f"Successfully created table for {symbol}")
                
            except Exception as e:
                print(f"Error for {symbol}:")
                print(e)


if __name__ == "__main__":
    symbol_path = 'ticker_symbols\S&P\s&p_symbols.txt'

    url_string = "mysql+pymysql://root:password@127.0.0.1/yfinance"
    host_port = dict(host='localhost', port=3306)
    engine = sql.create_engine(url = url_string, echo = False, connect_args=host_port)
    connection = engine.connect()
    save_historical_data(symbol_path, interval='1d', period='1m', prepost=False, connection=connection)
    connection.close()