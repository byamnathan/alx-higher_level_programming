#!/usr/bin/python3
"""Class to Json"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object"""

    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    return {}
