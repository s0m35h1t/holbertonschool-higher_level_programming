#!/usr/bin/python3
"""
get __dict__ class description
"""


def class_to_json(obj):
    """returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj (Object): file name
    Returns:
        (Object) : dict
    """
    return obj.__dict__
