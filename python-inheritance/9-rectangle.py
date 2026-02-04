#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """Represent a class BaseGeometry"""

    def area(self):
        """Area of the class BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represent a class Rectangle with inheritage of BaseGeometry class"""

    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height

    def area(self):
        """Area of the Rectangle"""
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
