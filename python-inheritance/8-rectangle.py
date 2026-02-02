#!/usr/bin/python3
class BaseGeometry:
    """Represent an empty class BaseGeometry"""

    def area(self):
        """Parameter of the class BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Parameter of the class BaseGeometry that check
         if value is a valid int"""
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Represent an empty class Rectangle with inheritage of previous class"""
    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

