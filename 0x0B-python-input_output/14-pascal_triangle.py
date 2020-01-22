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
    if n <= 0:
        return []

    tri_pas = [[1]]
    for i in range(1, n):
        row_list = [1]
        for iteration in range(1, i):
            row_list.append(
                tri_pas[i - 1][iteration - 1] + tri_pas[i - 1][iteration])
        row_list.append(1)
        tri_pas.append(row_list)
    return tri_pas
