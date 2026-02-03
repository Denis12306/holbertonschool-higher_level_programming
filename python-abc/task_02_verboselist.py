#!/usr/bin/python3
"""A class named VerboseList that extends the Python list class"""


class VerboseList(list):
    """Represent a VerboseList class"""

    def append(self, item):
        """Add an item to the list"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend the list with items"""
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Remove an item to the list"""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, item=-1):
        """Pop an item from the list"""
        value = super().pop(item)
        print(f"Popped [{value}] from the list.")
        return value
