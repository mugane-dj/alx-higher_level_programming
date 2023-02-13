#!/usr/bin/python3

"""Defines the Base class module"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON String representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        if list_objs is None:
            data = "[]"
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            data = Base.to_json_string(list_dicts)

        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(4, 4)
            else:
                dummy = cls(4)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r", encoding="utf-8") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**dict) for dict in list_dicts]
        except IOError:
            return []
