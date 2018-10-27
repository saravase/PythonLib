import numpy as np
import matplotlib.pyplot as mpl

x=np.linspace(0,2.0*np.pi,101)
y=np.sin(x)
z=np.sinh(x)

xnumbers=np.linspace(0,7,15)
ynumbers1=np.linspace(-1,1,11)
ynumbers2=np.linspace(0,300,7)

fig,ax1=mpl.subplots()
ax2=ax1.twinx()

curve1,=ax1.plot(x,y,color="red",label="Sin")
curve2,=ax2.plot(x,z,color="green",label="SinH")

# set legend
curves=[curve1,curve2]
# ax1.legend()
# ax2.legend()
ax1.legend(curves,[curve.get_label() for curve in curves])
# ax2.legend(curves,[curve.get_label() for curve in curves]) # Does not work

# set x axis label
ax1.set_xlabel("Angle" ''',color=curve1.get_color()''')
# ax2.set_xlabel("Angle",color=curve1.get_color()) # Does not work

# set y axis label
ax1.set_ylabel("Magnitude" ''',color=curve1.get_color()''')
ax2.set_ylabel("Magnitude" ''',color=curve2.get_color()''')

# x axis ticks via the axes
# ax1.tick_params(axis='x',colors=curve1.get_color())
# ax2.tick_params(axis='x',colors=curve2.get_color()) # Does not work

# y axis ticks via the axes
# ax1.tick_params(axis='y',colors=curve1.get_color())
# ax2.tick_params(axis='y',colors=curve2.get_color())


# Alternate Approach
# Set xaxis label
ax1.xaxis.label.set_color(curve1.get_color())

# Set yaxis label
ax1.yaxis.label.set_color(curve1.get_color())
ax2.yaxis.label.set_color(curve2.get_color())

#Set xticks
ax1.set_xticks(xnumbers)
# ax2.set_xticks(xnumbers) # This is also work

#Set yticks
ax1.set_yticks(ynumbers1)
ax2.set_yticks(ynumbers2)

ax1.grid(color=curve1.get_color())

ax1.grid(color=curve2.get_color())
ax2.grid(color=curve2.get_color())

mpl.title("Sine and SinH")
mpl.show()
