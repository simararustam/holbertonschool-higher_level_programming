#!/usr/bin/env python3
"""Pickling Custom Classes"""
import pickle


class CustomObject:
    """
    A class representing a custom object with
    attributes for name, age, and student status.
    """
    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initialize a CustomObject instance.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object.
        """
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle.
        """
        with open(filename, mode="wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.
        """
        with open(filename, mode="rb") as file:
            return pickle.load(file)
