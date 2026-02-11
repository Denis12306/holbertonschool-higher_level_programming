#!/usr/bin/python3
"""A class Student that defines a student by : first_name, last_name, age"""


class Student:
    """A class Student that defines a student by 3 parameters"""
    def __init__(self, first_name, last_name, age):
        """Represent the public instance attributs"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
