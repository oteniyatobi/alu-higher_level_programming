#!/usr/bin/python3
"""8-class_to_json module

This module contains a function that returns the dictionary
description for JSON serialization of an object.
"""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization"""
    return obj.__dict__.copy()
