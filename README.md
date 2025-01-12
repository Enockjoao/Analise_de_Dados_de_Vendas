# README do Projeto de Análise de Dados de Vendas

## Descrição

Este projeto é uma pipeline de dados que realiza a extração, transformação e carregamento (ETL) de dados de vendas a partir de um arquivo CSV. O objetivo é processar os dados e armazená-los em um banco de dados SQLite para análises futuras.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

-data_pipeline/.
-│.
-├── data/.
-│ └── raw/.
-│ └── sales_data.csv # Arquivo CSV com dados de vendas.
-│.
-├── scripts/.
-│ ├── extract.py # Script para extrair dados do CSV.
-│ ├── transform.py # Script para transformar os dados.
-│ └── load.py # Script para carregar os dados no banco de dados.
-│.
-├── main.py # Script principal que executa a pipeline.
-└── requirements.txt # Dependências do projeto.


## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalar as dependências, execute:

bash
pip install -r requirements.txt


As principais bibliotecas utilizadas são:

- `pandas`: Para manipulação e análise de dados.
- `sqlalchemy`: Para interagir com o banco de dados SQLite.
- `matplotlib`: Para visualização de dados (não utilizado diretamente neste projeto, mas incluído para futuras análises).
- `seaborn`: Para visualização de dados (não utilizado diretamente neste projeto, mas incluído para futuras análises).

## Como Usar

1. **Preparar o Ambiente**: Certifique-se de ter o Python e as dependências instaladas.

2. **Colocar os Dados**: Coloque o arquivo `sales_data.csv` na pasta `data/raw/`.

3. **Executar a Pipeline**: Execute o script principal para iniciar a pipeline de dados:

   ```bash
   python main.py
   ```

4. **Verificar o Banco de Dados**: Após a execução, os dados processados serão armazenados no banco de dados SQLite localizado em `database/sales.db`.

## Funcionamento da Pipeline

A pipeline é composta por três etapas principais:

1. **Extração**: O script `extract.py` lê os dados do arquivo CSV e os carrega em um DataFrame do pandas.

2. **Transformação**: O script `transform.py` realiza as seguintes transformações nos dados:
   - Remove entradas com valores ausentes.
   - Converte a coluna de preços para o tipo `float`.
   - Converte a coluna de quantidade para o tipo `int`.
   - Preenche valores nulos com zero.
   - Converte a coluna de data para o tipo `datetime`.

3. **Carregamento**: O script `load.py` carrega os dados transformados em uma tabela no banco de dados SQLite.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

