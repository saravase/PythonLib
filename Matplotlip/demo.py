import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2.0*np.pi,num=200)
y=np.sin(x)
plt.plot(x,y)
plt.show()
