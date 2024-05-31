#!/usr/bin/python3

""" This is class Square."""


class Square:
    """ This is class Square."""

    def __init__(self, size=0, position=(0, 0)):
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
        if isinstance(value, tuple) is False or len(value) != 2 \
                or (isinstance(value[0], int) is False or \
                isinstance(value[1], int) is False) \
                or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ compute the area of square."""
        return self.__size * self.__size

    def __str__(self):
        """print the square"""
        length = self.__size
        position = self.__position
        liste = []
        if length > 0:
            if position[1] > 0:
                liste.append(" " * position[1])
                liste.append('\n')
            for i in range(length):
                liste.append(" " * position[0])
                for j in range(length):
                    liste.append("#")
                liste.append('\n')
            return ''.join(liste[:-1])
        else:
            return ''
