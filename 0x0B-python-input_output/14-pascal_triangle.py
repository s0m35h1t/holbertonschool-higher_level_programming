#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """ representing the Pascal’s triangle of n

    Args:
        n (int): file name
    Returns:
        (list of lists)
    """
    tri_pas = []
    if n <= 0:
        return tri_pas
    for i in range(n):
        value = 1
        row_list = [1]
        for iteration in range(i):
            value = value * (i - iteration) * 1 / (iteration + 1)
            row_list.append(int(value))
        tri_pas.append(row_list)

    return tri_pas
