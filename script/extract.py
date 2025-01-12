import pandas as pd
import requests

def extract_data(data):
    # Carregar o arquivo CSV em um DataFrame
    df = pd.read_csv(r"data_pipeline\data\raw\sales_data.csv")  # Definindo df aqui
    print(df.to_string())  # Usando df corretamente
    return df  # Retornando df para uso posterior 