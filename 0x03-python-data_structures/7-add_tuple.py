#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n = len(tuple_a)
    m = len(tuple_b)

    if n == 0:
        a, b = 0, 0
        if m == 0:
            c, d = 0, 0
        elif m == 1:
            c, d = tuple_b[0], 0
        else:
            c, d = tuple_b[0], tuple_b[1]
    if n == 1:
        a, b = tuple_a[0], 0
        if m == 0:
            c, d = 0, 0
        elif m == 1:
            c, d = tuple_b[0], 0
        else:
            c, d = tuple_b[0], tuple_b[1]
    else:
        a, b = tuple_a[0], tuple_a[1]
        if m == 0:
            c, d = 0, 0
        elif m == 1:
            c, d = tuple_b[0], 0
        else:
            c, d = tuple_b[0], tuple_b[1]
    return a + c, b + d
