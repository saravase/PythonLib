import numpy as np
import matplotlib.pyplot as mpl

x=np.linspace(0,2*np.pi,200)
y=np.sin(x)
z=np.cos(x)

xnumbers=np.linspace(0,7,15)
ynumbers=np.linspace(-1,1,11)

mpl.plot(x,y,'r',x,z,'g')
mpl.xlabel("Angle in Radius")
mpl.ylabel("Magnitude")
mpl.title("Sine Curve")
mpl.xticks(xnumbers)
mpl.yticks(ynumbers)
mpl.axis([0,6.5,-1.1,1.1])
mpl.grid()
mpl.legend(['Sin','Cos'])
mpl.show()