#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    liste = []
    for i in my_list:
        if i not in liste:
            liste.append(i)
            sum += i
    return sum
