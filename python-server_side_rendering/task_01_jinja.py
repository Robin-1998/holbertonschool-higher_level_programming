from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
 
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Ouvre le fichier 'items.json' situé dans ton dossier de projet.
    # 'with' garantit que le fichier sera fermé automatiquement après lecture.
    with open('items.json') as file:
        # Charge le contenu JSON du fichier dans une variable Python.
        # Par exemple, si le fichier contient {"items": ["Python Book", "Flask Mug"]},
        # la variable 'data' sera un dictionnaire : {"items": ["Python Book", "Flask Mug"]}
        data = json.load(file)

        # Récupère la valeur associée à la clé "items" dans le dictionnaire 'data'.
        # Si la clé "items" n'existe pas (par exemple, erreur dans le fichier JSON), 
        # alors on renvoie une liste vide [] pour éviter une erreur.
        item_list = data.get("items", [])

    # Appelle le template 'items.html' et lui envoie la variable 'item_list',
    # qu'on renomme ici en 'items' pour l'utiliser dans le template Jinja.
    # Donc dans le fichier HTML, on pourra faire une boucle sur 'items'.
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
