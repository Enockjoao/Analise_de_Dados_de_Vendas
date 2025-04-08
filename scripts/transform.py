import pandas as pd
import requests


def transform_data(data):
    data = data.dropna()
    data["price"] = data["price"].astype(float)
    data["quantity"] = data["quantity"].astype(int) 
    data = data.fillna(0) 
    data["date"] = pd.to_datetime(data["date"]) 
    return data


