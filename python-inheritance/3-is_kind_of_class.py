#!/usr/bin/python3
"""This module define Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of, or if
    obj is an instance of a class that inherited
    from,the specified class a_class.

    Args:
        obj: An object to check.
        a_class: A class to compare obj against.

    Returns:
        True if obj is an instance of a_class or its subclass; otherwise False.
    """

    if isinstance(obj, a_class) or dir(obj) == dir(a_class):
        return True
    else:
        return False
