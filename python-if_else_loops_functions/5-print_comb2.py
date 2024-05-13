#!/usr/bin/python3
for i in range(100):
    char = '\n' if i == 99 else ', '
    print('{:2d}{}'.format(i, char), end='')
