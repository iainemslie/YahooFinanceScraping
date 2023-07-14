# YahooFinanceScraping
Using yfinance to download stock data from yahoo finance

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
3. /ticker_symbols - contains mostly .txt files of groups of ticker symbols, S&P500 etc.

# TODO

1. ✅ Use SQL Alchemy to insert Pandas Dataframe directly when getting data from yfinance
2. ✅ Make sure datetime info is included for the new tables (removed index = False)
3. For each symbol create a database table, get 5y historical data, then at end of each day (task scheduler) update the table with the daily price info
4. Create visualizations using matplotlib etc directly from database.
5. Figure out why some downloads fail for "The following 'Dividends' events are out-of-range"
6. Update the visualization scripts to pull from database instead of .csv files
7. Get daily 1d 1m tables as well as updating 1y 1d tables at end of day
8. Compile daily reports based on daily price action for all symbols in S&P
9. When we get daily data, create additional single table to compare all symbols
10. Use Matplotlib to create candle charts for 1d 1m data

# References

- [PandasDocs](https://pandas.pydata.org/docs/index.html)
- [SQLAlchemyDocs](https://docs.sqlalchemy.org/en/20/core/connections.html)
    - [EngineConfig](https://docs.sqlalchemy.org/en/20/core/engines.html#custom-dbapi-args)