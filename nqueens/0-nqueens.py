#!/usr/bin/python3
"""Solves the N queens puzzle using backtracking."""
import sys


def is_safe(board, row, col):
    """Checks if a queen can be placed at board[row] = col."""
    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == col or \
           abs(prev_col - col) == abs(prev_row - row):
            return False
    return True


def solve(board, row, n):
    """Places queens row by row and prints each full solution."""
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve([0] * n, 0, n)
