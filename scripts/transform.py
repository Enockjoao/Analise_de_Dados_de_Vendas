import pandas as pd
import requests


def transform_data():
    data = data.dropna()
    data["price"] = data["price"].astype(float) # Estou transformando a coluna price em float 
    data["quantity"] = data["quantity"].astype(int) # Estou transformando a coluna quantity em int
    data = pd.fillna(0) # transformando os Null em 0
    return data


