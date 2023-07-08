import yfinance as yf
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
        if not os.path.isfile(f'{output_dir}/{symbol}_{time_period}.csv'):
            try:
                ticker = yf.Ticker(symbol)
                ticker_history = ticker.history(period=time_period)
                ticker_history.to_csv(f'{output_dir}/{symbol}_{time_period}.csv')
            except Exception as e:
                print(f"Error for {symbol}:")
                print(e)

save_historical_data_as_csv('ticker_symbols\S&P\s&p_symbols.txt', 'csv_data', '1y')