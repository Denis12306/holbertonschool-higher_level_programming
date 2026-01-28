#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 2-square.py)"""

class Square:
    """Size must be an integer otherwaise raise a TypeError"""
    """If size is less than 0 raise a ValueError"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
