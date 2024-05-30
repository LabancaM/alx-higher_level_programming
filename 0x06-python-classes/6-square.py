#!/usr/bin/python3

""" This is class Square."""


class Square:
    """ This is class Square."""

    def __init__(self, size=0, position=(0,0)):
        """Initialisation function.

        args
            size: the size of square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get position"""
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False or (value[0] < 0 or value[1] < 0) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """ compute the area of square."""
        return self.__size * self.__size

    def my_print(self):
        """print the square"""
        length = self.__size
        position = self.__position
        if length > 0:
            for i in range(length):
                if position[1] == 0:
                    print(" " * position[0], end="")
                for j in range(length):
                    print("#", end="")
                print()
        else:
            print()


