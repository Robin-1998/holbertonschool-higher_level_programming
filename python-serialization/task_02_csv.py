#!/usr/bin/python3
""" fonction de sérialisation et déséralisation d'un fichier JSOn """
import csv
import json


def convert_csv_to_json(csv_filename):
    """ fonction qui convertit un fichier csv en json"""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"Erreur : {e}")
        return False
