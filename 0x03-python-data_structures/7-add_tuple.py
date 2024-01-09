#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n = len(tuple_a)
    m = len(tuple_b)
    if n == 0:
        a, b = 0, 0
        if m == 0:
            c, d = 0, 0
        if m == 1:
            c, d = tuple_b[0], 0
        if m >=2:
            c, d = tuple_b[0], tuple_b[1]
    elif m == 0:
        c, d = 0, 0
        if n == 0:
            a, b = 0, 0
        if n == 1:
            a, b = tuple_a[0], 0
        if m >=2:
            a, b = tuple_a[0], tuple_a[1]
    elif m >=2 and n >=2:
        a, b = tuple_a[0], tuple_a[1]
        c, d = tuple_b[0], tuple_b[1]
    return a+c, b+d
