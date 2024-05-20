#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    if n < 0 or n > length - 1:
        return str
    else:
        stri = ""
        for i in range(length):
            if i == n:
                continue
            stri = stri + str[i]
        return stri
