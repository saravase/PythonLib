# import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Customize data
x=np.linspace(0,2*np.pi,201)
c,s=np.cos(x),np.sin(x)
plt.plot(x,c,c='r',label="Cos")
plt.plot(x,s,c='g',label="Sin")
# plt.fill_between(x,1,s)
# plt.fill_between(x,1,c)
# plt.fill_between(x,0,s)
# plt.fill_between(x,0,c)
# plt.fill_between(x,-1,s)
# plt.fill_between(x,-1,c)
# plt.fill_between(x,c,s,color='orange',alpha=1)
plt.fill_between(x[20:50],c[20:50],s[20:50],color='orange',alpha=1)
# plt.fill_between(x,c,s,where=s>=c,color='orange',alpha=1)
# plt.fill_between(x,c,s,where=c>=s,color='red',alpha=1)
# plt.fill_between(x,c,s,color='orange',alpha=1)
plt.fill_between(x,c,s,where=s>=c,color='orange',alpha=1,interpolate=True)
plt.fill_between(x,c,s,where=c>=s,color='red',alpha=1,interpolate=True)
plt.title("Cos And Sine Curve")
plt.legend()
plt.grid()
plt.show()