# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 15:17:12 2023

@author: yonau
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

X = [0, 1, 1, 0]
Y = [0, 0, 1, 1]
Z = [0, 1, 0, 1]
triangles = [[0, 1, 2], [1, 2, 3]]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

mesh = Poly3DCollection([[(X[i], Y[i], Z[i]) for i in triangle] for triangle in triangles], alpha=0.5, edgecolor='k')
ax.add_collection3d(mesh)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
