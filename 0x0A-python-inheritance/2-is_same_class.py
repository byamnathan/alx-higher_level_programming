#!/usr/bin/python3
"""Is same class module"""


def is_same_class(obj, a_class):
    """Returns `true` if the object is exactly an instance of the
    specified class"""

    return type(obj) is a_class
