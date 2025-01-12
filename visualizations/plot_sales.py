import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_by_category(df):
    # Agrupar os dados por categoria e somar as quantidades
    sales_by_category = df.groupby('category')['quantity'].sum()

    # Criar um gráfico de barras
    sales_by_category.plot(kind='bar', color='skyblue')

    # Adicionar título e rótulos
    plt.title('Quantidade de Produtos Vendidos por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Quantidade Vendida')

    # Exibir o gráfico
    plt.show()

def plot_sales_with_seaborn(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='category', y='quantity', estimator=sum)
    plt.title('Total de Vendas por Categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()