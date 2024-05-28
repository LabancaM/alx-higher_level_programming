#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in my_list[:x]:
            val = int(i)
            print("{:d}".format(val), end="")
        print()
        return my_list[x - 1]
    except (IndexError, ValueError, TypeError):
        x += 1
