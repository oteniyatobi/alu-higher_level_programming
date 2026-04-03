#!/usr/bin/python3
"""Module for Base class - the foundation of all model classes."""
import json
import os


class Base:
    """Base class that manages id attribute for all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with an optional id.

        Args:
            id (int): The id to assign. If None, auto-increments.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation or '[]' if None/empty.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string.

        Args:
            json_string (str): A JSON string representing a list of dicts.

        Returns:
            list: The list represented by json_string, or [] if None/empty.
        """
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            **dictionary: Key/value pairs to assign to the instance.

        Returns:
            An instance with all attributes set from dictionary.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            dummy = Rectangle(1, 1)
        else:
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file.

        Returns:
            list: A list of instances, or [] if the file does not exist.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            json_str = f.read()
        list_dicts = cls.from_json_string(json_str)
        return [cls.create(**d) for d in list_dicts]
