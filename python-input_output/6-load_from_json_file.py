#!/usr/bin/python3
""" A function that creates an Object from a JSON file """
import json


def load_from_json_file(filename):
    """Represent the json object's created"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
