#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

"""Classe GrillesDeJeu.

Cette classe sert à stocker les différentes grilles de jeu auxquelles le joueur aura accès.
Elle ne nécessite pas d'instancier un objet. Elle ne contient que des attributs et méthodes de classe.
L'appel d'une fonction de cette classe se fait comme suit : 'GrillesDeJeu.fonction()'
"""


class GrillesDeJeu:

    grillesfacile = [
        [0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 0, 0, 0, 6, 1, 3, 0, 0, 4, 9, 0, 5, 7, 6, 5, 0, 0, 0, 0, 0, 0, 2, 9,
         1, 2, 4, 0, 3, 6, 8, 5, 8, 0, 0, 0, 0, 0, 0, 9, 3, 4, 2, 0, 8, 1, 0, 0, 3, 9, 3, 0, 0, 0, 9, 7, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 7, 1, 0, 6, 9, 0, 8, 0, 0, 0, 2, 0, 0, 6, 4, 1, 0, 2, 9, 0, 0, 7, 0, 0, 0, 0, 5, 2, 3, 4, 0, 5,
         0, 0, 7, 0, 4, 0, 0, 8, 0, 2, 4, 8, 3, 0, 0, 0, 0, 2, 0, 0, 1, 4, 0, 9, 7, 3, 0, 0, 9, 0, 0, 0, 8, 0, 5, 7, 0,
         5, 6, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 8, 0, 0, 3, 3, 2, 0, 7, 9, 0, 0, 1, 5, 0, 0, 0, 4, 3, 0, 0, 0, 6, 0, 5, 9, 1, 8, 0, 0, 0, 0, 0,
         1, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 2, 9, 5, 8, 0, 5, 0, 0, 0, 7, 2, 0, 0, 0, 7, 8, 0, 0, 5, 1, 0, 4, 2, 1, 0,
         0, 3, 0, 0, 7, 0, 0]]
    grillesfacile_solution = [
        [7, 9, 8, 1, 6, 5, 3, 2, 4, 2, 4, 5, 7, 3, 8, 9, 1, 6, 1, 3, 6, 2, 4, 9, 8, 5, 7, 6, 5, 3, 9, 8, 1, 4, 7, 2, 9,
         1, 2, 4, 7, 3, 6, 8, 5, 8, 7, 4, 6, 5, 2, 1, 9, 3, 4, 2, 7, 8, 1, 6, 5, 3, 9, 3, 6, 1, 5, 9, 7, 2, 4, 8, 5, 8,
         9, 3, 2, 4, 7, 6, 1],
        [3, 5, 2, 4, 8, 7, 1, 9, 6, 9, 7, 8, 5, 6, 1, 2, 3, 4, 6, 4, 1, 3, 2, 9, 5, 8, 7, 8, 6, 7, 9, 5, 2, 3, 4, 1, 5,
         9, 3, 7, 1, 4, 6, 2, 8, 1, 2, 4, 8, 3, 6, 7, 5, 9, 2, 8, 6, 1, 4, 5, 9, 7, 3, 4, 1, 9, 2, 7, 3, 8, 6, 5, 7, 3,
         5, 6, 9, 8, 4, 1, 2],
        [9, 6, 5, 2, 1, 8, 4, 7, 3, 3, 2, 4, 7, 9, 6, 8, 1, 5, 8, 7, 1, 4, 3, 5, 2, 9, 6, 6, 5, 9, 1, 8, 7, 3, 2, 4, 2,
         1, 8, 5, 4, 3, 9, 6, 7, 4, 3, 7, 6, 2, 9, 5, 8, 1, 5, 4, 6, 8, 7, 2, 1, 3, 9, 7, 8, 3, 9, 5, 1, 6, 4, 2, 1, 9,
         2, 3, 6, 4, 7, 5, 8]]
    grillesmoyen = []
    grillesmoyen_solution = []
    grilleshardcore = []
    grilleshardcore_solution = []

    def get_nb_grilles(cls, niveau):
        if niveau == 1:
            return len(cls.grillesfacile)
        elif niveau == 2:
            return len(cls.grillesmoyen)
        else:
            return len(cls.grilleshardcore)
    get_nb_grilles = classmethod(get_nb_grilles)

    def get_grille(cls, niveau, ngrille):
        if niveau == 1:
            return cls.grillesfacile[ngrille - 1]
        elif niveau == 2:
            return cls.grillesmoyen[ngrille - 1]
        else:
            return cls.grilleshardcore[ngrille - 1]
    get_grille = classmethod(get_grille)
