#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Classe BaseGeometry with test
"""


class BaseGeometry:
    """Classe vide"""

    def area(self):
        """ public instance method with an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public instance method with other exception"""
        isinstance(name, str)
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
