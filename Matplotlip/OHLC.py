import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import dates,ticker
from matplotlib.finance import candlestick_ohlc
import csv

mpl.style.use('default')
fname='data.csv'

#Empty list
date_data=[]
open_data=[]
high_data=[]
low_data=[]
close_data=[]
trade=[]
turn=[]

# Extracting data
with open(fname,'r') as csvfile:
    data=csv.reader(csvfile,delimiter=',')
    for line in data:
        date_data.append(line[0])
        open_data.append(line[1])
        high_data.append(line[2])
        low_data.append(line[3])
        close_data.append(line[4])
        trade.append(line[5])
        turn.append(line[6])

# Conversion to numpy arrays
open_val=np.array(open_data[1:],dtype=np.float64)
high_val=np.array(high_data[1:],dtype=np.float64)
low_val=np.array(low_data[1:],dtype=np.float64)
close_val=np.array(close_data[1:],dtype=np.float64)
trade_val=np.array(trade[1:],dtype=np.float64)
turn_val=np.array(turn[1:],dtype=np.float64)

date_val=[]
for date in date_data[1:]:
    new_date=dates.datestr2num(date)
    date_val.append(new_date)

# Creating ohlc_data
ohlc_data=[]
i=0
while i <len(date_val):
    first_day=date_val[i],open_val[i],high_val[i],low_val[i],close_val[i]
    ohlc_data.append(first_day)
    i+=1

#Day formatter for x lables
dayFormatter=dates.DateFormatter('%d-%b-%Y')

fig,ax1=plt.subplots()
candlestick_ohlc(ax1,ohlc_data,width=1.0,colorup='g',colordown='r',alpha=0.8)
# plt.plot(date_val,open_val)
# plt.plot(date_val,close_val)
# plt.plot(date_val,high_val)
# plt.plot(date_val,low_val)

ax1.xaxis.set_major_formatter(dayFormatter)
ax1.xaxis.set_major_locator(ticker.MaxNLocator(10))
plt.xticks(rotation=30)
plt.grid()
plt.xlabel("Date")
plt.ylabel("NSE Index")
plt.title("Historical Data for NIFTY")
plt.tight_layout()
plt.show()



