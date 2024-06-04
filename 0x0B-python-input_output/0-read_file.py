#!/usr/bin/python3
""" read file"""


def read_file(filename=""):
    """ function to read file

        Args
            filename: text file name
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
