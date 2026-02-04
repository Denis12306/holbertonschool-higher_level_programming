#!/usr/bin/python3
"""Define a class MyList that inherits to list"""


class MyList(list):
    """Represent a class MyList that inherits to list"""

    def print_sorted(self):
        """Print the list sorted in ascending order"""
        new_list = self[:]
        new_list.sort()
        print(new_list)
