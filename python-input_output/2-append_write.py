#!/usr/bin/python3
"""
Function that appends a string to the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to add at the end of the file.

    Returns:
        int: Number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
