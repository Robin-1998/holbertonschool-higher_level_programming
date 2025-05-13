#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    largest = my_list[0]
    for i in my_list:
        if i > largest:
            largest = i
    return (largest)

# on parcourt la liste et on va chercher la plus grande valeur
# Si l'élément actuel est supérieur au plus grand on le met à jour
