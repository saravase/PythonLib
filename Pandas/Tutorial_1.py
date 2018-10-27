# import library
import pandas as pd
df=pd.read_csv('data.csv')
print(df['Open'].max())
print(df['High'].mean())
print(df['Date'][df['Low']>11000])