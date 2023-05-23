#!/usr/bin/python3


"""Defines the Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializer for Student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of an instance of Student"""
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            for attr in attrs:
                if hasattr(self, attr):
                    return {attr: getattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
