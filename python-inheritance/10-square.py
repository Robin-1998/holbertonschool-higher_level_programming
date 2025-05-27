#!/usr/bin/python3
"""
Ce module contient la définition d'une classe de base pour des formes
géométriques.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square qui hérite de Rectangle"""

    def __init__(self, size):
        """ instantation """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2
# on mutliple pour avoir l'air au carré vu qu'il n'y a pas de présence de
# width et height alors on multiplie deux fos par deux

    def __str__(self):
        return (f"[Rectangle] {self.__size}/{self.__size}")
