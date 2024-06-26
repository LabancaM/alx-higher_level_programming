#!/usr/bin/python3

""" This is class Square."""


class Square:
    """ This is class Square."""

    def __init__(self, size=0):
        """Initialisation function.

        args
            size: the size of square.
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
