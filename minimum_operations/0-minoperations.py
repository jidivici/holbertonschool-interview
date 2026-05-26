#!/usr/bin/python3
"""Module to calculate minimum operations to reach n H characters."""


def minOperations(n):
    """Return minimum operations to get n H chars using Copy All and Paste."""
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
