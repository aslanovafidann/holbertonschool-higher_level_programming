#!/usr/bin/python3
"""Module that defines MyList class inherited from list"""

class MyList(list):
    """MyList class inherits from list"""

    def print_sorted(self):
        """Print the list elements in ascending order"""
        print(sorted(self))
