#!/usr/bin/python3
"""10-student module

Defines a Student class and a method to return its dictionary representation
with optional attribute filtering.
"""


class Student:
    """Student class with attribute filter"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation, optionally filtering attributes"""
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()
