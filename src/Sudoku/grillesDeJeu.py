#!/usr/bin/python3.7
# -*-coding:Utf-8 -*
import random
import math

"""Classe GrillesDeJeu.

Cette classe sert à stocker les différentes grilles de jeu auxquelles le joueur aura accès.
Elle ne nécessite pas d'instancier un objet. Elle ne contient que des attributs et méthodes de classe.
L'appel d'une fonction de cette classe se fait comme suit : 'GrillesDeJeu.fonction()'
"""


class GrillesDeJeu:

    # Grille pré-faites
    grilles = [[7, 9, 8, 1, 6, 5, 3, 2, 4, 2, 4, 5, 7, 3, 8, 9, 1, 6, 1, 3, 6, 2, 4, 9, 8, 5, 7, 6, 5, 3, 9, 8, 1, 4, 7, 2, 9,
     1, 2, 4, 7, 3, 6, 8, 5, 8, 7, 4, 6, 5, 2, 1, 9, 3, 4, 2, 7, 8, 1, 6, 5, 3, 9, 3, 6, 1, 5, 9, 7, 2, 4, 8, 5, 8,
     9, 3, 2, 4, 7, 6, 1],
    [3, 5, 2, 4, 8, 7, 1, 9, 6, 9, 7, 8, 5, 6, 1, 2, 3, 4, 6, 4, 1, 3, 2, 9, 5, 8, 7, 8, 6, 7, 9, 5, 2, 3, 4, 1, 5,
     9, 3, 7, 1, 4, 6, 2, 8, 1, 2, 4, 8, 3, 6, 7, 5, 9, 2, 8, 6, 1, 4, 5, 9, 7, 3, 4, 1, 9, 2, 7, 3, 8, 6, 5, 7, 3,
     5, 6, 9, 8, 4, 1, 2],
    [9, 6, 5, 2, 1, 8, 4, 7, 3, 3, 2, 4, 7, 9, 6, 8, 1, 5, 8, 7, 1, 4, 3, 5, 2, 9, 6, 6, 5, 9, 1, 8, 7, 3, 2, 4, 2,
     1, 8, 5, 4, 3, 9, 6, 7, 4, 3, 7, 6, 2, 9, 5, 8, 1, 5, 4, 6, 8, 7, 2, 1, 3, 9, 7, 8, 3, 9, 5, 1, 6, 4, 2, 1, 9,
     2, 3, 6, 4, 7, 5, 8],
     [6, 7, 2, 1, 9, 5, 8, 3, 4, 8, 4, 5, 2, 3, 6, 7, 1, 9, 3, 1, 9, 7, 4, 8, 2, 6, 5, 5, 3, 4, 6, 8, 9, 1, 2, 7, 1,
      2, 6, 5, 7, 3, 4, 9, 8, 9, 8, 7, 4, 2, 1, 6, 5, 3, 2, 5, 8, 9, 6, 4, 3, 7, 1, 4, 6, 1, 3, 5, 7, 9, 8, 2, 7, 9,
      3, 8, 1, 2, 5, 4, 6],
     [9, 4, 2, 1, 3, 8, 5, 6, 7, 8, 6, 3, 7, 9, 5, 1, 2, 4, 7, 1, 5, 4, 6, 2, 8, 3, 9, 6, 3, 7, 5, 4, 9, 2, 1, 8, 5,
      9, 1, 8, 2, 6, 7, 4, 3, 2, 8, 4, 3, 1, 7, 6, 9, 5, 3, 7, 6, 2, 5, 4, 9, 8, 1, 4, 2, 8, 9, 7, 1, 3, 5, 6, 1, 5,
      9, 6, 8, 3, 4, 7, 2],
      [6, 1, 9, 5, 3, 8, 4, 7, 2, 3, 7, 8, 1, 4, 2, 5, 9, 6, 4, 2, 5, 9, 6, 7, 3, 1, 8, 5, 6, 1, 7, 2, 9, 8, 3, 4, 9,
       3, 2, 4, 8, 1, 7, 6, 5, 8, 4, 7, 6, 5, 3, 9, 2, 1, 1, 8, 6, 3, 9, 5, 2, 4, 7, 7, 5, 3, 2, 1, 4, 6, 8, 9, 2, 9,
       4, 8, 7, 6, 1, 5, 3],
      [4, 7, 9, 8, 3, 5, 6, 1, 2, 6, 2, 5, 7, 4, 1, 8, 3, 9, 1, 3, 8, 6, 2, 9, 5, 7, 4, 8, 4, 6, 9, 7, 3, 2, 5, 1, 9,
       1, 7, 2, 5, 4, 3, 8, 6, 2, 5, 3, 1, 8, 6, 9, 4, 7, 3, 9, 2, 5, 1, 7, 4, 6, 8, 7, 8, 4, 3, 6, 2, 1, 9, 5, 5, 6,
       1, 4, 9, 8, 7, 2, 3]]

    # Fonction get_grille
    #
    # cls : tableau des grilles
    # niveau : niveau de difficulté
    # grille : grille dans laquelle enregistrer la grille choisie
    #
    # Fnction permettant de récuperer une grille du tableau de grilles cls et d'enlever aléatoirement des
    # nombres enfonction de la difficulté
    #
    def get_grille(cls, niveau, grille):

        g = random.choice(cls.grilles)

        diff = 0.5 + (niveau-1)*0.1
        for x in range(0, grille.largeur):
            for y in range(0, grille.hauteur):
                if random.random() > diff:
                    grille.getCaseByCoords(x, y).setNumber(g[y*grille.largeur+x])
        return grille
    get_grille = classmethod(get_grille)
