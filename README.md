## Fonctionnalités :
Pouvoir traiter interactivement et localement les données de la BD.
Cela fait appel à 1 requête SQL immuable (quelque soit l'année) par table.

Le notebook permet de parcourir la BD, faire des interrogations, des graphiques
(via par exemple `mathplotlib`), etc.

## Pré-requis :
* python 3
* python pandas
* python jupyter
* httpie

## Contenu  :
* `dbwalk.ipynb` : le notebook ; pour réaliser les traitements interactifs
* `dbwalk.py` : un ensemble de routines sur lesquelles s'appuie le notebook ; contrairement au notebook, ce module n'a pas a être modifié par l'utilisateur final
* `settings.py` : configuration de `dbwalk.py`
* `secret.py` : paramètres privés

## Utilisation :
* cloner ce dépôt
* renommer le fichier `secret.py.in` en `secret.py` et initialiser les variables qu'il contient
* (optionnel) lancer le module `dbwalk.py` pour le tester 
* l'utilisation normale se fait via le notebook `dbwalk.ipynb`, à exécuter sous Jupyter.
