#!/usr/bin/python3
""" write file"""


def write_file(filename="", text=""):
    """ function to write file

        Args
            filename: text file name
    """
    with open(filename, 'w', encoding='utf-8') as f:
        print(f.write(text), end="")
