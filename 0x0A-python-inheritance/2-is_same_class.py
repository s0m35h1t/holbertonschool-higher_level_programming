#!/usr/bin/python3


def is_same_class(obj, a_class):
    """check object is exactly an instance of the specified class

    Args:
        obj (object):
        a_class (object class):

    Returns: Bool
    """
    return type(obj) == a_class
