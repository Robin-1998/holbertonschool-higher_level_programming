#!/usr/bin/python3
"""
This module provides a function that adds two integers.
It accepts integers or floats as input.
If floats are passed, they are casted to integers.
Raises a TypeError if inputs are not valid numbers.
Returns the integer addition result.
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats after casting.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
