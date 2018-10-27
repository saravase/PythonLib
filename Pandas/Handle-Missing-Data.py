# import libraries
import pandas as pd
import numpy as np
df=pd.read_csv('weather_data.csv',parse_dates=['Date'])
# df.set_index('Date',inplace=True)
# new_df=df.fillna(0)
# new_df=df.fillna({
#     'Open':0,
#     'Shares Traded':1,
#     'Turnover (Rs. Cr)':3
# })
# new_df=df.fillna(method='ffill')
# new_df=df.fillna(method='bfill')
# new_df=df.fillna(method='bfill',axis='columns')
# new_df=df.fillna(method='ffill',limit=1) # If you have two row sequentially.t was replace only first row.
# new_df=df.interpolate()
# new_df=df.interpolate(method='time')
# new_df=df.dropna() #  Remove NaN available column from DataFrame
# new_df=df.dropna(how="all") # Which row has every column NaN value. That row removed from the DF
# new_df=df.dropna(thresh=1) # Which row has only one NaN value. That row removed from the DF
# new_df=df.dropna(thresh=2) # Which row has two NaN value. That row removed from the DF

# Replace
# new_df=df.replace(-99999,np.NaN)
# new_df=df.replace([-99999,-88888],np.NaN)
# new_df=df.replace({
#     'Open':-99999,
#     'Low':-99999,
#     'High':-99999,
# # },np.NaN)
# new_df=df.replace({
#     -99999:np.NaN,
#     'No Event':'Festivel'
# # })
# new_df=df.replace({
#     'Open':'[A-Za-z]'
# },'',regex=True)
#new_df=df.replace(['poor','average','good','exceptional'],[1,2,3,4])
print(new_df)