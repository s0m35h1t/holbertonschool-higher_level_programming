#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module functions: add_integer(a, b).
"""


def add_integer(a, b=98):
    """
    add_integer: adds 2 integers
    Args:
        a (int, float): first number
        b (int, float): second number
    Returns:
        int
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
