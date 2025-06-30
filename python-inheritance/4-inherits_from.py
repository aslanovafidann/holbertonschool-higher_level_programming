#!/usr/bin/python3
"""Module to check if object inherits from a class (not exactly instance)"""

def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
