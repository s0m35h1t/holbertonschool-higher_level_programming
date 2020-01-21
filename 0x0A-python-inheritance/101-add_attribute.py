#!/usr/bin/python3


def add_attribute(cl, name, value):
    try:
        setattr(cl, name, value)
    except Exception:
        raise TypeError("can't add new attribute")
