#!/usr/bin/python3

"""Defines the write file module"""


def write_file(filename="", text=""):
    """Write text to a text file

    Args:
        filename (.txt): text file to write to.
        text (str): text to write to text file.
    Returns:
        number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
