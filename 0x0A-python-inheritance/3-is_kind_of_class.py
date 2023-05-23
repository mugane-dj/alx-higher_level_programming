#!/usr/bin/python3

"""Defines the is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class

    Args:
        obj (any): Object to check.
        a_class (type): class to check obj against.
    Returns:
        True is obj is an instance of a_class
        False otherwise
    """

    return isinstance(obj, a_class)
