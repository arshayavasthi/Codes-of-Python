import pandas as pd
df=pd.read_csv('tec.csv')
print(df)
print(df['marks'].max())
print(df['name'][df['fcolor']=='red'])
print(df['marks'].mean())
