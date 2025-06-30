#!/usr/bin/python3
"""Module that defines Rectangle class with area and string representation"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with width, height, area and __str__"""

    def __init__(self, width, height):
        """Initialize with width and height, both validated"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
