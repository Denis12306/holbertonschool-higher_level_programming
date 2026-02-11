#!/usr/bin/python3
"""A function that returns a list of lists of integers representing
the Pascal's triangle of n"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            line = [1]
        else:
            prev = triangle[i - 1]
            line = [1]
            for j in range(1, len(prev)):
                line.append(prev[j - 1] + prev[j])
            line.append(1)
        triangle.append(line)

    return triangle
