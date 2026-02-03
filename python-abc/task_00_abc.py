#!/usr/bin/python3
from abc import ABC, abstractmethod
"""Create an abstract class named Animal using the ABC package"""


class Animal(ABC):
    """Represent a class Animal"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Represent the class Dog"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Represent the class Cat"""

    def sound(self):
        return "Meow"
