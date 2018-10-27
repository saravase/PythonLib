# import library
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')

# Customize data
N=100
x=np.linspace(-2.0*np.pi , 2.0*np.pi,N)
y=np.random.normal(0,1,N)+np.sin(x)

# Draw scatter plot
# plt.scatter(x,y)
# plt.scatter(x,y,label="sine scatter",marker="*",c="yellow")
plt.scatter(x,y,label="sine scatter",marker="*",c="yellow",s=150,edgecolors="red",alpha=0.9,linewidths=1.5)


plt.xlabel('Angles')
plt.ylabel('Plot')
plt.title('Sctter plot')
plt.legend()
plt.grid()
plt.show()