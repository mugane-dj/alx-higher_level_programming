
"""Defines the JSON to object module"""
import json


def from_json_string(my_str):
    """Converts JSON string to its object representation

    Args:
        my_string: JSON string.
    Returns: object representation of JSON string.
    """

    return json.loads(my_str)
