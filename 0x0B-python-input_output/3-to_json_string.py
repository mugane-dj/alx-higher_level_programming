#!/usr/bin/python3

"""Defines the string to JSON module"""
import json


def to_json_string(my_obj):
    """Converts string to JSON

    Args:
        obj(str): string to convert to JSON.
    Returns:
        JSON representation
    """

    return json.dumps(my_obj)
