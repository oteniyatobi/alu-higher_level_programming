#!/usr/bin/python3
"""Returns dictionary description for JSON serialization"""

def class_to_json(obj):
    """Return dictionary of object attributes"""
    return obj.__dict__
