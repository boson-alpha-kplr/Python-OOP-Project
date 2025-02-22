# La classe ProfitTracker est utilisée pour suivre les profits du magasin.

from inventory_product_entry import InventoryProductEntry
from product_classes import Product


class ProfitTracker:

    # Le constructeur initialise la variable balance (solde)
    def __init__(self):
        # Créer une variable 'balance' et l'initialiser à 1000 euros
        self.balance= 1000

    #Méthode buy_product 
    """   
    La méthode buy_product est utilisée pour acheter un produit et mettre à jour le coût total et le solde.
    """     

    def buy_product(self, product: Product, quantity): 
        total_price= quantity * product.price
        if self.balance<total_price:
            print('erreur!')
            return False
        else:
            self.balance-= total_price
            return True   
    """
        Vérifie si le solde est suffisant pour acheter la quantité demandée de produit
            Si le solde est insuffisant:
                affiche un message d'erreur 
                retourne False pour indiquer que l'achat a échoué.
            Sinon, si le solde est suffisant:
                met à jour le solde en soustrayant le coût du produit multiplié par la quantité achetée
                retourne True pour indiquer que l'achat a réussi
        """
        
    #Méthode sell_product 
    """   
    La méthode sell_product est utilisée pour vendre un produit et mettre à jour le solde.
    """  
 
    def sell_product(self, product: Product, quantity):
        self.balance+= product.price * quantity
        
        # Met à jour le solde en ajoutant le prix du produit multiplié par la quantité vendue


