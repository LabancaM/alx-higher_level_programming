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

    def __eq__(self, square):
        """comparaison of two square"""
        return self.area() == square.area()

    def __ne__(self, square):
        """comparaison of two square"""
        return self.area() != square.area()

    def __gt__(self, square):
        """comparaison of two square"""
        return self.area() > square.area()

    def __ge__(self, square):
        """comparaison of two square"""
        return self.area() >= square.area()

    def __lt__(self, square):
        """comparaison of two square"""
        return self.area() < square.area()

    def __le__(self, square):
        """comparaison of two square"""
        return self.area() <= square.area()
