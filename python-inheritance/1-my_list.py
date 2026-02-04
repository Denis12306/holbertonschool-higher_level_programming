#!/usr/bin/python3
"""Represent a class MyList that inherits from list"""


class MyList(list):
    """Define a class MyList that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
