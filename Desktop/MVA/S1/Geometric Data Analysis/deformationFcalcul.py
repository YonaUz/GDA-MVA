# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:32:35 2023

@author: yonau
"""

import meshio
import numpy as np
from scipy.optimize import minimize

def read_mesh(file_path):
    # Read .msh file
    mesh = meshio.read(file_path)
    points = mesh.points
    cells = mesh.cells_dict['tetra']  # Assuming tetrahedral elements

    return points, cells

def objective_function(displacement, initial_points, deformed_points):
    # Reshape the displacement vector to a matrix
    F = np.eye(3) + displacement.reshape((3, -1))

    # Compute the deformed points using the current deformation matrix F
    deformed_points_current = np.dot(initial_points, F.T)

    # Calculate the error between the deformed points and the target deformed points
    error = np.sum((deformed_points_current - deformed_points)**2)

    return error

def calculate_deformation_matrix(initial_file, deformed_file):
    # Read the initial and deformed configurations
    initial_points, _ = read_mesh(initial_file)
    deformed_points, _ = read_mesh(deformed_file)

    # Initial guess for the displacement
    displacement_initial_guess = np.zeros(9)

    # Optimize the deformation matrix F using scipy's minimize function
    result = minimize(objective_function, displacement_initial_guess,
                      args=(initial_points, deformed_points),
                      method='L-BFGS-B')  # You can choose a different optimization method if needed

    # Extract the optimized displacement
    optimal_displacement = result.x

    # Reshape the displacement vector to a 3x3 matrix (deformation gradient matrix F)
    F = np.eye(3) + optimal_displacement.reshape((3, -1))

    return F

# Example usage:
initial_file = "C:/Users/yonau/Downloads/tremble-master/tremble-master/geo/simple_2.msh"
deformed_file = "C:/Users/yonau/Desktop/MVA/S1/Geometric Data Analysis/deformed_mesh.msh"

deformation_matrix = calculate_deformation_matrix(initial_file, deformed_file)
print("Deformation Gradient Matrix F:")
print(deformation_matrix)
