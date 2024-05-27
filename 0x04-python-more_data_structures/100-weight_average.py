#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        num, den = 0, 0
        for i in my_list:
            num += (i[0] * i[1])
            den += i[1]
        return num / den
    return 0
