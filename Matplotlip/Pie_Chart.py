# import library
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('default')

# Customize data
Distors=['Apple','Mango','Graphs','Orange','PineApple','Strawberry','Lemon','Pomagranate','sappotta','perry']
Colurs=['pink','yellow','green','orange','red','blue','magenta','grey','purple','aqua']
Users=np.array([234,423,21,543,64,756,552,90,167,789])
Explodes=np.zeros(10)
Explodes[1]=0.5

# plt.pie(Users,labels=Distors)

plt.axis([-1.5,1.5,-1.5,1.5])
# plt.pie(Users,
#         labels=Distors,
#         colors=Colurs,
#         startangle=90,
#         shadow=True,
#         radius=2.0,
#         explode=Explodes,
#         autopct='%2.2f%%',
#         pctdistance=0.6,
#         labeldistance=1.2,
#         counterclock=False,
#         frame=True
#         )

def make_autopct(values):
    def my_autopct(pct):   # pct means percentage
        total=sum(values)  # total value of the values
        val=int(round(pct*total/100.0)) # prdict the actual value
        return '{p:.2f}% ({v:d})'.format(p=pct,v=val)
    return my_autopct

plt.pie(Users,
        labels=Distors,
        colors=Colurs,
        startangle=90,
        shadow=True,
        radius=2.0,
        explode=Explodes,
        autopct=make_autopct(Users),
        pctdistance=0.6,
        labeldistance=1.2,
        counterclock=False,
        frame=True
        )

plt.title("Fruits Users")
# plt.axes(aspect=1)
plt.axis('equal')
plt.show()