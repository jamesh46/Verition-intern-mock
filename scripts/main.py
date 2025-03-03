import os
from get_data import get_data
from data_cleaning import import_and_clean
from data_vis import calculate_moving_average, plot_closing_prices_and_moving_average
import datetime

def main():
    ticker = 'AAPL'
    start_date = '2023-01-01'
    end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data_files')
    get_data(ticker, start_date, end_date)
    stock_data_path = os.path.join(data_dir, 'stock_data.csv')
    data = import_and_clean(stock_data_path)
    data = calculate_moving_average(data)
    plot_closing_prices_and_moving_average(data)

if __name__ == '__main__':
    main()
