#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Fichier python contenant la définition de la classe d'un Etat et une
instance Base = declarative_base()
"""

# On importe les éléments nécessaires de SQLAlchemy :
# - Column : pour définir des colonnes de table
# - Integer et String : types de données SQL (entiers, chaînes)
# - create_engine : utilisé plus tard pour se connecter à la base
from sqlalchemy import Column, Integer, String, create_engine
# On importe declarative_base pour créer une classe de base ORM.
# C'est **obligatoire** pour que SQLAlchemy sache que `State` est une table.
from sqlalchemy.orm import declarative_base
# On définit une classe `State`, qui représentera la table `states`
# dans la base SQL.
# Elle hérite de `Base`, ce qui permet à SQLAlchemy de la reconnaître
# comme un modèle.
Base = declarative_base()


class State(Base):
    """
    Classe `State` représentant la table `states` dans la base de données.
    Chaque instance de `State` correspondra à une ligne (row)
    dans cette table.
    Pourquoi cette classe ?
    → Elle permet d'interagir avec la table `states` directement
    depuis Python, sans écrire de requêtes SQL brutes.
    """

    # Nom réel de la table dans la base de données.
    # Obligatoire pour que SQLAlchemy sache à quel nom de
    # table associer ce modèle.
    __tablename__ = 'states'
    # Définition de la colonne `id` :
    # - Type : Integer
    # - C'est la clé primaire (primary_key=True)
    # → Chaque état aura un identifiant unique.
    id = Column(Integer, primary_key=True)
    # Définition de la colonne `name` :
    # - Type : String, taille max 128
    # - nullable=False : cette colonne doit obligatoirement avoir une valeur
    # → Elle stocke le nom de l’état (ex : 'California', 'Texas')
    name = Column(String(128), nullable=False)
