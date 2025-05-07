#!/usr/bin/python3
def print_last_digit(number):
    print(abs(number) % 10, end='')
    return (abs(number) % 10)
# abs(number) : prend la valeur absolue du nombre.Cela transforme un
# nombre négatif en positif. Par exemple, abs(-278) devient 278.
# %10, permet d'obtenir le dernier chiffre
