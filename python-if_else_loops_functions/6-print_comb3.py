#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        char = '\n' if i == 8 and j == 9 else ', '
        print('{0}{1}'.format(i, j), end=char)
