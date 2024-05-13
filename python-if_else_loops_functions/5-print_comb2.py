#!/usr/bin/python3
for i in range(0, 100):
    char = '\n'
    if i < 10:
        print(0, end='')
    
    if i <= 98:
        char = ', '
    print(i, end=char)
