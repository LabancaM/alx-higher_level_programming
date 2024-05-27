#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dicter = {}
    for i, j in zip(a_dictionary.keys(), a_dictionary.values()):
        dicter[i] = j * 2
    return dicter
