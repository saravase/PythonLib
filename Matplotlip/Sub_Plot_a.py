# import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')

# Customize data
n=201
x=np.linspace(0,4.0*np.pi,n)
y1=np.sin(x)
y2=np.cos(x)
y3=y1+y2

# Plot graph
plt.figure()

# Plot -1  - sine curve
plt.subplot(311)
plt.plot(x,y1,c='red',linestyle='-',label='Sine')
plt.ylabel('Magnitude')
plt.title('Sine Curve')
plt.grid()
plt.legend()
# Plot -2  - cosine curve

plt.subplot(312)
plt.plot(x,y2,c='green',linestyle='-',label='Cosine')
plt.ylabel('Magnitude')
plt.title('Cosine Curve')
plt.grid()
plt.legend()
# Plot -3  - sinecosine curve

plt.subplot(313)
plt.plot(x,y3,c='blue',marker='o',label='Sine+Cosine')
plt.xlabel('Angle')
plt.title('SineCosine Curve')
plt.ylabel('Magnitude')
plt.grid()
plt.legend()
plt.show()