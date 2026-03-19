#!/usr/bin/python3
"""4-from_json_string module

This module contains a function that returns a Python object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string"""
    return json.loads(my_str)
