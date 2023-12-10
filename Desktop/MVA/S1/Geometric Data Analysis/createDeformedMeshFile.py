# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:41:55 2023

@author: yonau
"""

import meshio
import numpy as np

def deform_mesh(initial_points, deformation_matrix):
    # Apply the deformation matrix F to the initial points
    deformed_points = np.dot(initial_points, deformation_matrix.T)
    return deformed_points

def write_deformed_mesh(initial_file, deformed_file, deformation_matrix):
    # Read the initial configuration
    mesh = meshio.read(initial_file)
    points = mesh.points
    cells = mesh.cells

    # Apply the deformation to the mesh nodes
    deformed_points = deform_mesh(points, deformation_matrix)

    # Create a new mesh with deformed points
    deformed_mesh = meshio.Mesh(points=deformed_points, cells=cells)

    # Write the deformed mesh to a new .msh file
    meshio.write(deformed_file, deformed_mesh, file_format='gmsh22')

# Example usage:
initial_file = "C:/Users/yonau/Downloads/tremble-master/tremble-master/geo/simple_2.msh"
deformed_file = 'deformed_mesh.msh'
deformation_matrix = np.array([[1.2, 0.1, 0.2],
                               [0.3, 0.9, 0.4],
                               [0.5, 0.6, 1.1]])

write_deformed_mesh(initial_file, deformed_file, deformation_matrix)
