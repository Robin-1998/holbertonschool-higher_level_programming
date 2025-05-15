#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    tableau = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
# on divise nos 2 éléments en les parcourtant à l'aide de la vrble index
        except TypeError:
            print("wrong type")
            result = 0  # on réinitialise result à zéro pour préciser
# que la variable existe toujours
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            tableau.append(result)  # on ajoute result à la fin de notre liste
    return tableau
