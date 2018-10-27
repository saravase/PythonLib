# import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Customize data
x=np.linspace(0,2*np.pi,101)
c,s=np.cos(x),np.sin(x)
plt.plot(x,c,c='r',label="Cos")
plt.plot(x,s,c='g',label="Sin")
plt.plot(np.pi*0.5,np.sin(np.pi*0.5),'bo')
plt.plot(np.pi*1.5,np.sin(np.pi*1.5),'ko')
plt.annotate(s="Maxima",
             xy=(np.pi*0.5,np.sin(np.pi*0.5)),
             xytext=(np.pi*1.0,np.sin(np.pi*0.5)),
             arrowprops=dict(facecolor='blue',shrink=.5)
             )
plt.annotate(s="Minima",
             xy=(np.pi*1.5,np.sin(np.pi*1.5)),
             xytext=(np.pi*1.5-0.5,np.sin(np.pi*1.5)+0.5),
             arrowprops=dict(facecolor='blue',shrink=.5)
             )   
plt.title("Cos And Sine Curve")
plt.legend()
plt.grid()
plt.show()