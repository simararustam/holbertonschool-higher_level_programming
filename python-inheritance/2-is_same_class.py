#!/usr/bin/python3
"""This module returns True if the object is \
exactly an instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Check if true or not"""

    if dir(obj) == dir(a_class):
        return True
    else:
        return False
