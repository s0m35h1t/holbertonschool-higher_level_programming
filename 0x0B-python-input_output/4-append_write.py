#!/usr/bin/python3
"""
append text to file
"""


def append_write(filename="", text=""):
    """append a string to a text file (UTF8) and returns
    the number of characters written

    Args:
        filename (str): file name
        text (int): text to write
    Returns:
        (int)
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
