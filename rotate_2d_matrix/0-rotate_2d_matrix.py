#!/usr/bin/python3
"""Rotate a square 2D matrix 90 degrees clockwise in place."""


def rotate_2d_matrix(matrix):
    """Rotate an n x n matrix 90 degrees clockwise without a copy.

    Each square ring is handled from the outside in. Inside a ring, four
    cells trade places at once: left -> top -> right -> bottom -> left.
    """
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
