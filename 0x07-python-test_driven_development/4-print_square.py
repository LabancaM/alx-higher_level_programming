#!/usr/bin/python3
""" square function"""


def print_square(size):
    """ square function

    Args
        size: size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print()
