#!/usr/bin/python3
"""Module that defines Square class with correct __str__ format"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size):
        """Initialize Square with size validated"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return string representation of the square"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
