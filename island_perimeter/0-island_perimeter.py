#!/usr/bin/python3
"""Compute the perimeter of the island in a grid."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid.

    Every land cell brings 4 sides. When two land cells touch, the side
    they share is not on the coast, and it was counted once for each of
    them, so 2 is taken away. Looking only up and left counts each shared
    side exactly once.
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != 1:
                continue
            perimeter += 4
            if row > 0 and grid[row - 1][col] == 1:
                perimeter -= 2
            if col > 0 and grid[row][col - 1] == 1:
                perimeter -= 2
    return perimeter
