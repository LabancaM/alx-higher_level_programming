#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char = i
        if ord(i) >= 97 and ord(i) <= 122:
            char = chr(ord(i) - 32)
        print(char, end="")
    print()
