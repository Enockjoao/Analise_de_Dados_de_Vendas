from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_csv
from visualizations.plot_sales import plot_sales_by_category, plot_sales_with_seaborn
import pandas as pd

def main():
    
    raw_file_path = r"C:\Users\vitor\Desktop\Pasta_de_Projetos\Analise_de_Dados_de_Vendas\data_pipeline\data\raw\sales_data.csv"
    processed_db_path = "database/sales.db"
    
   
    print("Iniciando o pipeline de dados...")
    
    
    df = extract_data(raw_file_path)
    if df is None:
        return
    
   
    df = transform_data(df)
    
 
    df = load_csv(raw_file_path)  # Carregue o DataFrame usando load_csv
    
    # 4. Plotar
    plot_sales_by_category(df)  # Chame a função de plotagem
    plot_sales_with_seaborn(df)  # Chame a nova função de plotagem com Seaborn
    
    print("Pipeline concluído com sucesso!")

if __name__ == "__main__":
    main()
