#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for remove in my_string:
        if remove != 'c' and remove != 'C':
            result = result + remove
    return result

# on est obliger de stocker du caractère dans result avant pour pouvoir
# modifier les caractères dedans.
