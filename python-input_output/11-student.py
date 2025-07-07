#!/usr/bin/python3
"""
Defines a Student class with serialization and deserialization methods.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves dictionary representation of the Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list are retrieved. Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from json.

        Args:
            json (dict): Dictionary with attribute names as keys
                         and attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
