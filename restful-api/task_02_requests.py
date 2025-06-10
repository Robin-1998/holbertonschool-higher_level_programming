#!/usr/bin/python3
""" Consommer et traiter des données provenant d'une API"""
import csv
import requests


def fetch_and_print_posts():
    """function qui imprime le post"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    # Envoi d'une requête HTTP GET à l'URL

    print(f"Status Code: {response.status_code}")
    # retour de la réponse HTTP

    # si la réponse a réussi alors on transforme le contenu JSON en dic python
    # puis on parcourts chaque post dans la list et on affiche le titre du post
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("échec du traitement des données")
    # si la requête échoue, on affiche un message d'erreur


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        data = [
            {'id': dictt['id'], 'title': dictt['title'], 'body': dictt['body']}
            for dictt in posts
        ]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            # Écrit les noms de colonnes
            writer.writerows(data)
            # Écrit chaque ligne à partir du dictionnaire
    else:
        print("échec de la sauvegarde au niveau du traitement des données")
