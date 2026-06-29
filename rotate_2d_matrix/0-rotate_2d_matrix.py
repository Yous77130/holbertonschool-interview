#!/usr/bin/python3
"""Module pour faire pivoter une matrice 2D de 90° dans le sens horaire."""


def rotate_2d_matrix(matrix):
    """Fait pivoter une matrice n x n de 90° sens horaire, sur place.

    Args:
        matrix: liste de listes (matrice carrée) modifiée directement.
    """
    n = len(matrix)

    # Étape 1 : transposer (échanger lignes et colonnes)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Étape 2 : inverser chaque ligne
    for row in matrix:
        row.reverse()
