# import library
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('default')

#Parameters
n = 2001
f = np.pi
r = 5.0

#Data
theta=np.linspace(0,30.0*np.pi,n)
curve1=r*np.cos(f*theta)
curve2=r*np.sin(f*theta)

#Get an axex handle/object
ax1=plt.subplot(111,polar=True)

#Plot the figure
ax1.plot(theta,curve1,color='red',label="rose surve1")
ax1.plot(theta,curve2,color='orange',label="rose surve2")

## Main tweaks
# Radius limits
ax1.set_ylim(-6,6)

# Radius ticks
ax1.set_yticks(np.linspace(-6,6,7))

# Radius tick position in degrees
ax1.set_rlabel_position(270)

# Angle ticks
ax1.set_xticks(np.linspace(0,2.0*np.pi,17)[:-1])

# Additional Tweaks
plt.grid(True)
plt.legend()
plt.title("Rose plots")
plt.show()
