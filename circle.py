import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
#import scipy as sc
#import numpy as np
x=float(input())
y=float(input())
radius=float(input())
circle = plt.Circle((x,y),radius)
#circle = plt.Circle((0.1,0.1), 0.3)

fig, ax= plt.subplots()
#ax=plt.gca()
ax.add_artist(circle)
ax.set_xlim((-10,10))
ax.set_ylim((-10,10))
plt.show()
fig.savefig('circle1.png')
