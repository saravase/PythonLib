# import libsrary
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')

# Customize data
range_vals=np.linspace(0,100,11)
counts1=np.random.rand(10)*4.0
counts2=np.random.rand(10)*8.0
counts3=np.random.rand(10)*2.0
errors=np.ones(10)*0.5
barwidth=1.0
groups=['g01','g02','g03','g04','g05','g06','g07','g08','g09','g10','g11',]

# mid_vals
# mid_vals=(range_vals[0:-1]+range_vals[1:])*0.5 # for default style
mid_vals=(range_vals[0:-1]+range_vals[1:])*0.5-barwidth*0.5 # for classic style

# plot bar chart
# plt.bar(mid_vals,counts1)
# plt.bar(mid_vals,counts1,facecolor='pink',width=barwidth,label="Sample bar chart")
plt.bar(mid_vals,counts1,facecolor='pink',width=barwidth,label="Sample bar chart 1",yerr=errors)
plt.bar(mid_vals+1,counts2,facecolor='orange',width=barwidth,label="Sample bar chart 2",yerr=errors)
plt.bar(mid_vals+2,counts3,facecolor='yellow',width=barwidth,label="Sample bar chart 3",yerr=errors)
plt.xlabel("Values")
plt.ylabel("Counts")
plt.title("Bar Chart")
# plt.xticks(mid_vals) # for default style
plt.xticks(mid_vals+barwidth*1.5,groups,rotation='45') # for classic style
plt.legend()
plt.grid()
plt.show()