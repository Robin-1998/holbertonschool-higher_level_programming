#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Une classe abstraite : Animal
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """ classe principale """
    @abstractmethod
    def area(self):
        pass

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
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    print("Area", shape.area())
    print("Perimeter", shape.perimeter())
