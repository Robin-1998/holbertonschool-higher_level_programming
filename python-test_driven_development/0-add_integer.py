#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Write a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
        Return the factorial of n, an exact integer >= 0.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
