"""
Demo of SQLAlchemy
"""
import csv
from sqlalchemy import create_engine

engine = create_engine("sqlite:///crm.db", echo=True)
print(engine.table_names())

with engine.connect() as connection:
    result = connection.execute("SELECT * FROM clients LIMIT 5")
    for row in result:
        print(row)

import pandas as pd
df = pd.read_sql("SELECT * FROM clients LIMIT 5", engine)
print(df.head())
