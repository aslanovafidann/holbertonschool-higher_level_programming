#!/usr/bin/python3
"""
Function that returns the dictionary description for
JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description of a simple data structure
    for JSON serialization of an object.
    """
    return obj.__dict__
