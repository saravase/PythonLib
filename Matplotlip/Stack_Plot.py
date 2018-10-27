# import library
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('classic')

# Custimize datd
N=11
lim1=0
lim2=10
years=np.linspace(2000,2010,N,dtype=np.int64)
expense1=np.random.randint(lim1,lim2,N)
expense2=np.random.randint(lim1,lim2,N)
expense3=np.random.randint(lim1,lim2,N)
expense4=np.random.randint(lim1,lim2,N)
expense5=np.random.randint(lim1,lim2,N)
expenses=[expense1,expense2,expense3,expense4,expense5]
Labels=['Educaion','Medicine','Food','Infrastructure','Defence']
Colurs=['red','green','blue','orange','yellow']

# plot stack plot
# plt.stackplot(years,expense1,colors=["green"],labels=['Education'])
#plt.stackplot(years,expense1,expense2,expense3,expense4,expense5,colors=Colurs,labels=Labels)
plt.stackplot(years,expenses,colors=Colurs,labels=Labels)
plt.xlabel('Years')
plt.ylabel('Expenses')
plt.title('{} city past {} years {} stack plot graph'.format('Coimbatore',N,'expenses'))
plt.grid()
plt.legend()
plt.show()