#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    length = len(sys.argv)

    j = -1
    for i in sys.argv:
        j += 1
    print("{} arguments:".format(j))
    
    k = 1
    while k < length:
        print("{}: {}".format(k, sys.argv[k]))
        k += 1
