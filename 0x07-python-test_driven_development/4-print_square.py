#!/usr/bin/python3
"""
This is the "4-print_square.py" module.

The 0-add_integer module functions: say_my_name(first_name, last_name="").
"""


def print_square(size):
    """
    print_square: prints a square with the character #.
    Args:
        size (int): the size length of the square
    Returns:
        None
    """

    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        if type(size) is float:
                raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    for i in range(int(size)):
        for j in range(int(size)):
            print("#", end="")
        print()
