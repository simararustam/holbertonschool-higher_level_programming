#!/usr/bin/python3
"""This module Only sub class of return"""


def inherits_from(obj, a_class):
    """
        Args:
        obj: An object to check.
        a_class: A class to compare obj against.
    """

    return isinstance(obj, a_class) and type(obj) != a_class
