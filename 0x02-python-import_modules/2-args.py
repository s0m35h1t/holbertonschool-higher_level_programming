#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
l = len(argv)
print("{:d} {:s}{:s}".format(l - 1, "argument" if l <= 2 else "arguments",
                                "." if l == 1 else ":"))
for i in range(1, l):
    if i > 0:
        print("{:d}: {:s}".format(i, argv[i]))
