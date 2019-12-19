#!/usr/bin/python3
def weight_average(my_list=[]):
    dem_sum = num = 0
    for t in my_list:
        num += t[0] * t[1]
        dem_sum += t[1]
    return num / dem_sum
