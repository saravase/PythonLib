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
barwidth=5.0
groups=['g01','g02','g03','g04','g05','g06','g07','g08','g09','g10','g11',]

# mid_vals
# mid_vals=(range_vals[0:-1]+range_vals[1:])*0.5 # for default style
mid_vals=(range_vals[0:-1]+range_vals[1:])*0.5 # for classic style

# plot bar chart
plt.barh(mid_vals,counts1,facecolor='pink',align="center",height=barwidth,label="Sample bar chart 1",xerr=errors)
plt.barh(mid_vals,counts2,left=counts1,facecolor='orange',align="center",height=barwidth-1,label="Sample bar chart 2",xerr=errors)
plt.barh(mid_vals,counts3,left=counts1+counts2,facecolor='red',align="center",height=barwidth-2,label="Sample bar chart 2",xerr=errors)
plt.xlabel("Values")
plt.ylabel("Counts")
plt.title("Bar Chart")
# plt.yticks(mid_vals) # for default style
plt.yticks(mid_vals,groups,rotation='45') # for classic style
plt.legend()
plt.grid()
plt.show()
