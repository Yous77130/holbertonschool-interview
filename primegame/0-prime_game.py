#!/usr/bin/python3
"""Determine le gagnant du Prime Game (Maria vs Ben)."""


def isWinner(x, nums):
    """Retourne le joueur qui gagne le plus de manches.

    Args:
        x: nombre de manches.
        nums: liste des valeurs de n (une par manche).

    Returns:
        'Maria', 'Ben', ou None si egalite.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)

    # Crible d'Eratosthene : compter les nombres premiers jusqu'a chaque n.
    # sieve[i] = True si i est premier.
    sieve = [True] * (max_n + 1)
    sieve[0] = False
    if max_n >= 1:
        sieve[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_n + 1, i):
                sieve[multiple] = False

    # prime_count[n] = nombre de premiers <= n.
    prime_count = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Si le nombre de premiers <= n est impair, Maria gagne, sinon Ben.
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
