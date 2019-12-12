#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    l = len(argv)
    print("{:d} {}{}".format(l - 1, "argument" if l - 1 == 1 else "arguments",
                             "." if l == 1 else ":"))
    for i, arg in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, arg))
