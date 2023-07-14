import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ticker_symbols/S&P/s&p500_raw.txt', delimiter='\t', header=None)
df = df.rename({0: "Symbol", 1: "Company Name", 2: "Sector"}, axis=1)

value_counts = df.iloc[:, 2].value_counts().reset_index()
value_counts = value_counts.rename(columns={"count": "Count"})
# print(value_counts)

sectors = value_counts['Sector'].tolist()
# print(sectors)
counts = value_counts['Count'].tolist()
# print(counts)

# Color palette generator - http://vrl.cs.brown.edu/color
colors = ["#75eab6", "#18786a", "#99c1b8", "#378811", "#96ea4e", "#266197", "#a8a2f4", "#EF32D3", "#e586fe", "#F932bf", "#38b5fc"]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

fig, ax = plt.subplots()
ax.pie(counts, explode=explode, labels=sectors, colors=colors, autopct='%.2f %%')

plt.title('S&P500 by Sector')
plt.savefig('visualization/sector/s&p500_by_sector.png', dpi=300)
plt.show()