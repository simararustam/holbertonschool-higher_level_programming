#!/usr/bin/python3
def print_last_digit(number):
    last = str(number)[-1:]
    last = int(last)
    print(last, end='')
    return last
