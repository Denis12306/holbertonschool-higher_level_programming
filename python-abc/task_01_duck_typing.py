#!/usr/bin/python3
from abc import ABC, abstractmethod
import math
"""Create an abstract class named Shaped using the ABC package"""


class Shaped(ABC):
    """Represent a class Shaped"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shaped):
    """Represent a class Circle inherited from Shaped"""

    def __init__(self, radius):
         """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """Calculate the perimeter of the circle"""
        return 2 * math.pi * self.radius

    def shape_info(self):
        """Print the area and perimeter of the shape."""
        return f"[Circle] radius={self.radius}"


class Rectangle(Shaped):
    """Represent a class Rectangle inherited from Shaped"""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def shape_info(self):
        """Print the area and perimeter of the shape."""
        return f"[Rectangle] {self.width}/{self.height}"


def shape_info(obj):
    """Print the area and perimeter of the shape."""
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
