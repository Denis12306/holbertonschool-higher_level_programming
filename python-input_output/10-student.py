#!/usr/bin/python3
"""A class Student that defines a student by : first_name, last_name, age"""


class Student:
    """A class Student that defines a student by 3 parameters"""
    def __init__(self, first_name, last_name, age):
        """Represent the public instance attributs"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                new_dict[attr] = getattr(self, attr)
        return new_dict
