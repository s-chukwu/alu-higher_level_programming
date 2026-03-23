#!/usr/bin/python3
"""Module to solve the N Queens puzzle."""
import sys


def solve_nqueens(n, row, queens, solutions):
    """Recursively find all non-attacking queen positions.

    Args:
        n (int): size of the board.
        row (int): current row being evaluated.
        queens (list): positions of queens already placed.
        solutions (list): collection of all valid solutions found.
    """
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(queens)])
        return

    for col in range(n):
        if is_safe(row, col, queens):
            queens.append(col)
            solve_nqueens(n, row + 1, queens, solutions)
            queens.pop()


def is_safe(row, col, queens):
    """Check if a queen can be placed at (row, col).

    Args:
        row (int): current row.
        col (int): current column.
        queens (list): positions of existing queens.

    Returns:
        bool: True if safe, False otherwise.
    """
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def main():
    """Handle command line arguments and execute the solver."""
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

    solutions = []
    solve_nqueens(n, 0, [], solutions)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
