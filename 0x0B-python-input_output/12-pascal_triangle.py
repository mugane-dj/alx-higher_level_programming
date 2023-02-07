#!/usr/bin/python3

"""Defines the Pascal Trinagle module"""


def pascal_triangle(n):
    """Gets a list of lists of integers representing the Pascal's triangle"""

    output = [[1]]
    if n <= 0:
        return []

    while len(output) != n:
        a = output[-1]
        tmp = [1]
        for i in range(len(a) - 1):
            tmp.append(a[i] + a[i + 1])
        tmp.append(1)
        output.append(tmp)
    return output
