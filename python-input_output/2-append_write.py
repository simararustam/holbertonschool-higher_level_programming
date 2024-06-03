#!/usr/bin/python3
"""This function that appends a string at the end of
a text file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """
    Appends the specified text to a file.
    If the file does not exist, it will be created.
    """

    with open(filename, mode='a', encoding="utf-8") as f:
        f.write(text)

    num = 0
    for i in text:
        num += 1
    return num
