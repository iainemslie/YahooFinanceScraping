import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_volume(input_file):
    """
    Reads .csv file specified by input file and plots date and volume plot using matplotlib
        
        Parameters:
            input_file (str): path to .csv file one year stock price information
    """
    symbol = input_file.split('_')[0]
    file_name = input_file.split('.')[0]

    df = pd.read_csv(f"csv_data/{input_file}")

    # Convert string representation of date into datetime
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
    # Remove timestamp and only have date
    df['Date'] = df['Date'].dt.date

    plt.figure(figsize=(8,5))

    plt.title(f'One Year Trade Volume for {symbol}')

    plt.xlabel('Month')
    plt.ylabel('Volume')

    plt.plot(df.Date, df.Volume)

    plt.savefig(f'visualization/volume/{file_name}.png', dpi=300)
    plt.close()

def plot_price(input_file):
    """
    Reads .csv file specified by input file and plots date and volume plot using matplotlib
        
        Parameters:
            input_file (str): path to .csv file one year stock price information
    """
    symbol = input_file.split('_')[0]
    file_name = input_file.split('.')[0]

    df = pd.read_csv(f"csv_data/{input_file}")

    # Convert string representation of date into datetime
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
    # Remove timestamp and only have date
    df['Date'] = df['Date'].dt.date

    plt.figure(figsize=(8,5))

    plt.title(f'One Year Price for {symbol}')

    plt.xlabel('Month')
    plt.ylabel('Closing Price ($USD)')

    plt.plot(df.Date, df.Close)

    plt.savefig(f'visualization/price/{file_name}.png', dpi=300)
    plt.close()

for file_name in os.listdir('csv_data'):
    """
    For every file in /csv_data we create a plot and save it
    """
    plot_volume(file_name)
    # plot_price(file_name)
