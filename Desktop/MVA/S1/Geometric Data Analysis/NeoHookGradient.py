# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:47:55 2023

@author: yonau
"""

import numpy as np

def neo_hookean_potential(F, mu, lam):
    C = np.dot(F.T, F)

    J = np.linalg.det(F)

    #  Neo-Hookean potential
    psi = (mu / 2) * (np.trace(C) - 3) + (lam / 2)*(J-1)**2

    return psi


F = np.array([[1.2, 0.1, 0.2],
              [0.3, 0.9, 0.4],
              [0.5, 0.6, 1.1]])

mu = 1.0  # Shear modulus
lam = 2.0  # parameter

psi_value = neo_hookean_potential(F, mu, lam)

print("Neo-Hookean potential value:", psi_value)


import sympy as sp


mu, lam = sp.symbols('mu lam')
C11, C22, C33, C12, C23, C31 = sp.symbols('C11 C22 C33 C12 C23 C31')
J = sp.symbols('J')
F = sp.Matrix([[C11, C12, C31],
               [C12, C22, C23],
               [C31, C23, C33]])

# Define Neo-Hookean potential
Psi = (2 * mu * (sp.trace(F) - 3) - mu * sp.log(J) + lam / 2 * sp.log(J)**2)

# Calculate the gradient of Psi with respect to F
grad_Psi = sp.diff(Psi, F)

# Display the result
print("Gradient of Psi(F):")
print(grad_Psi)
