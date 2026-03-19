#!/usr/bin/python3
"""11-student module"""

class Student:
    """Student class with JSON reload"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation, optionally filtering attributes"""
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with the dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
