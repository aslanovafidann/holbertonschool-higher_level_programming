#!/usr/bin/python3
"""
Function that writes an Object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a file in JSON format.

    Args:
        my_obj: Python object to serialize.
        filename (str): Name of the file to write into.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
