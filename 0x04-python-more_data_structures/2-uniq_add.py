#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_uniq = 0
    for el in set(my_list):
        sum_uniq += el
    return sum_uniq
