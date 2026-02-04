#!/usr/bin/python3
"""Define an empty class BaseGeometry"""


class BaseGeometry:
    """Represent an empty class BaseGeometry"""

    def area(self):
        """Raise an exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer"""
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Define an empty class Rectangle with inheritage of BaseGeometry class"""

    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
