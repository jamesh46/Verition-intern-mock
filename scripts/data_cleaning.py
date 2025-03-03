import numpy as numpy
import pandas as pd

def import_and_clean(stock_data_path):
    data = pd.read_csv(stock_data_path)
    data['Date'] = pd.to_datetime(data['date'])
    data = data.dropna()
    data.to_csv('cleaned_stock_data.csv', index=False)
    return data.describe(), data.head()