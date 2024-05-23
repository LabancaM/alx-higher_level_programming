#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = dict(sorted(a_dictionary.items()))
    for i,j in zip(new_dict.keys(), new_dict.values()):
        print("{}: {}".format(i, j))
    return new_dict
