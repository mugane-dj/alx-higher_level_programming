#!/usr/bin/python3


"""Defines the Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializer for Student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of an instance of Student"""

        return self.__dict__
