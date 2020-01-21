#!/usr/bin/python3


def inherits_from(obj, a_class):
    """the object is an instance of a class that inherited (directly or indirectly)
    from the specified class

    Args:
        obj (object):
        a_class (object class):

    Returns: None
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
