#!/usr/bin/python3
"""This function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Reads a file line by line and prints each
    line without adding a new line character at the end.

    Parameters:
        filename (str): The path to the file to be read.
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
