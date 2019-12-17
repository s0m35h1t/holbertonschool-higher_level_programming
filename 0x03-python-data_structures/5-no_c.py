#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            str += c
    return str
