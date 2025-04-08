import pandas as pd
import os
import sqlite3


def load_csv(file_path):
    
    try:
        df = pd.read_csv(file_path, index_col=0)  # Usando a primeira coluna como índice
        print("CSV carregado com sucesso!")
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo {file_path} não encontrado.")
        return None



csv_path = r"c:\Users\vitor\Desktop\Pasta_de_Projetos\Analise_de_Dados_de_Vendas\data_pipeline\data\raw\sales_data.csv"


df = load_csv(csv_path)

if df is not None:
    
    os.makedirs('database', exist_ok=True)

    
    database_path = os.path.join('database', 'sales.db')

    
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            product TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            date TEXT NOT NULL
        );
    ''')
    print("Tabela criada com sucesso!")

    
    try:
        df.to_sql('sales', conn, if_exists='replace', index=False)
        print("Dados inseridos com sucesso no banco de dados!")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

   
    conn.close()
else:
    print("Operação cancelada devido a erro no carregamento do CSV.")
