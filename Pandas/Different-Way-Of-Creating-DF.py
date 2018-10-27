# import libraries
import pandas as pd
df=pd.read_csv('data.csv')
df=pd.read_excel('data,xlsx','Sheet1')
weather_data={
    'day':['1/1/2017','2/1/2017','3/1/2017','4/1/2017'],
    'Event':['Rain','Snow','Sunny','Rain'],
    'Temperature':[23,32,23,12]
}
df=pd.DataFrame(weather_data)
weather_data=[
    ('1/1/2017','32','Rain'),
    ('2/1/2017','32','Rain'),
    ('3/1/2017','32','Rain')
]
df=pd.DataFrame(weather_data,columns=['Day','Temperature','Event'])
weather_data=[
    {'Day':'1/1/2017','Temperatue':34,'Event':'Sunny'},
    {'Day':'2/1/2017','Temperatue':34,'Event':'Sunny'},
    {'Day':'3/1/2017','Temperatue':34,'Event':'Sunny'}
]
df=pd.DataFrame(weather_data)