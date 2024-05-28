#!/usr/bin/python3
"""This script defines a function to print a \
text with two new lines after each '.', '?', or ':' character."""


def text_indentation(text):
    """Prints the given text with two new lines after each '.', '?', or ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print()
            i += 1
        else:
            print(text[i], end="")
            i += 1
