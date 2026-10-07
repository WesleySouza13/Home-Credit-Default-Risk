import pandas as pd 
import os 

query_path = os.path.join('src', 'analytics', 'feature_store.sql')

with open(query_path) as f:
    query = f.read()
    