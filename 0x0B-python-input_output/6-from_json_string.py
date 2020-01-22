#!/usr/bin/python3
"""
from string to JSON
"""
import json


def from_json_string(my_obj):
    """object (Python data structure) represented by a JSON string

    Args:
        my_obj (Object str): string to transform
    Returns:
        (Object)
    """
    return json.loads(my_obj)
