#!/usr/bin/python3
""" Développer une API en utilisant le module http.server """
import http.server
import socketserver
import json

PORT = 8000


class server(http.server.BaseHTTPRequestHandler):
    """ Classe server qui comprend les conditions suivant le path rencontré """

    def do_GET(self):
        if self.path == "/data":
            # On gère le cas où le serveur fonctionne
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            # Utiliser application/json pour les données JSON
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            
            self.wfile.write(json.dumps(dataset).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        elif self.path == "/info":
            data_info = {"version": "1.0",
                         "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(json.dumps(data_info).encode('utf-8'))

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            # Sans ce code le client ne saura comment lire la réponse (mauvais
            # affichage), là où lui donne un texte encodé en UTF-8
            self.end_headers()
            # On indique au client que la partie entête est terminée. Sinon il
            # attend encore et il ne peut pas lire son contenu.
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
            # C'est une sorte de lien qui fait la passation de la réponse
            # du serveur au client pour qu'il puisse voir le message

        # Utilisation d'un 'else' pour attraper toutes les autres routes
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode('utf-8'))

# Si on ne met pas toutes ces informations, l'utilisateur ne pourra pas voir sa
# réponse et il faut aussi respecter la structure (statut + entêtes + corps)

# STATUT : indique le code statut (échec, réussite ou autre)

# ENTETES : donne des informations supplémentaires au client comme le type
# de contenu envoyé (texte par ex), la longueur du contenu, la gestion du
# cache et bien d'autres

# CORPS : c'est le contenu que reçoit le client. Par exemple si c'est une
# page HTML, un fichier JSON, du texte BRUT, une image et bien d'autres

if __name__ == "__main__":
# Dans le 'with', le fait de rajouter une chaîne vide signifie que le serveur
# écoutera sur n'importe quelle interface réseau (toutes les adresses IP)
    with socketserver.TCPServer(("", PORT), server) as httpd:
        print("Serving on port", PORT)
        httpd.serve_forever()
        # server_forever est une méthode sur l'instance TCPserver qui permet
        # tout simplement de démarrer le serveur


