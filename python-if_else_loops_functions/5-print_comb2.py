#!/usr/bin/python3
for i in range(100):
    end_char = '\n' if i == 99 else ', '
    print('{:02d}{}'.format(i, end_char), end='')
