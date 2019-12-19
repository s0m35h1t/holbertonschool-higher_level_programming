#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        roman_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        for i in roman_string:
            sum += roman_num[i]
        return sum
    return (0)
