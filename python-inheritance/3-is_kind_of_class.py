#!/usr/bin/python3
"""Check if an object is an instance of a class or subclass.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or subclass, else False."""
    return isinstance(obj, a_class)
