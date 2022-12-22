"""
La classe JoueurOrdinateur

Hérite de Joueur et contient une "intelligence artificielle" extrêmement rudimentaire.
"""

from random import randint
from jeu.joueur import Joueur


#### DÉBUT DÉFI JOUEUR ORDINATEUR ####


class JoueurOrdinateur(Joueur):  # N'oubliez pas d'hériter de Joueur !!
    """
    # Args : numero joeur, des_initiaux, arene

    """

    def __init__(self, numero_joueur, des_initiaux, arene):
        # Supprimer la ligne du raise, et ajoutez l'appel à super().__init__
        super().__init__(numero_joueur, des_initiaux, arene)
        # raise ValueError("Le défi Joueur Ordinateur n'a pas encore été réalisé!")

    # Écrivez les 4 méthodes demandées.

    def choisir_coordonnees(self):
        return super().piger_coordonnees()

    def choisir_angle(self):
        return super().piger_angle()

    def choisir_puissance(self):
        return super().piger_puissance()

    def decision_continuer(self):
        if randint(0, 3) != 0:
            return True
        else:
            return False

    #### FIN DÉFI JOUEUR ORDINATEUR ####
