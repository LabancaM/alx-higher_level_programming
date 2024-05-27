#!/usr/bin/python3
def best_score(a_dictionary):
    maxi = 0
    key = None
    if a_dictionary != None:
        for i, j in zip(a_dictionary.keys(), a_dictionary.values()):
            if maxi < j:
                maxi = j
                key = i
    return key
