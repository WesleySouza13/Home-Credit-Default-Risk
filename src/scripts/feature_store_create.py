import pandas as pd 
import os 
import sqlite3 
query_path = os.path.join('src', 'analytics', 'feature_store.sql')
db_path = db_path = os.path.join('src', 'analytics', 'Credit_Risk_Default.db')
data_path = os.path.join('data', 'processed', 'feature_store.csv')
con = sqlite3.connect(db_path)

with open(query_path) as f:
    query = f.read()

df = pd.read_sql_query(query, con)
df.to_csv(data_path)