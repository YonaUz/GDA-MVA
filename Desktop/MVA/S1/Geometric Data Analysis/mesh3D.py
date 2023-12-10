# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 23:34:51 2023

@author: yonau
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import meshio

# Load the mesh from the .msh file
# mesh = meshio.read("C:/Users/yonau/Downloads/tremble-master/tremble-master/geo/simple_2.msh")
mesh = meshio.read("C:/Users/yonau/Downloads/tremble-master/tremble-master/geo/simple_muscle_3d.msh")
# mesh = meshio.read("C:/Users/yonau/Desktop/MVA/S1/Geometric Data Analysis/deformed_mesh.msh")

# Extract triangle information
triangles = mesh.cells_dict["triangle"].data

# Plot the mesh in 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(mesh.points[:, 0], mesh.points[:, 1], mesh.points[:, 2], triangles=triangles, cmap="viridis")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Mesh Plot")
plt.show()
