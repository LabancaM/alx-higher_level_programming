#!/usr/bin/python3

""" This is class Square."""


class Square:
    """ This is class Square."""

    def __init__(self, size=0):
        """Initialisation function.

        args
            size: the size of square.
        """
        self.size = size

    @property
    def size(self):
        """get function"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ compute the area of square."""
        return self.__size * self.__size

    def my_print(self):
        """print the square"""
        length = self.__size
        if length > 0:
            for i in range(length):
                for j in range(length):
                    print("#", end="")
                print()
        else:
            print()
