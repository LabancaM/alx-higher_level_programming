#!/usr/bin/python3
def roman_to_int(roman_string):
    dicte = {"I": 1, "V": 5, "X": 10, "D": 500, "L": 50, "C": 100}
    sum = 0
    if roman_string is None or roman_string is not str:
        return 0
    length = len(roman_string)
    for i in range(length - 1):
        if roman_string[i] == "I" and \
                (roman_string[i + 1] == "V" or roman_string[i + 1] == "X"):
            sum -= 1
            continue
        sum += dicte[roman_string[i]]
    sum += dicte[roman_string[-1]]
    return sum
