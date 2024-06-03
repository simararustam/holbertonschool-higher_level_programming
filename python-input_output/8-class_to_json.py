#!/usr/bin/python3
"""This function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object import json
"""


def class_to_json(obj):
    """
    Converts an object to a JSON-compatible dictionary
    """

    json_ob = {}

    for key, value in obj.__dict__.items():
        json_ob[key] = value

    return json_ob
