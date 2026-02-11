#!/usr/bin/python3
"""A function that returns the dictionary description with simple data
structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object"""
import json


def class_to_json(obj):
    """Represent the dict to return"""
    return obj.__dict__
