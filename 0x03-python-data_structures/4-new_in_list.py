#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    l = my_list[:]
    if 0 <= idx < len(l):
        l[idx] = element
        return (l)
    return (my_list)
