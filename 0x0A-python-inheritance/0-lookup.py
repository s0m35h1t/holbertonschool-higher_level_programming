#!/usr/bin/python3


def lookup(obj):
    """the list of available attributes and methods of an object

    Args:
        obj (object): object

    Returns: list
    """
    return dir(obj)
