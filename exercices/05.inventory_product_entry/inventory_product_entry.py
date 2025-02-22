# Vous allez créer une classe InventoryProductEntry qui a pour role 
# de représenter une entrée d'inventaire pour un produit spécifique.
from product_classes import Product

class InventoryProductEntry:
    # Initialisation de la classe, en prenant en argument un objet Product et une quantité initiale
    def __init__(self, product:Product, quantity):
        self.product = product
        self.quantity = quantity
        self.sales = 0
        self.expenses = 0

        """
        'product' : un objet de type produit qui rassemble les différents attributs et caractéristiques de ce dernier
        'quantity' : un entier qui représente le nombre des pièces du produit en question
        """
        # Initialisation des variables
        
        """
        Vous devez initialiser deux variables. 
        la variable 'sales' qui stocke le total des revenues des ventes du produit
        la variable 'expenses' qui stocke le total des dépenses pour restocker le produit
        
        """

    #Méthode Sell
    """
    La méthode sell est utilisée pour retirer la quantité vendue du produit depuis le stock.
    Elle met également à jour les ventes totales pour le produit.
    
    """
    def check_quantity(self, quantity):
        if self.quantity >= quantity:
          print("Il y a suffisamment de quantité disponible.")
        else:
          print("Il n'y a pas suffisamment de quantité disponible.")

    def sell(self, quantity):
        #Avant de mettre à jour l'état du stocke du produit, on doit vérifier si on a déjà une quantité suffisante à vendre.
        if self.check_quantity(quantity):
          self.quantity -= quantity  #Réduire la quantité en stock par la quantité demandée
          self.sales += quantity * self.product.price #Ajouter le revenue total de la vente à la variable 'sales' en multipliant la quantité vendue par le prix du produit
          return True
        else:
          print(f'Le stock du produit' [Product],'est insuffisant.')
          return False
       
            
    """
        En utilisant des conditions, vérifier: 

        SI la quantité en stock est inférieure à la quantité demandée:
            Afficher "Le stock du produit [nom du produit] est insuffisant."
            Retourner Faux
        SINON:
            Réduire la quantité en stock par la quantité demandée
            Ajouter le revenue total de la vente à la variable 'sales' en multipliant la quantité vendue par le prix du produit
            Retourner Vrai
        
        """
    
    #Méthode Restock
    """
    La méthode restock est utilisée pour augmenter la quantité en stock lorsqu'un nouveau stock de produit est reçu. 
    Elle met également à jour les dépenses totales pour restocker ce produit.
    """
    def restock(self, quantity):
        self.quantity += quantity
        self.expenses+= quantity * self.product.price
        return True
    
    """
        Ajouter la quantité reçue à la quantité en stock
        Ajouter le coût total de la nouvelle quantité reçue  à la variable 'expenses' en multipliant la quantité reçue par le coût du produit
        """

    #Méthode repr
    """
    La méthode repr est utilisée pour fournir une représentation en chaîne de caractères de l'objet InventoryProductEntry, 
    qui contient des informations utiles telles que le nom du produit, la marque, la quantité en stock et le prix du produit.

    """
    def __repr__(self):
        # Retourner une chaîne de caractères formatée contenant le nom du produit, la marque, la quantité en stock et le prix du produit.
        return f"{self.product.name} ({self.product.brand}): {self.quantity} en stock à {self.product.price} par unité."