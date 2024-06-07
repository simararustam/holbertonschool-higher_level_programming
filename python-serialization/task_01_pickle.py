#!/usr/bin/env python3
"""Pickling Custom Classes"""
import pickle


class CustomObject:

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        with open(filename, mode="wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, mode="rb") as file:
            return pickle.load(file)
