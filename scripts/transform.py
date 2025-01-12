import pandas as pd
import requests


def transform_data(data):
    data = data.dropna()
    data["price"] = data["price"].astype(float) # Estou transformando a coluna price em float 
    data["quantity"] = data["quantity"].astype(int) # Estou transformando a coluna quantity em int
    data = data.fillna(0) # transformando os Null em 0
    data["date"] = pd.to_datetime(data["date"]) # transformando a data em modo de data
    return data


