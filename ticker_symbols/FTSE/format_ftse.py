import pandas as pd

df = pd.read_csv('ticker_symbols/FTSE/ftse100_raw.txt', delimiter='\t', header=None)
df.columns = ['Company Name', 'Symbol', 'Sector']
new_index = ['Symbol', 'Company Name', 'Sector']
df = df.reindex(columns=new_index)
df.to_csv('ticker_symbols/FTSE/ftse100_raw.txt', sep='\t', header=False, index=False)

