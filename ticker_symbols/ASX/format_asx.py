import pandas as pd

df = pd.read_csv('ticker_symbols/ASX/asx200_raw.txt', delimiter='\t', header=None)

index_to_drop = [3, 4, 5]
df = df.drop(columns=index_to_drop)

df.to_csv('ticker_symbols/ASX/asx200_raw.txt', sep='\t', header=False, index=False)
