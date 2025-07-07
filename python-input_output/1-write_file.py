#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns number of characters written.

    Args:
        filename (str): name of the file to write to.
        text (str): text to write.

    Returns:
        int: number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
