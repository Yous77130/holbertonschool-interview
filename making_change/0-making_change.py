#!/usr/bin/python3
"""Module de résolution du problème de rendu de monnaie (making change)."""


def makeChange(coins, total):
    """Retourne le nombre minimal de pièces pour atteindre total.

    Args:
        coins: liste des valeurs de pièces disponibles (nombre infini de chaque).
        total: montant à atteindre.

    Returns:
        Le nombre minimal de pièces, 0 si total <= 0, -1 si impossible.
    """
    if total <= 0:
        return 0

    count = 0
    remaining = total
    # On commence par les plus grosses pièces (approche gloutonne).
    for coin in sorted(coins, reverse=True):
        if remaining == 0:
            break
        # Combien de pièces de cette valeur tiennent dans le reste ?
        count += remaining // coin
        remaining %= coin

    if remaining != 0:
        return -1
    return count
