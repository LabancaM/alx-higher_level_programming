#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) > 0:
        return [ True if i % 2 == 0 else False for i in my_list]
    else:
        return my_list
