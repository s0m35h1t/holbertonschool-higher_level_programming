#!/usr/bin/python3
"""
string to JSON
"""
import json


def to_json_string(my_obj):
    """string to JSON representation of an object (string):

    Args:
        my_obj (Object str): string to transform
    Returns:
        (int)
    """
    return json.dumps(my_obj)
