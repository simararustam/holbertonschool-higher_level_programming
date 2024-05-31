#!/usr/bin/env python3
"""Abstract Animal Class and its Subclasses"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
    """Abstract method representing the sound an animal makes."""
        pass

class Dog(Animal):
    """Class representing a dog."""

    def sound(self):
    """Return the sound of a dog."""
        return "Bark"

class Cat(Animal):
    """Class representing a cat."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
