#!/usr/bin/python3

"""Defines the class to json module"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an
    object

    Arg:
        obj: an instance of a class
    Returns:
        dictionary description
    """

    return obj.__dict__
