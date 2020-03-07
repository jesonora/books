import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import String, Integer
import os


engine = create_engine(os.environ['DATABASE_URL'])

data = [[4, 'Miguel Cervantes'], [5, 'Miguel de Unamuno'], [6, 'Paulo Cohelo']]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['id', 'author'])

# print dataframe.
print(df)

df.to_sql('authors', engine, if_exists='append', index=False, dtype={'id': Integer(), 'author': String()})



