#!/usr/bin/python3

"""Defines is_same_class module"""


def is_same_class(obj, a_class):
    """Returns bool if obj is an instance of a_class

    Args:
        obj (any): Object to check.
        a_class (type): class to check obj against.
    Returns:
        True is obj is an instance of a_class
        False otherwise
    """

    if type(obj) == a_class:
        return True
    return False
