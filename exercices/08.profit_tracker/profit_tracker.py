# La classe ProfitTracker est utilisée pour suivre les profits du magasin.

from product_classes import Product


class ProfitTracker:

    # Le constructeur initialise la variable balance (solde)
    def __init__(self):
        # Créer une variable 'balance' et l'initialiser à 1000 euros
        self.balance= '1000 euros'

    #Méthode buy_product 
    """   
    La méthode buy_product est utilisée pour acheter un produit et mettre à jour le coût total et le solde.
    """     

    def buy_product(self, product: Product, quantity): 
        if self.check_stock_balance(self.balance, 2):
        self.inventory_manager.add_product(self.chaise, 5)
        self.inventory_manager.buy_product(self.chaise, 5)
        self.assertEqual(self.inventory_manager.inventory[self.chaise], 0)
        self.assertEqual(self.inventory_manager.expenses, 25.00)
        
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
        
        # Met à jour le solde en ajoutant le prix du produit multiplié par la quantité vendue


