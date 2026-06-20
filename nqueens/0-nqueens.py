#!/usr/bin/python3
"""Solves the N-Queens puzzle and prints all valid placements."""
import sys


def is_safe(row, col, queens):
    """Checks if placing a queen at (row, col) is safe from attacks."""
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_nqueens(n, row, queens, solutions):
    """Recursively places queens row by row to find all valid solutions."""
    if row == n:
        solution = [[i, queens[i]] for i in range(n)]
        print(solution)
        return

    for col in range(n):
        if is_safe(row, col, queens):
            queens.append(col)
            solve_nqueens(n, row + 1, queens, solutions)
            queens.pop()

def main():
    """Parses CLI arguments and launches the N-Queens solver."""
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

    solve_nqueens(n, 0, [], [])


if __name__ == "__main__":
    main()
