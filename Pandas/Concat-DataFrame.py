# import library
import pandas as pd
import numpy as np

india_weather=pd.DataFrame({'City':['Tamilnadu','Kerala','Karnataka','Andra'],'Temperature':[54,23,87,34],'Humidity':[98,93,87,90]})
us_weather=pd.DataFrame({'City':['Newyork','Orlanda','Chicago','Paris'],'Temperature':[98,73,12,53],'Humidity':[78,98,76,59]})
# df=pd.concat([india_weather,us_weather])
# df=pd.concat([india_weather,us_weather],ignore_index=True)
# df=pd.concat([india_weather,us_weather],keys=['India','US'])
# print(df.loc['US'])
temp_df=pd.DataFrame({
    'City':['Kolkatta','Pune','Dheli','Gujarat'],
    'Temperature':[23,43,87,98]
})
windspeed_df=pd.DataFrame({
    'City':['Kolkatta','Pune','Dheli','Gujarat'],
    'Windspeed':[54,87,65,90]
})
# df=pd.concat([temp_df,windspeed_df],ignore_index=True)
df=pd.concat([temp_df,windspeed_df],axis=1)
print (df)