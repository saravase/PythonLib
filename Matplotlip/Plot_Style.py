# import library
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('grayscale') # 'classic','seaborn','ggplot','bmh','grayscale'
print(mpl.style.available)

# Customize Data
x=np.linspace(-2.0*np.pi, 2.0*np.pi,201)
y=np.sin(x)
z=np.cos(x)

#Plot Datas
plt.plot(x,y,color="r",label="Sin")
plt.plot(x,z,color="g",label="Cos")
plt.xlabel("Angle")
plt.ylabel("Magnitude")
plt.title("Sin Curve")
plt.legend()
plt.grid()
plt.show()