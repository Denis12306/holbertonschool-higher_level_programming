#!/usr/bin/python3
"""Learn how to serialize and deserialize custom Python
objects using the pickle module"""
import pickle


class CustomObject:
    """Represent a class CustomObjet"""

    def __init__(self, name, age, is_student):
        """Initialised the 3 asking parameters"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """This method will take a filename as its parameter"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Deserialised the object"""
        with open(filename, "rb") as f:
            return pickle.load(f)
