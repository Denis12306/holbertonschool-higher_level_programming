#!/usr/bin/python3
class MyList(list):
    """Write a class MyList that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
