
symbol_list = []
with open('ticker_symbols/TSX/tsx_raw.txt', 'r') as infile:
    for line in infile:
        symbol = line.split(' ')[0]
        # yfinance formats with a dash instead of a dot
        symbol = symbol.replace(".", "-")
        symbol_list.append(symbol)

# print(symbol_list)

with open('ticker_symbols/TSX/tsx_symbols.txt', 'w') as outfile:
    for symbol in symbol_list:
        outfile.write(f'{symbol}.TO\n')

