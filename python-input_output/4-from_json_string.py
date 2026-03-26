#!/usr/bin/python3
"""Convert JSON string to Python object"""
import json


def from_json_string(my_str):
    """Return Python object from JSON string"""
    return json.loads(my_str)
