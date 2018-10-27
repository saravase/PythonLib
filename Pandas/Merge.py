#import library
import pandas as pd
df1=pd.DataFrame({
    'city':['Kerala','Tamilnadu','Karnataka','Andra'],
    'Temperature':[54,76,98,87]
})
df2=pd.DataFrame({
    'city':['Tamilnadu','Kerala','Karnataka','Andra'],
    'Temperature':[65,45,97,54]
})
print(df1)