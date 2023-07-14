import yfinance as yf

msft = yf.Ticker("MSFT")


# Doesn't work
# print(msft.info)

# Works
print(msft.basic_info)
# print(msft.income_stmt)
# print(msft.history(period="1d"))
# print(msft.history_metadata)
# print(msft.actions)
# print(msft.dividends)
# print(msft.get_shares_full())
# print(msft.income_stmt)
# print(msft.balance_sheet)
# print(msft.quarterly_cash_flow)
# print(msft.news)
