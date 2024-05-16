#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    length = len(sys.argv)

    j = -1
    for i in sys.argv:
        j += 1

    if j == 0:
        print("0 arguments.")
    elif j == 1:
        print("{} argument:".format(j))
    elif j > 1:
        print("{} arguments:".format(j))
    
    k = 1
    while k < length:
        print("{}: {}".format(k, sys.argv[k]))
        k += 1
