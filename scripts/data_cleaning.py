import os
import pandas as pd

def import_and_clean(stock_data_path):
    data = pd.read_csv(stock_data_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data_clean = data.dropna()
    data_dir = os.path.dirname(stock_data_path)
    cleaned_csv_path = os.path.join(data_dir, 'cleaned_stock_data.csv')
    data_clean.to_csv(cleaned_csv_path, index=False)
    print(data_clean.info())
    print(data_clean.head())
    return data_clean
