#!/usr/bin/python3
""" développer une API en utilisant le module http.server"""
import http.server
import socketserver
import json

PORT = 8000


class server(http.server.BaseHTTPRequestHandler):
    """ Class server qui comprend les conditions suivant le path rencontré """
    def do_GET(self):
        if self.path == "/data":
# on gère le cas dans la méthode ou le serveur fonctionne
            self.send_response(200)
            self.send_header("Content-Type", "application/john; charset=utf-8")
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dataset).encode('utf-8'))

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
# sans ce code le client ne sara comment lire la réponse (mauvais
# affichage) là où lui donne un texte encodé en UTF-8
            self.end_headers()
# on indique au client que la partie entête est terminé. sinon il
# attend encore et il ne peut pas lire son contenu.
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
# est une sorte de lien qui fait la passation de la réponse du serveur
# au client pour qu'il puisse voir le message

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/john; charset=utf-8")
            self.end_headers()
            data_info = {"version": "1.0",
                         "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(data_info).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        elif self.path != "/status":
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("404 Not Found".encode('utf-8'))

# si on ne met pas toute ses informations, userne pourra pas voir sa
# réponse et il faut aussi respecter la structure (statut + entêtes + corpts)

# STATUT : indique le code statut (échec, réussite ou autre)

# ENTETES : donne des informations supplémentaires au client comme le type
# de contenu envoyé (texte par ex), la longueur du contenu, la gestion du
# cache et bien d'autre

# CORPS : c'est le contenu que reçoit le client. Par exemple si c'est une
# page HTML, un fichier JSON, du texte BRUT, une image et bien d'autre


Handler = server

# dans le with, le fait de rajouter une chaîne vide signifie que le serveur
# écoutera sur n'importe quelle inferface réseau (toutes les adresses IP)
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving as port", PORT)
    httpd.serve_forever()
# server_forever est une méthode sur l'instance TCPserver qui permet
# tout simplement de démarrer le serveur
