#!/usr/bin/python3
"""This module defines the MyList class that extends the built-in list.
"""


class MyList(list):
    """A custom list class that inherits from the built-in list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
