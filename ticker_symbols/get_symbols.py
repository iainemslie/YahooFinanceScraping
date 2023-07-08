
symbol_list = []
with open('ticker_symbols/S&P/s&p500_raw.txt', 'r') as infile:
    for line in infile:
        symbol = line.split(' ')[0]
        # yfinance formats with a dash instead of a dot
        symbol = symbol.replace(".", "-")
        symbol_list.append(symbol)

# print(symbol_list)

with open('ticker_symbols/S&P/s&p_symbols.txt', 'w') as outfile:
    for symbol in symbol_list:
        outfile.write(f'{symbol}\n')

