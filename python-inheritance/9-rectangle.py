#!/usr/bin/python3
"""
Ce module contient la définition d'une classe de base pour des formes
géométriques.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle qui hérite de basegeometry"""

    def __init__(self, width, height):
        """ instantation """
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", width)

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
# la fonction str doit retourner une chaine de caractère et non un print

    def area(self):
        return self.__height * self.__width
