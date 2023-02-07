#!/usr/bin/python3

"""Defines the read file module"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
        filename (.txt): text file to read.
    """

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
