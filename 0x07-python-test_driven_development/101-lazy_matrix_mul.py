#!/usr/bin/python3
"""
This is the "101-lazy_matrix_mul.py" module.

The 101-lazy_matrix_mul module functions: \
    lazy_matrix_mul(first_name, last_name="").
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    azy_matrix_mul: multiplies 2 matrices by using the module NumPy
    Args:
        m_a (list of lists): first matrice
        m_b (list of lists): second matrice
    Returns:
        matrice
    """
    return np.matmul(m_a, m_b)
