#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    liste = []
    for i, j in zip(a_dictionary.keys(), a_dictionary.values()):
        if j == value:
            liste.append(i)
    for k in liste:
        del a_dictionary[k]
    return a_dictionary
