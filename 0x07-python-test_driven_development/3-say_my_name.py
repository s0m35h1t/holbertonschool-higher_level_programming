#!/usr/bin/python3
"""
This is the "3-say_my_name" module.

The 0-add_integer module functions: say_my_name(first_name, last_name="").
"""


def say_my_name(first_name, last_name=""):
    """
    add_integer: prints My name is <first name> <last name>
    Args:
        a (str): first name
        b (str): last name
    Returns:
        None
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
