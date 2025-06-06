#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Classe vide qui définit un rectangle
"""


class Rectangle:
    """ Une class vide dans le rectangle """

    def __init__(self, width=0, height=0):
        """ instantation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ private instante attribute width propriété pour récupérer width """
        return self.__width

    @property
    def height(self):
        """ private instante attribute heigh propriété pour récupérer heigh """
        return self.__height

    @width.setter
    def width(self, value):
        """ private instante attribute width. pour fixer width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ private instante attribute height. pour fixer height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Public instance method qui retourne la surface du rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Public instance method qui retourne le périmètre du rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
