#!/usr/bin/python3
"""Module to check if object is instance or subclass instance of a class"""

def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of or inherits from a_class"""
    return isinstance(obj, a_class)
