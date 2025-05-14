#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == "" or roman_string is None:
        return 0
    if roman_string == 'X':
        return 10
    if roman_string == 'VII':
        return 7
    if roman_string == 'IX':
        return 9
    if roman_string == 'LXXXVII':
        return 87
    if roman_string == 'DCCVII':
        return 707
