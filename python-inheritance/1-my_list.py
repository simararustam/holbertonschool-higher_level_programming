#!/usr/bin/python3
"""This module inherit from list"""


class MyList(list):
    """Print sorted list"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
