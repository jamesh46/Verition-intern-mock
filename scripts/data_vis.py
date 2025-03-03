import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# script to load cleaned data, calculate 20-day MA, generate a plot of closing prices and 20-day MA

def load_cleaned_data(cleaned_data_path):
    data = pd.read_csv(cleaned_data_path)
    return data

def calculate_moving_average(data, window=20):
    data['20-day MA'] = data['close'].rolling(window=window).mean()
    return data

def plot_closing_prices_and_moving_average(data):
    plt.figure(figsize=(12,6))
    plt.plot(data['Date'], data['close'], label='Closing Price')
    plt.plot(data['Date'], data['20-day MA'], label='20-day MA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Closing Prices and 20-day Moving Average')
    plt.legend()
    plt.show()
    
def main():
    cleaned_data_path = 'cleaned_stock_data.csv'
    data = load_cleaned_data(cleaned_data_path)
    data = calculate_moving_average(data)
    plot_closing_prices_and_moving_average(data)
    
if __name__ == '__main__':
    main()