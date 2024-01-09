#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if length == 0 or idx < 0 or idx >= length:
        return None
    else:
        return my_list[idx]
