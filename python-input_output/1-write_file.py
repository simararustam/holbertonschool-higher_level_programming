#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(text)
    with open(filename, mode='r', encoding="utf-8") as r:
        read = r.read()

    num = 0
    for i in read:
        num += 1
    return num
