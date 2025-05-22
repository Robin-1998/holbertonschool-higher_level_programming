import random

class BaguetteMagique:
    # Attributs de classe
    bois = ["Hêtre", "Chêne", "Acajou", "If", "Houx", "Vigne", "Saule", "Aubépine", "Sureau", "Prunellier"]
    coeurs = ["Crin de licorne", "Ventricule de dragon", "Plume de phénix", "Crin de Sombral", "Cheveu de Vélane"]
    longueur = [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    baguettes = {}  # Dictionnaire pour stocker les baguettes créées
    
    def __init__(self, maison, proprietaire):
        """
        Constructeur de la classe BaguetteMagique
        
        Paramètres:
        - maison: str - La maison de Poudlard du propriétaire (Gryffondor, Poufsouffle, Serdaigle, Serpentard)
        - proprietaire: str - Le nom du propriétaire de la baguette
        
        Attributs d'instance à initialiser:
        - proprietaire: le nom du propriétaire (paramètre)
        - maison: la maison de Poudlard (paramètre)
        - bois: choisi aléatoirement dans la liste 'bois' de la classe
        - coeur: choisi aléatoirement dans la liste 'coeurs' de la classe
        - longueur: nombre aléatoire entre 22 et 35 (cm)
        
        Tous les attributs doivent être privés et utiliser des getter et setter
        """
        self.maison = maison
        self.proprietaire = proprietaire
        self.matiere = random.choice(self.bois)
        self.vaudoo = random.choice(self.coeurs)
        self.lgbaguette = random.choice(self.longueur)

    def expelliarmus(self):
        """
        Méthode qui simule le sort Expelliarmus
        Affiche simplement "Expelliarmus !"
        """
        print("Expelliarmus !")
    
    def avada_kedavra(self):
        """
        Méthode qui simule le sort Avada Kedavra
        Vérifie si la baguette appartient à un sorcier de Serpentard
        Si oui, affiche "Avada Kedavra !"
        Si non, lève une exception avec un message approprié
        """
        if self.maison == "Serpentard":
            print("Avada Kedavra !")
        else:
            raise ValueError("Tu n'es pas un sorcier Harry !!")
    
    def enregistrer_baguette(self):
        """
        Méthode qui enregistre les informations de la baguette dans le dictionnaire de classe 'baguettes'
        Utilise le nom du propriétaire comme clé
        La valeur doit être un dictionnaire contenant toutes les informations de la baguette
        (maison, bois, coeur, longueur)
        """
        self.baguettes[self.proprietaire] = {"maison": self.maison, "bois": self.matiere, "coeurs": self.vaudoo, "longueurs": self.lgbaguette}

    @property
    def matiere(self):
        return self.__matiere

    @property
    def vaudoo(self):
        return self.__vaudoo

    @property
    def lgbaguette(self):
        return self.__lgbaguette
    
    @matiere.setter
    def matiere(self, value):
        self.__matiere = value

    @vaudoo.setter
    def vaudoo(self, value):
        self.__vaudoo = value

    @lgbaguette.setter
    def lgbaguette(self, value):
        self.__lgbaguette = value

if __name__ == "__main__":
    # Création de quelques baguettes magiques
    baguette_harry = BaguetteMagique("Gryffondor", "Harry Potter")
    baguette_drago = BaguetteMagique("Serpentard", "Drago Malefoy")
    baguette_luna = BaguetteMagique("Serdaigle", "Luna Lovegood")
    
    # Enregistrement des baguettes
    baguette_harry.enregistrer_baguette()
    baguette_drago.enregistrer_baguette()
    baguette_luna.enregistrer_baguette()
    
    # Affichage des baguettes enregistrées
    print("Baguettes enregistrées:")
    for proprietaire, infos in BaguetteMagique.baguettes.items():
        print(f"Baguette de {proprietaire}: {infos}")
    
    # Test des sorts
    print("\nTest des sorts:")
    baguette_harry.expelliarmus()
    
    try:
        baguette_harry.avada_kedavra()  # Devrait lever une exception
    except Exception as e:
        print(f"Exception: {e}")
    
    baguette_drago.avada_kedavra()
