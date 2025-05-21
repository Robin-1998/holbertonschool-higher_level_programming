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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ On renvoie le plus grand rectangle en fonction de la surface"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Retourne une nouvelle instance de rectangle où la largeur
        et la haueteur sont égales à size"""
        return cls(size, size)

# cls(size, size) crée une nouvelle instance de Rectangle avec la même
# valeur pour la largeur et la hauteur.
# size qui est un des paramètres, appelle le constructeur init aui utilise
# donc width et height qui sont bien présent dans le _init_

    def __str__(self):
        """On répète la ligne de # autant de fois que la hauteur e"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        return '\n'.join(str(self.print_symbol) * self.__width
                         for _ in range(self.__height))

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
