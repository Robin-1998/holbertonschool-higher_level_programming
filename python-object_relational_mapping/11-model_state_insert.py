#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui ajoute un l'état Louisiana dans la database
"""

import sys
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

# Création d'une nouvelle instance de State avec le nom "Louisiana"
# Cet objet représente une future ligne dans la table "states"
    State_louisiana = State(name="Louisiana")

# Ajout de l'objet à la session (transaction en mémoire, pas encore
# enregistrée en base)
    session.add(State_louisiana)

# Validation de la transaction : envoie l'objet dans la base et crée la ligne
# À ce moment-là, SQLAlchemy génère automatiquement un ID (auto-incrémenté)    
    session.commit()

    # Affichage de l'ID de l'état ajouté
    print(State_louisiana.id)
