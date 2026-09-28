import pandas as pd 
import os 
import sqlite3 
raw_path = os.path.join('data', 'raw')
data_dir = os.scandir(raw_path)
db_path = os.path.join('src', 'analytics', 'Credit_Risk_Default.db')
con = sqlite3.connect(db_path)

for dir in data_dir:
    if dir.is_file() and dir.name.endswith('.csv'):
        print(f"Arquivo {dir.name} encontrado")

        df = pd.read_csv(dir, encoding='utf-8', nrows=15000)
        print(f"arquivo {dir.name} transformado em dataframe")
        print()
        # criando db 
        table_name = dir.name.strip('.csv')
        df.to_sql(table_name, if_exists='append', con=con, index=False)
        print(f"tabela {table_name} criada")
        print()