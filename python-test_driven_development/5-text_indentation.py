#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Fonction qui imprime un texte avec 2 nouvelles lignes après des caractères spc
"""


def text_indentation(text):
    """
    Fonction qui imprime un texte avec 2 nouvelles lignes
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in [".", "?", ":"]:
        text = text.replace(char, char + "\n\n")

    print(text.strip())
