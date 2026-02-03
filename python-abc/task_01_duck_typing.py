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
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def shape_info(self):
        return f"[Circle] radius={self.radius}"


class Rectangle(Shaped):
    """Represent a class Rectangle inherited from Shaped"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def shape_info(self):
        return f"[Rectangle] {self.width}/{self.height}"


def shape_info(obj):
    """Duck typing info"""
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
