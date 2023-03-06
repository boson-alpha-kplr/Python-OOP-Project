class Products:
    def __init__(self, cost, price, marque):
        self.cost = cost
        self.price = price
        self.marque = marque

class Meubles(Products):
    def __init__(self, cost, price, marque, materiaux, couleur, dimension):
        super().__init__(cost, price, marque)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimension = dimension 
    def afficher_attributs(self):
        print("Attributs pour le Meubles :")
        print("- Cost :", self.cost)
        print("- Price :", self.price)
        print("- Marque :", self.marque)
        print("- Matriaux :", self.materiaux)
        print("- Couleur :", self.marque)
        print("- Dimension :", self.dimension)

class Canape (Meubles):
    def __init__(self, cost, price, marque, materiaux, couleur, dimension, nom):
        super().__init__(cost, price, marque, materiaux, couleur, dimension)
        self.nom = nom
    def afficher_attributs(self):
        super().afficher_attributs()
        print("- Nom :", self.nom)
class Chaise (Meubles):
    def __init__(self, cost, price, marque, materiaux, couleur, dimension, nom):
        super().__init__(cost, price, marque, materiaux, couleur, dimension)
        self.nom = nom
    def afficher_attributs(self):
        super().afficher_attributs()
        print("- Nom :", self.nom)
class Table (Meubles):
    def __init__(self, cost, price, marque, materiaux, couleur, dimension):
        super().__init__(cost, price, marque, materiaux, couleur, dimension)
    
    def afficher_attributs(self):
        super().afficher_attributs()

# Création d'une instance de chaque classe
Canape1 = Canape(1000, 2000, "OKLM", "Cuir","Blanc", 200*100*80,"Canape")
Canape2 = Canape(800, 1600, "SIESTA", "Tissu","Bleu", 150*90*70,"Canape")
Chaise1 = Chaise(50, 100, "PEPOUSE", "Plastique","Rouge", 50*50*70,"Chaise")
Chaise2 = Chaise(75, 150, "PEPOUSE", "Metal","Gris", 60*60*80,"Chaise")
Table1 = Table(350, 700, "TEX", "Verre","Transparent", 120*60*75)
Table2 = Table(250, 500, "TEX", "Bois","Chêne", 150*80*75)


Canape1.afficher_attributs()
Canape2.afficher_attributs()
Chaise1.afficher_attributs()
Chaise2.afficher_attributs()
Table1.afficher_attributs()
Table2.afficher_attributs()