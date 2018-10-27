# import library
import pandas as pd

# READ CSV

# df=pd.read_csv('weather_data.csv',skiprows=3) # skip first three rows
# df=pd.read_csv('weather_data.csv',header=3)   # skip first three rows
# df=pd.read_csv('weather_data.csv',header=None)# Take header 0,1..
# df=pd.read_csv('weather_data.csv',header=None,names=['Date','Open','Close','High','Low','Trade','Turn']) # Create user defined header
# df=pd.read_csv('weather_data.csv',nrows=2) # print first two rows with header
# df=pd.read_csv('weather_data.csv',na_values=['NA','No Date','not ',-1])
# df=pd.read_csv('weather_data.csv',na_values={
#     'Date':['No Date'],
#     'Close':[-1],
#     'High':['not '],
#     'Low':[-1],
# })

# WRITE CSV

# df.to_csv('newweather_data.csv')
# df.to_csv('newweather_data.csv',index=False)
# df.to_csv('newweather_data.csv',index=False,columns=['Date','High','Low'])
# df.to_csv('new_weather_data.csv',index=False,columns=['Date','High','Low'],header=False)

import xlrd as xl
#READ EXCEL

# df=pd.read_excel('weather_data.xlsx','weather_data')
def convert_Date(cell):
    if cell=='n.a.':
        return '2018-01-03 00:00:00'
    return cell
def convert_Open(cell):
    if cell==-1.00:
        return 0.00
    return cell
# df=pd.read_excel('weather_data.xlsx','weather_data',converters={
#     'Date':convert_Date,
#     'Open':convert_Open
# })
from openpyxl.workbook import workbook
#df.to_excel('new_weather_data.xlsx',sheet_name='weather_data',startrow=1,startcol=2,index=False,header=False)
df_fruits=pd.DataFrame({
    'Fruits':['Apple','Orange','Lemon','PineApple'],
    'Rupees':[100,50,20,80]
})
df_foods=pd.DataFrame({
    'Foods':['Dosa','Idly','Parotta','Sappathy'],
    'Price':[50,10,20,20]
})
with pd.ExcelWriter('fruits_foods.xlsx') as writer:
    df_fruits.to_excel(writer,sheet_name="Fruits")
    df_foods.to_excel(writer, sheet_name="Foods")