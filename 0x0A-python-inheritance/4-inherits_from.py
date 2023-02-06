#!/usr/bin/python3


"""Defines inherits_from module"""


def inherits_from(obj, a_class):
    """Check is obj is an instance of a subclass of a_class

    Args:
        obj (any): Object to check.
        a_class (type): class to check obj against.
    Returns:
        True is obj is an instance of a subclass of a_class
        False otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
