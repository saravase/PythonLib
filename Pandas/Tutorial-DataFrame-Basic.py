# import library
import pandas as pd
df=pd.read_csv('data.csv')
# print(df.shape)    # Get shape(124,7)
# print(df.head)     # Print Everything
# print(df.tail())   # Print last 5 rows
# print(df.tail(1))  # Print last row
# print(df[2:5])     # Print rows[2,3,4]
# print(df.columns)    # Print header only
# print(df['Open'])   #Print open column only
# print(type(df['Open'])) # Print Series
# print(type(df) # Print Dataframe
# print(df[['Open','High','Low']]) # Print columns['Open','High','Low']
# print(df['High'].max()) # Print maximum high data
# print(df['High'].std()) # Print SD
# print(df.describe())    # Print count,mean,std,min,max
# print(df[df.Open>11000]) # Print open data higher then  11000
# print(df[['Date','Open']][df.Open==df['Open'].max()])
# print(df.index) # RangeIndex(start=0, stop=124, step=1)
# df.set_index('Date',inplace=True)
# print(df.loc['05-Jan-2018'])
# df.reset_index(inplace=True)
