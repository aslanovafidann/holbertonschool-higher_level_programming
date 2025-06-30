#!/usr/bin/python3
"""Module that defines the inherits_from function"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class, else False"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
