#!/usr/bin/python3
"""This function that returns an object
(Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.
    """

    return json.loads(my_str)
