#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        max = list(a_dictionary.keys())[0]
        for key in a_dictionary.keys():
            if a_dictionary[max] < a_dictionary[key]:
                max = key
        return max
    return None
