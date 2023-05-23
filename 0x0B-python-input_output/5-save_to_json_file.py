#!/usr/bin/python3

"""Defines the save to JSON file module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON

    Args:
        my_obj: Object to convert to JSON.
        filename: Text file to write JSON on.
    """

    with open(filename, 'w', encoding="utf-8") as f:
        write_data = json.dumps(my_obj)
        f.write(write_data)
