#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix) -> None:
    """Rotates an n x n 2D matrix 90 degrees clockwise, in-place."""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for row in matrix:
        row.reverse()
