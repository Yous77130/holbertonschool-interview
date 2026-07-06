#!/usr/bin/python3
"""Module de résolution du problème de rendu de monnaie (making change)."""


def makeChange(coins, total):
    """Retourne le nombre minimal de pièces pour atteindre total.

    Approche par programmation dynamique (toujours optimale).

    Args:
        coins: liste des valeurs de pièces (nombre infini de chaque).
        total: montant à atteindre.

    Returns:
        Le nombre minimal de pièces, 0 si total <= 0, -1 si impossible.
    """
    if total <= 0:
        return 0

    # dp[i] = nombre minimal de pièces pour atteindre le montant i.
    # On initialise à total + 1 (valeur "infinie" impossible à atteindre).
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
