#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

from random import *

"""Fichier d'initialisation du module Poker.

Ce fichier contient la classe Poker qui initialise une partie de poker.
La classe est adaptée à la fois pour une utilisation sur interface en lignes de commandes,
et pour une utilisation sur interface graphique.
"""


class Partie:
    """Classe principal du module Poker, permet de lancer le jeu.

    Pour démarrer une partie de poker, simplement saisir 'Partie()'.

    Attributs :
    listeGrilleMain (Liste des grilles correspondantes aux mains des joueurs)
    grilleTable (Grille contenant les 5 cartes de la table)

    pileCartesJeu (Liste des cartes triées aléatoirement. pileCartes[0] = première carte de la pile, etc.)
    001 : As de Coeur, 101: As de Pique, 201: As de Carreau, 301 : As de Trèfle, 313: Roi de Trèfle
    pileCartesBrulees (Liste des cartes brulées, c'est-à-dire retirées du jeu)

    listeJoueurs (Liste d'objets de classe Joueur)
    petiteBlinde (Liste contenant l'ID du joueur associé et la valeur de la petite blinde)
    grosseBlinde (Liste contenant l'ID du joueur associé et la valeur de la grosse blinde)

    pot (Contient la mise commune)

    tour (int contenant le numéro du tour. 0 (1er tour), 1 (2ème tour) ou 2 (3ème tour)
    """

    def __init__(self):
        """Définition du joueur petite mise et grande mise"""

        # Initialiser et mélanger cartes
        self.pilecartes = [0 for i in range(52)]
        self.initialiser_cartes()
        self.pilecartes = self.melanger_cartes(self.pilecartes)
        L = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dâme', 'Roi']
        print(self.pilecartes)

        # Distribution des cartes

    def initialiser_cartes(self):
        # Trèfle (0), coeur (1), pique (2), carreau (3)
        i = 1
        s = 0  # Initialiser à Coeur
        ind = 0
        while s <= 3:
            while i <= 13:
                self.pilecartes[ind] = s * 100 + i
                i += 1
                ind += 1
            i = 1
            s += 1

    @staticmethod
    def melanger_cartes(pilecartes):
        piletemp = []

        c = 51
        while c >= 0:
            selec = randint(0, c)
            piletemp.append(pilecartes[selec])
            pilecartes.remove(pilecartes[selec])
            c -= 1

        return piletemp


Partie()
