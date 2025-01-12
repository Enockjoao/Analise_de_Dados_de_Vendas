from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_csv
import pandas as pd

def main():
    # Caminhos
    raw_file_path = r"C:\Users\vitor\Desktop\Pasta_de_Projetos\Analise_de_Dados_de_Vendas\data_pipeline\data\raw\sales_data.csv"
    processed_db_path = "database/sales.db"
    
    # Pipeline
    print("Iniciando o pipeline de dados...")
    
    # 1. Extrair
    df = extract_data(raw_file_path)
    if df is None:
        return
    
    # 2. Transformar
    df = transform_data(df)
    
    # 3. Carregar
    df = load_csv(raw_file_path)  # Carregue o DataFrame usando load_csv
    
    print("Pipeline concluído com sucesso!")

if __name__ == "__main__":
    main()