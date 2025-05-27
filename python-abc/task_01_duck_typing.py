#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Une classe abstraite : Shape
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """ classe principale """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """ Sous-class cercle qui hérite de shape"""

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return self.radius ** 2 * math.pi

    def perimeter(self):
        return 2 * (math.pi * self.radius)


class Rectangle(Shape):
    """ Sous-classe Rectangle qui hérite de Shape """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """ fonction qui retourne l'aire du rectangle et cercle ainsi que
        le périmètre
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
