#!/usr/bin/python3
"""This module provides a `Student` class to represent student
information and convert it into a dictionary format for easy
JSON serialization."""


class Student:
    """ A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """Constructs all the necessary attributes
        for the student object."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the student instance.
        """

        json_student = {}

        for key, value in self.__dict__.items():
            json_student[key] = value
        return json_student
