#!/usr/bin/python3
class BaseGeometry:
    """Represent an empty class BaseGeometry"""

    def area(self):
        """Area of the class BaseGeometry"""
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
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height

    def area(self):
        """Area of the class BaseGeometry"""
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """Represent a class Square with Rectangle attributs """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
