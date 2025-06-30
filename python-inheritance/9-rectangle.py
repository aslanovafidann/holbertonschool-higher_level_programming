#!/usr/bin/python3
"""Module that defines BaseGeometry class with an area method"""


class BaseGeometry:
    """BaseGeometry class with unimplemented area method"""

    def area(self):
        """Raise Exception for area not implemented"""
        raise Exception("area() is not implemented")
