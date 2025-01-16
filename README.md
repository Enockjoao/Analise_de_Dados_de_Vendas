# Pipeline de Análise de Dados de Vendas 🚀✨📊

---

## **Descrição do Projeto** 📜🛠️💡

Este projeto implementa uma pipeline de dados para realizar o processo de **ETL (Extração, Transformação e Carregamento)** de um conjunto de dados de vendas. O objetivo principal é transformar um arquivo CSV bruto em dados organizados e armazenados em um banco de dados SQLite, prontos para análise e visualização.

Este projeto é ideal para entender o ciclo de vida dos dados em pipelines e pode ser expandido para casos reais em aplicações de engenharia de dados. 🔍📈🌟

---

## **Estrutura do Projeto** 🗂️⚙️🔧

A estrutura segue boas práticas de organização para facilitar a colaboração e manutenção:

```
data-pipeline/
├── data/
│   ├── raw/                # Arquivos CSV originais
│   │   └── sales_data.csv  # Arquivo bruto de vendas
│   └── processed/          # Dados limpos e transformados
├── database/               # Banco de dados SQLite
│   └── sales.db            # Banco criado pela pipeline
├── scripts/                # Scripts ETL
│   ├── extract.py          # Extração dos dados do CSV
│   ├── transform.py        # Limpeza e transformação dos dados
│   ├── load.py             # Carregamento dos dados no SQLite
│   └── utils.py            # Funções auxiliares para análise e visualização
├── main.py                 # Script principal para orquestrar a pipeline
├── requirements.txt        # Dependências do projeto
└── LICENSE                 # Licença do projeto
```

---

## **Tecnologias Utilizadas** 💻📚🔬

- **Linguagem:** Python 3.8+
- **Bibliotecas:**
  - `pandas`: Manipulação e análise de dados.
  - `sqlite3`: Interação com banco de dados SQLite.
  - `sqlalchemy`: Alternativa para consultas SQL avançadas.
  - `matplotlib` e `seaborn`: Visualização de dados (prontos para futuras análises).

---

## **Configuração do Ambiente** 🖥️🛠️📦

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/data-pipeline.git
   cd data-pipeline
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate      # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

---

## **Como Usar** 🏃‍♂️📂⚙️

1. **Adicione os dados brutos:**
   Coloque o arquivo CSV de vendas (`sales_data.csv`) na pasta `data/raw/`.

2. **Execute a pipeline:**

   ```bash
   python main.py
   ```

3. **Verifique os resultados:**
   - O banco de dados `sales.db` será criado na pasta `database/`.
   - Os dados transformados estarão disponíveis na tabela `sales`. 🎯📊✅

---

## **Funcionamento da Pipeline** 🔍⚙️📈

### **1. Extração** 📥📋💾
O script `extract.py` lê o arquivo CSV bruto e converte os dados em um DataFrame do pandas.

### **2. Transformação** 🛠️🧹🔄
O script `transform.py` aplica as seguintes transformações:
- Remove entradas nulas.
- Converte colunas para os tipos apropriados:
  - `price`: `float`
  - `quantity`: `int`
  - `date`: `datetime`
- Garante que todos os dados estejam consistentes e prontos para análise.

### **3. Carregamento** 📤📂🗄️
O script `load.py` carrega os dados transformados em um banco de dados SQLite, criando a tabela `sales` se ela ainda não existir.

---

## **Exemplo de Expansão** 🚀🌍🔧

Este projeto pode ser expandido com:
- **Dashboards:** Use ferramentas como Tableau ou Power BI conectadas ao SQLite para criar gráficos e relatórios.
- **Automatização:** Integre o pipeline com Airflow ou Prefect para execução agendada.
- **Conexão com APIs:** Extraia dados diretamente de APIs externas em vez de arquivos CSV.

---


