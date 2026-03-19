#!/usr/bin/python3
"""Module defines MyList class"""


class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """Prints a sorted list without modifying original"""
        print(sorted(self))
