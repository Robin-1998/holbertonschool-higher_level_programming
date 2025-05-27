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
