#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {} {}".format(first_name, last_name))
    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
