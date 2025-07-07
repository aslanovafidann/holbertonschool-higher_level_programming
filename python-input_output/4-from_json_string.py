#!/usr/bin/python3
"""
Function that returns an object (Python data structure)
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): JSON-formatted string.

    Returns:
        object: Corresponding Python data structure.
    """
    return json.loads(my_str)
