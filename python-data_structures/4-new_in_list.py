#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    diff_list = my_list.copy()
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    diff_list[idx] = element
    return diff_list

# on créé une nouvelle variable dif_list qui va contenir une copie de my_listt
# qui permettre de modifier la copie de my_listt sans détruire l'original

# légende : en commentaire les variables finissent par deux fois la lettre
# car le checker holberton n'accepte pas les nom de variable identique en
# commentaire
