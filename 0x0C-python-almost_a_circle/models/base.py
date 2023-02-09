#!/usr/bin/python3

"""Defines the Base class module"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        __nb_objects += 1
        self.id = __nb_objects
