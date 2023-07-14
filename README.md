# YahooFinanceScraping
Using yfinance to download stock data from yahoo finance and save this to a local MySQL database  
Using matplotlib to visualize data

## Create and setup a virtual env
```sh
$ python -m venv scrapeenv
```

### Activate the virtual env
```sh 
$ source scrapeenv/Scripts/activate
```

### Install requirements
```
$ pip install -r requirements.txt
```

# Directories

1. /csv_data - contains historical price data .csv files for each ticker symbol
2. /get_data_scripts - scripts for accessing and saving data from yfinance
3. /ticker_symbols - contains mostly .txt files of groups of ticker symbols, S&P500, TSX60 etc.

# TODO

1. Update the visualization scripts to pull from database instead of .csv files
2. At end of each day add to yfinance_daily and yfinance_yearly (task scheduler)
3. Create visualizations using matplotlib etc directly from database.
4. Figure out why some downloads fail for "The following 'Dividends' events are out-of-range"
5. Compile daily reports based on daily price action for all symbols in S&P
6. When we get daily data, create additional single table to compare all symbols
7. Use Matplotlib to create candle charts for 1d 1m data

# References

- [PandasDocs](https://pandas.pydata.org/docs/index.html)
- [SQLAlchemyDocs](https://docs.sqlalchemy.org/en/20/core/connections.html)
    - [EngineConfig](https://docs.sqlalchemy.org/en/20/core/engines.html#custom-dbapi-args)
- [ColorPaletteGenerator](http://vrl.cs.brown.edu/color)