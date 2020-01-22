#!/usr/bin/python3
"""
load from json file
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    Args:
        filename (str): file name
    Returns:
        (Object)
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
