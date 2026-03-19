#!/usr/bin/python3
"""0-read_file module

This module contains a function that reads a UTF-8 text file
and prints its content to stdout.
"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
