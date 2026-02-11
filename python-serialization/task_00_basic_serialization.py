#!/usr/bin/python3
"""Create a basic serialization module that adds the functionality to
serialize a Python dictionary to a JSON file and deserialize the JSON file
to recreate the Python Dictionary."""
import json


def serialize_and_save_to_file(data, filename):
    """A Python Dictionary with data with output JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f)
    except Exception:
        return None


def load_and_deserialize(filename):
    """Deserialised the Python object"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None
