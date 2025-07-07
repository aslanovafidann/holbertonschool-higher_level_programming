#!/usr/bin/python3
"""
Defines a Student class with optional attrs filtering for JSON representation.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.
        If attrs is a list of strings, returns only those attributes.
        Otherwise, returns all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict
        else:
            return self.__dict__
