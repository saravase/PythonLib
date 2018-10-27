# import libsrary
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')

mean=100
sd=15
binsize=20
n=1000
IQ=np.random.normal(mean,sd,n)

count, bins, extras=plt.hist(IQ,binsize,facecolor='orange',label='IQ',normed=False)
print(bins[1:])
plt.plot(bins[1:],count,label="series",color="green")
plt.xlabel("IQ")
plt.ylabel("Count")
plt.title("IQ Distrubution Histogram")
plt.xticks(bins)
plt.grid(True)
plt.legend()
plt.show() 