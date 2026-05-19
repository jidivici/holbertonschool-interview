#!/usr/bin/python3
"""
Module for generating Pascal's triangle.

This module provides a function to compute Pascal's triangle
up to a given number of rows.
"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle up to n rows."""
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
