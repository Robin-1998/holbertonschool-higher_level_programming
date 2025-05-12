#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

# 0 représente la longueur de la chaîne vide
