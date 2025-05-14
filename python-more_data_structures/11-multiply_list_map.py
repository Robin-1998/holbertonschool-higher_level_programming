#!/usr/bin/python3
# fonction qui renvoie une liste avec toute les valeurs multiplié par un
# nombre sans utiliser de loupe.

def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * 4, my_list))
