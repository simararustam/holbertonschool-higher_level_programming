#!/usr/bin/python3
"""This  a function that writes a string to a text file
(UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """Writes the specified text to a file.
    If the file does not exist, it will be created."""

    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(text)
    with open(filename, mode='r', encoding="utf-8") as r:
        read = r.read()

    num = 0
    for i in read:
        num += 1
    return num
