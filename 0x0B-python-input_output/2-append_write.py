#!/usr/bin/python3

"""Defines the append text module"""


def append_write(filename="", text=""):
    """Appends text to a text file

    Args:
        filename (.txt): text file to write to.
        text (str): text to write to text file.
    Returns:
        number of characters written
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
