#!/usr/bin/python3
"""Module that defines Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle of size n."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev = triangle[-1]

        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])

        row.append(1)
        triangle.append(row)

    return triangle
