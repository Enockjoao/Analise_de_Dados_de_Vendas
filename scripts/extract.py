import pandas as pd
import requests

def extract_data(data):
   
    df = pd.read_csv(r"data_pipeline\data\raw\sales_data.csv")  # Definindo df aqui
    print(df.to_string())  # Usando df corretamente
    return df  
