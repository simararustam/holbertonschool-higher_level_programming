#!/usr/bin/python3
"""This module define Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class) or dir(obj) == dir(a_class):
        return True
    else:
        return False
