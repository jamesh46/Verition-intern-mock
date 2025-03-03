import os
import pandas as pd
import matplotlib.pyplot as plt

def load_cleaned_data(cleaned_data_path):
    data = pd.read_csv(cleaned_data_path, parse_dates=['Date'])
    return data

def calculate_moving_average(data, window=20):
    # Calculate 20-day moving average of 'Close'
    data['20-day MA'] = data['Close'].rolling(window=window).mean()
    return data

def plot_closing_prices_and_moving_average(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Close'], label='Closing Price', color='blue')
    plt.plot(data['Date'], data['20-day MA'], label='20-Day MA', linestyle='--', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Closing Prices and 20-Day Moving Average')
    plt.legend()
    plt.grid(True)
    
    # Define the output image path in the data_files folder
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data_files')
    image_path = os.path.join(data_dir, 'closing_prices_and_moving_average.png')
    plt.savefig(image_path)
    plt.show()

def main():
    # Build the path to the cleaned data file
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data_files')
    cleaned_data_path = os.path.join(data_dir, 'cleaned_stock_data.csv')
    data = load_cleaned_data(cleaned_data_path)
    data = calculate_moving_average(data)
    plot_closing_prices_and_moving_average(data)

if __name__ == '__main__':
    main()
