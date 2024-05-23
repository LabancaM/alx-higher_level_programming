#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    mew_set1 = set_1.union(set_2)
    new_set2 = set_1.intersection(set_2)
    return mew_set1.difference(new_set2)
