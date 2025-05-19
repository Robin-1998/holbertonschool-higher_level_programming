#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Class qui définit un carré
"""


class Square:
    """ on définit le carré dans la class Square """
    pass

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size
