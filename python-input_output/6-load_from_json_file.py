#!/usr/bin/python3
"""This function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.
    """

    with open(filename, mode='r', encoding="utf-8") as f:
        return json.loads(f.read())
