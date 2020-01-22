#!/usr/bin/python3
"""
reads txt file
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it

    Args:
        filename (str): file name
    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
