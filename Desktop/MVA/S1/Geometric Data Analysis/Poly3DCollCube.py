# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 15:19:38 2023

@author: yonau
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_muscle_contraction(t):
    # Fonction pour afficher un cube ressemblant à un muscle en contraction

    # Coordonnées des sommets du cube
    vertices = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1],
    ]

    # Faces du cube
    faces = [
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[3], vertices[0], vertices[4], vertices[7]],
        [vertices[0], vertices[3], vertices[2], vertices[1]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
    ]

    # Créer une figure 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Afficher le maillage
    mesh = Poly3DCollection(faces, alpha=0.5, edgecolor='k')
    ax.add_collection3d(mesh)

    # Définir les étiquettes des axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Titre de la figure
    ax.set_title(f'Muscle Contraction at t={t}')

    # Afficher le maillage
    plt.show()

# Exemple d'appel avec un instant de temps t
plot_muscle_contraction(t=0.8)
