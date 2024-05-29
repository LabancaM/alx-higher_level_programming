#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for i in my_list[:x]:
        try:
            val = int(i)
            print("{:d}".format(val), end="")
        except (IndexError, ValueError, TypeError):
            x += 1
