#!/usr/bin/python3

"""Defines the MyList class"""


class MyList(list):
    """A class that inherits from list base class"""

    def print_sorted(self):
        print(sorted(self))
