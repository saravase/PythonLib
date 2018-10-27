# import libraries
import pandas as pd
import numpy as np
df=pd.read_csv('weather_cities.csv')
g=df.groupby('City')
# for city,city_df in g:
#     print(city)
#     print(city_df)
# print(g.get_group('Tamilnadu'))
# print(g.max())
# print(g.mean())
# print(g.describe())
