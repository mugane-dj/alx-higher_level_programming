#!/usr/bin/python3


"""Defines the Object from JSON file module"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

    Args:
        filename: JSON file name.
    """

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        json.loads(read_data)
