#!/usr/bin/python3
"""A function that appends a string at the end of a text file (UTF8) and
returns the number of characters added"""


def append_write(filename="", text=""):
    """Represent the append string at the end of a file and returns
    the number of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        written = f.write(text)
        return written
