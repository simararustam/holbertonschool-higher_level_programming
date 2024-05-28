#!/usr/bin/python3
"""This script defines a function to print a \
text with two new lines after each '.', '?', or ':' character."""


def text_indentation(text):
    """Prints the given text with two new lines after each '.', '?', or ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            new_text += text[i] + "\n"
            i += 1
        else:
            if text[i] == ' ' and i > 0 and text[i - 1] in ['.', '?', ':']:
                i += 1
                continue
            new_text += text[i]
            i += 1

    print(new_text)
