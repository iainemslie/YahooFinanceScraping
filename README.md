# YahooFinanceScraping
Using yfinance to download stock data from yahoo finance

## Create and setup a virtual env
- `python -m venv scrapeenv`

### Activate the virtual env
- `source scrapeenv/Scripts/activate`

### Install requirements
- `pip install requirements.txt`

# Directories

1. /csv_data - contains historical price data .csv files for each ticker symbol
2. /get_data_scripts - scripts for accessing and saving data from yfinance
3. /ticker_symbols - contains mostly .txt files of groups of ticker symbols, S&P500 etc.