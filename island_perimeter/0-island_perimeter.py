#!/usr/bin/python3
"""Module pour calculer le périmètre d'une île dans une grille."""


def island_perimeter(grid):
    """Retourne le périmètre de l'île décrite dans grid.

    Args:
        grid: liste de listes d'entiers (0 = eau, 1 = terre).

    Returns:
        Le périmètre de l'unique île (entier).
    """
    perimeter = 0
    rows = len(grid)

    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j] == 1:
                # Chaque case de terre apporte 4 côtés au départ.
                perimeter += 4
                # On retire 2 côtés pour chaque voisin de terre adjacent
                # (le côté partagé disparaît des deux côtés).
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
