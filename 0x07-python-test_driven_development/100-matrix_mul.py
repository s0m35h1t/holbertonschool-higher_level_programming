#!/usr/bin/python3
"""
This is the "6-max_integer_test.py" module.

The 0-add_integer module functions: matrix_mul(m_a, m_b).
"""


def get_matrix_size(matrix, mat_name):
    if len(matrix) == 0:
        msg = mat_name + " can't be empty"
        raise ValueError(msg)
    size = None
    for mat in matrix:
        if type(mat) is not list:
            msg = mat_name + " must be a list of lists"
            raise TypeError(msg)
        if len(mat) == 0:
            msg = mat_name + " can't be empty"
            raise ValueError(msg)
        if size is None:
            size = len(mat)
        elif size != len(mat):
            msg = "each row of " + mat_name + " must be of the same size"
            raise TypeError(msg)
        for i in mat:
            if type(i) is not int and type(i) is not float:
                msg = mat_name + " should contain only integers or floats"
                raise TypeError(msg)
    return size


def matrix_mul(m_a, m_b):
    """
    print_square: prints a square with the character #.
    Args:
        size (int): multiplies 2 matrices
    Returns:
        list of lists
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    size_ma = get_matrix_size(m_a, "m_a")
    size_mb = get_matrix_size(m_b, "m_b")
    if size_ma != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(size_mb):
            n = 0
            for k in range(len(m_b)):
                n += m_a[i][k] * m_b[k][j]
            row.append(n)
        matrix.append(row)
    return matrix
