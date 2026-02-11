#!/usr/bin/python3
"""Create a basic serialization module that adds the functionality to
serialize a Python dictionary to a JSON file and deserialize the JSON file
to recreate the Python Dictionary."""
import pickle


def serialize_and_save_to_file(data, filename):
    """Represent the Python dictionary added"""
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """Represent the deserialized JSON data from the file"""
    with open(filename, "rb") as f:
        return pickle.load(f)
