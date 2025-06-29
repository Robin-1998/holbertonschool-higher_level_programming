#!/usr/bin/python3
"""
Projet Holberton
ROBIN D
Script qui change le nom d'un état à partir de la base de donnée
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter_by(id=2).update({"name": "New Mexico"})

    session.commit()
