#!/usr/bin/python3
"""6-load_from_json_file module

This module contains a function that creates a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
