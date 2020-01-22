#!/usr/bin/python3
"""
number of line of file
"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file

    Args:
        filename (str): file name
    Returns:
        (int)
    """
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)
