#!/usr/bin/python3
import json
"""This function that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string
    """

    return json.dumps(my_obj)
