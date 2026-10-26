#!/usr/bin/python3
"""Solve the N queens puzzle and print every solution."""
import sys


def solve(n, columns, solutions):
    """Place a queen on the next row, saving the board when all rows are done.

    columns[i] is the column of the queen on row i. A square is free when no
    earlier queen shares its column or one of its two diagonals.
    """
    row = len(columns)
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(columns)])
        return
    for col in range(n):
        free = True
        for prev_row in range(row):
            prev_col = columns[prev_row]
            if prev_col == col or abs(prev_col - col) == row - prev_row:
                free = False
                break
        if free:
            columns.append(col)
            solve(n, columns, solutions)
            columns.pop()


def main():
    """Read N from the arguments, then print every solution on its own line."""
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
    solve(n, [], solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
