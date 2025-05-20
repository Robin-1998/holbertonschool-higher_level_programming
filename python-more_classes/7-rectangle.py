#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Classe vide qui définit un rectangle
"""


class Rectangle:
    """ Une class vide dans le rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ instantation"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """On répète la ligne de # autant de fois que la hauteur e"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return '\n'.join(str(self.print_symbol) * self.__width for _ in range(self.__height))

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

# on utilise str pour convertir n'importe quel type chaine de caractère
