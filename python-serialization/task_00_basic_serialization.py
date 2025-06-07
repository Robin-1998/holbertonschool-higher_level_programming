#!/usr/bin/python3
""" fonction de sérialisation et déséralisation d'un fichier JSOn """
import json


def serialize_and_save_to_file(data, filename):
    """ fonction qui sérialise et sauvegarde le fichier """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """ fonction qui désérialise le fichier"""
    with open(filename, "r", encoding="utf-8") as f:
        dictionery = json.load(f)
    return dictionery
