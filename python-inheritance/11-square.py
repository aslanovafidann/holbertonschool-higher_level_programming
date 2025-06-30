#!/usr/bin/python3
"""Module that defines Square class with string representation"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with size and __str__"""

    def __init__(self, size):
        """Initialize square with size validated"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square"""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
