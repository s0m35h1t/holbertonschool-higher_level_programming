#!/usr/bin/python3
"""Define: find peak algorithm."""


def find_peak(li):
    """finds a peak in a list
    Agruments:
        li (list): list of unsorted integers
    Returns:
        int, None
    """
    l = len(li)
    if l == 0:
        return
    mid = l // 2
    if (mid == l - 1 or li[mid] >= li[mid + 1])\
            and (mid == 0 or li[mid] >= li[mid - 1]):
        return li[mid]
    if mid != l - 1 and li[mid + 1] > li[mid]:
        return find_peak(li[mid + 1:])
    return find_peak(li[:mid])
