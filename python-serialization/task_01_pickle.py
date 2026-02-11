#!/usr/bin/python3
"""Learn how to serialize and deserialize custom Python
objects using the pickle module"""
import pickle


class CustomObject:
    """Represent a class CustomObjet"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
