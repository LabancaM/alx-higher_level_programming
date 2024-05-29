#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0:
        print()
        return 0
    else:
        try:
            for i in my_list[:x]:
                print(i, end="")
            print()
            return my_list[x - 1]
        except IndexError:
            return my_list[-1]
