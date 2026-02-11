#!/usr/bin/python3
"""Create a basic serialization module that adds the functionality to
serialize a Python dictionary to a JSON file and deserialize the JSON file
to recreate the Python Dictionary."""
import pickle


def serialize_and_save_to_file(data, filename):
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
