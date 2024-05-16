#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0
    leng = len(sys.argv)
    i = 1

    while i < leng:
        result += int(sys.argv[i])
        i += 1
    print(result)
