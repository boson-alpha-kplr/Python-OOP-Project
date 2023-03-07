import json
from unidecode import unidecode
from treelib import Tree
import os
# Fonction pour charger les données JSON depuis un fichier et les convertir en dictionnaire Python
def json_dict_from_file():
# Get the directory path of the current Python file
    local_path = os.path.dirname(os.path.abspath(__file__))
    # Chargement des données JSON à partir du fichier dans un dictionnaire python
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    
    # il est nécessaire de reconvertir le dictionnaire en chaine de caractere pour le traiter ensuite
    json_str = json.dumps(json_data)

    # Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
    json_data = (unidecode(json_str))

    # Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
    # Le dictionnaire python est plus pratique à manipuler que la chaine de caractère car il est structuré
    json_dict = json.loads(json_data)

    return json_dict

# Fonction pour créer un arbre à partir d'un dictionnaire Python
def create_tree_from_dict(tree, parent_node_id, json_dict):
    for key, value in json_dict.items():
        if isinstance(value, dict):
            # Créer un nouveau noeud pour la clé courante du dictionnaire
            new_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            
            # Créer récursivement le sous-arbre pour le dictionnaire courant
            create_tree_from_dict(tree, new_node_id, value)
        else:
            # Créer un nouveau noeud pour la feuille courante du dictionnaire
            leaf_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=f"{key}: {value}", identifier=leaf_node_id, parent=parent_node_id)


def main():
    my_tree = Tree()
    # Créer le noeud racine pour l'arbre
    my_tree.create_node(tag="Product", identifier="product")

    # Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    json_dict = json_dict_from_file()
    create_tree_from_dict(my_tree, "product", json_dict)

    # Afficher l'arbre
    my_tree.show()

if __name__ == '__main__':
    # Appeler la fonction principale
    main()