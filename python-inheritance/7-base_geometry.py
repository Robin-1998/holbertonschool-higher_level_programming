#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Classe BaseGeometry with test
"""


class BaseGeometry:
    """Classe BaseGeometry"""

    def area(self):
        """ Public instance method with an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method with a multiple exception """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
