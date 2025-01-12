import pandas as pd
import os



def load_csv(sales):
    sales = (r"sales_data.csv")
    df = pd.read_csv(sales, index_col=(0))

    df.read(sales)

