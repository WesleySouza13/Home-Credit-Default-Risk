import pandas as pd 
import os 
import sqlite3 
raw_path = os.path.join('data', 'raw')
data_dir = os.scandir(raw_path)
db_path = os.path.join('src', 'analytics', 'Credit_Risk_Default.db')
con = sqlite3.connect(db_path)

# mudando chunk de carregamento para aumentar base de dados 
for dir in data_dir:
    if dir.is_file() and dir.name.endswith('.csv'):
        print(f"Arquivo {dir.name} encontrado")
        table_name = os.path.splitext(dir.name)[0]
        for i, df in enumerate(pd.read_csv(dir.path, encoding='utf-8', chunksize=100_000)):
            df.to_sql(table_name, con=con,if_exists='replace' if i == 0 else 'append',index=False)
            print(f"  bloco {i+1} de {dir.name} gravado")
        print(f"tabela {table_name} criada")
        cols = [c[1] for c in con.execute(f'PRAGMA table_info("{table_name}")')]
        for key in ('SK_ID_CURR', 'SK_ID_BUREAU', 'SK_ID_PREV'):
            if key in cols:
                con.execute(f'CREATE INDEX IF NOT EXISTS idx_{table_name}_{key} ON "{table_name}"({key})')
        con.commit()
        print()
print('Criaçao de Bd concluida')
con.close()