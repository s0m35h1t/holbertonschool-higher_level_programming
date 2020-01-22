#!/usr/bin/python3
"""
write text to a file
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
    the number of characters written

    Args:
        filename (str): file name
        text (int): text to write
    Returns:
        (int)
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
