#!/usr/bin/python
"""a class named CountedIterator that extends the built-in iterator
    obtained from the iter function"""


class CountedIterator:
    """Define a class CountedIterator"""

    def __init__(self, iterable):
        """Initialised the attributs"""
        self.count = 0
        self.it = iter(iterable)

    def __iter__(self):
        """Initialise the iterator object"""
        return self

    def __next__(self):
        """Fetch the next item from the original iterator and return it"""
        try:
            value = next(self.it)
        except StopIteration:
            raise
        else:
            self.count += 1
            return value

    def get_count(self):
        """Retrieve and print the number of items that have been fetched"""
        return self.count
