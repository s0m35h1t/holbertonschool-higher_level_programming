#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    l = []
    if my_list:
        for i in my_list:
            l.append(False if i % 2 else True)
    return l
