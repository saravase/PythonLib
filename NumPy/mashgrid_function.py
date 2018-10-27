# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 12:09:27 2018

@author: ADMIN
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-4,4,9)
y=np.linspace(-5,5,11)
xx,yy=np.meshgrid(x,y)

#Elipse
elipse=xx**2+4.0*yy**2.0
plt.contourf(xx,yy,elipse,cmap='jet')
plt.colorbar()
plt.show()

random_data=np.random.random((11,9))
plt.contourf(xx,yy,random_data,cmap='jet')
plt.colorbar()
plt.show()

xx1,yy1=np.meshgrid(x,y,indexing='ij')
np.all(xx==xx1.T)
np.all(yy==yy1.T)