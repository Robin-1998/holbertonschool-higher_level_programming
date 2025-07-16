from flask import Flask, render_template, request
import json
import csv

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
    with open('items.json') as file:
        data = json.load(file)
        item_list = data.get("items", [])
    return render_template('items.html', items=item_list)

# Fonction pour lire un fichier JSON
def lire_json(fichier='products.json'):
    try:
        # Ouvre le fichier JSON en lecture avec encodage UTF-8
        with open(fichier, 'r', encoding='utf-8') as f:
            # Charge les données JSON dans une variable Python (liste/dictionnaire)
            return json.load(f)
    except Exception:
        # Si une erreur survient (ex : fichier non trouvé), retourne une liste vide
        return []

# Fonction pour lire un fichier CSV
def lire_csv(fichier='products.csv'):
    try:
        # Ouvre le fichier CSV avec encodage UTF-8
        with open(fichier, newline='', encoding='utf-8') as f:
            # Crée un lecteur CSV qui retourne chaque ligne sous forme de dictionnaire
            lecteur = csv.DictReader(f)
            données = []
            # Parcourt chaque ligne du fichier
            for ligne in lecteur:
                # Ajoute les données dans une liste après conversion des types
                données.append({
                    "id": int(ligne['id']),            # Convertit l'id en entier
                    "name": ligne['name'],             # Nom du produit (texte)
                    "category": ligne['category'],     # Catégorie du produit
                    "price": float(ligne['price'])     # Prix converti en nombre décimal
                })
            # Retourne la liste complète des produits
            return données
    except Exception:
        # En cas d'erreur (ex : mauvaise structure), retourne une liste vide
        return []

# Définition d'une route Flask pour afficher les produits
@app.route('/produits')
def afficher_produits():
    # Récupère le paramètre "source" (json ou csv) dans l'URL
    source = request.args.get('source')
    
    # Récupère le paramètre "id" dans l'URL, converti en entier
    produit_id = request.args.get('id', type=int)

    # Choisit la source des données selon la valeur passée dans l'URL
    if source == 'json':
        produits = lire_json()  # Charge les données depuis le fichier JSON
    elif source == 'csv':
        produits = lire_csv()   # Charge les données depuis le fichier CSV
    else:
        # Si la source est invalide, affiche un message d'erreur
        return render_template(
            'product_display.html',
            error="Source invalide. Choisissez 'json' ou 'csv'.",
            products=[]
        )

    # Si un ID est fourni, filtre la liste des produits
    if produit_id:
        # Garde uniquement le produit avec l'ID demandé
        produits = [p for p in produits if p['id'] == produit_id]
        # Si aucun produit ne correspond à cet ID, afficher une erreur
        if not produits:
            return render_template(
                'product_display.html',
                error="Produit non trouvé.",
                products=[]
            )

    # Affiche la page HTML avec la liste des produits (ou un seul produit si filtré)
    return render_template('product_display.html', products=produits)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
