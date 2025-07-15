#!/usr/bin/python3
from os.path import exists

def generate_invitations (template, attendees):
    if not isinstance(template, str):
        print("Is not a string")
        return
    if not isinstance(attendees, list):
        print("Is not a list")
        return
    if not all(isinstance(a, dict) for a in attendees):
        print("Is not a dictionaries")
        return
# all vérifie si tous les éléments de la liste sont vrai
# la seconde partie permet de vérifié si l'élément qui a été bouclé :(vu que
# c'est un dictionnaire avec plusieurs contenu)
# a, donc pour chaque élément de attendes est bien un dict

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    # . strip enlève les espaces au début et à la fin
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for x, attende in enumerate(attendees, start=1):
        # "enumerate" permet de parcourir la liste "attendees" tout en ayant un compteur "x" qui commence à 1.
        # "x" sera donc 1 pour le premier invité, 2 pour le deuxième, etc.
        # "attende" est le dictionnaire qui contient les infos d'un invité (par exemple : {"name": "Alice", ...})

        print(f"participant {x}")
        # Affiche dans la console le numéro du participant en cours de traitement (par ex. "participant 1")

        invitation = template
        # On crée une copie du template (texte avec des mots à remplacer) pour cet invité.
        # On va modifier cette copie en remplaçant les mots-clés par les vraies infos.

        for key in ['name', 'event_title', 'event_date', 'event_location']:
            # Pour chaque clé attendue (nom, titre de l'événement, date, lieu)...

            value = attende.get(key)
            # On récupère la valeur associée à la clé dans le dictionnaire de l'invité.
            # Par exemple, si key == 'name', value sera "Alice" pour le premier invité.
            # Si la clé n'existe pas dans le dictionnaire, get() renvoie None.

            if value is None:
                value = "N/A"
            # Si la valeur est None (c'est-à-dire absente), on la remplace par "N/A" pour indiquer que l'info manque.

            invitation = invitation.replace(f"{{{key}}}", str(value))
            # Dans le texte "invitation", on remplace toutes les occurrences du mot-clé entre accolades,
            # par exemple "{name}", par la vraie valeur (ou "N/A").
            # On convertit la valeur en chaîne de caractères avec str(), car replace() attend un texte.


        filename = f"output_{x}.txt"
        if exists(filename):
            print(f"{filename} already exists")

        with open(filename, 'w', encoding=u'utf-8') as f:
            f.write(invitation)
            # on écrit le contenu de la template dans le fichier filename
