import yfinance as yf
import os
import pandas as pd

def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data.reset_index()
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data_files')
    os.makedirs(data_dir, exist_ok=True)
    csv_path = os.path.join(data_dir, 'stock_data.csv')
    data.to_csv(csv_path, index=False)
    return data

