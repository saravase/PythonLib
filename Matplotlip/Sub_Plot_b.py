# import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')

# Customize data
n=101
x=np.linspace(0,4.0*np.pi,n)
y1=np.sin(x)
y2=np.cos(x)
r=np.random.random(n)

# Plot graph
fig=plt.figure(figsize=(100,80))

# Plot -1

ax1=fig.add_subplot(121)
ax1.scatter(x,r,color='orange',marker='*',label="random scatter")
ax1.set_title('Random Scatter')
ax1.set_xlabel('Angle',color='g')
ax1.set_ylabel('Magnitude',color='g')
ax1.tick_params(axis='x',colors='red')
ax1.tick_params(axis='y',colors='aqua')
ax1.grid()
ax1.legend()

# Plot -2

ax2=fig.add_subplot(322)
ax2.scatter(x,y1,color='orange',marker='*',label="random scatter")
ax2.set_title('Sine')
ax2.set_xlabel('Angle',color='g')
ax2.set_ylabel('Magnitude',color='g')
ax2.grid(True)
ax2.legend()

# Plot -3

ax3=fig.add_subplot(324)
ax3.scatter(x,y2,color='green',marker='*',label="random scatter")
ax3.set_title('Cosine')
ax3.set_xlabel('Angle',color='r')
ax3.set_ylabel('Magnitude',color='r')
ax3.grid(True)
ax3.legend()

# Plot -4

ax4=fig.add_subplot(326)
ax4.scatter(x,y1+y2,color='blue',marker='*',label="random scatter")
ax4.set_title('Sine+Cosine')
ax4.set_xlabel('Angle',color='r')
ax4.set_ylabel('Magnitude',color='r')
ax4.grid(True)
ax4.legend()

plt.tight_layout()
plt.subplots_adjust(top=0.94)
plt.savefig('sub_plot.png',format='png',dpi=400)
plt.show()
