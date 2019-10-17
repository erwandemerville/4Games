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

    """grillesfacile = [
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
    grillesmoyen = [
        [6, 0, 0, 0, 0, 5, 0, 0, 4, 0, 0, 5, 2, 3, 0, 7, 0, 0, 0, 1, 0, 0, 4, 0, 2, 0, 0, 0, 0, 4, 6, 0, 0, 0, 2, 7, 0,
         2, 0, 5, 0, 3, 0, 9, 0, 9, 8, 0, 0, 0, 1, 6, 0, 0, 0, 0, 8, 0, 6, 0, 0, 7, 0, 0, 0, 1, 0, 5, 7, 9, 0, 0, 7, 0,
         0, 8, 0, 0, 0, 0, 6],
        [9, 0, 0, 0, 3, 0, 5, 0, 7, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 4, 6, 0, 8, 0, 9, 0, 0, 0, 0, 4, 0, 2, 1, 0, 5,
         0, 1, 0, 2, 0, 7, 0, 3, 0, 8, 4, 0, 1, 0, 0, 0, 0, 3, 0, 6, 0, 5, 4, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 1, 0,
         9, 0, 8, 0, 0, 0, 2]]
    grillesmoyen_solution = [
        [6, 7, 2, 1, 9, 5, 8, 3, 4, 8, 4, 5, 2, 3, 6, 7, 1, 9, 3, 1, 9, 7, 4, 8, 2, 6, 5, 5, 3, 4, 6, 8, 9, 1, 2, 7, 1,
         2, 6, 5, 7, 3, 4, 9, 8, 9, 8, 7, 4, 2, 1, 6, 5, 3, 2, 5, 8, 9, 6, 4, 3, 7, 1, 4, 6, 1, 3, 5, 7, 9, 8, 2, 7, 9,
         3, 8, 1, 2, 5, 4, 6],
        [9, 4, 2, 1, 3, 8, 5, 6, 7, 8, 6, 3, 7, 9, 5, 1, 2, 4, 7, 1, 5, 4, 6, 2, 8, 3, 9, 6, 3, 7, 5, 4, 9, 2, 1, 8, 5,
         9, 1, 8, 2, 6, 7, 4, 3, 2, 8, 4, 3, 1, 7, 6, 9, 5, 3, 7, 6, 2, 5, 4, 9, 8, 1, 4, 2, 8, 9, 7, 1, 3, 5, 6, 1, 5,
         9, 6, 8, 3, 4, 7, 2]]
    grillesdifficile = [
        [0, 0, 0, 0, 3, 0, 0, 7, 2, 0, 0, 8, 0, 4, 2, 0, 9, 0, 0, 0, 0, 9, 0, 0, 3, 0, 0, 5, 6, 0, 0, 2, 0, 0, 3, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 5, 0, 0, 2, 1, 0, 0, 6, 0, 0, 5, 0, 0, 0, 0, 5, 0, 2, 1, 0, 6, 0, 0, 2, 9,
         0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 6, 0, 0, 6, 0, 0, 0, 0, 1, 0, 0, 9, 1, 3, 0, 0, 0, 9, 5, 0, 0, 0, 4, 0, 9, 0, 0, 0, 0, 0, 9,
         0, 7, 0, 5, 0, 3, 0, 6, 0, 0, 0, 0, 0, 6, 0, 4, 0, 0, 0, 2, 5, 0, 0, 0, 6, 8, 7, 0, 0, 3, 0, 0, 0, 0, 5, 0, 0,
         1, 0, 0, 8, 0, 0, 0]]
    grillesdifficile_solution = [
        [6, 1, 9, 5, 3, 8, 4, 7, 2, 3, 7, 8, 1, 4, 2, 5, 9, 6, 4, 2, 5, 9, 6, 7, 3, 1, 8, 5, 6, 1, 7, 2, 9, 8, 3, 4, 9,
         3, 2, 4, 8, 1, 7, 6, 5, 8, 4, 7, 6, 5, 3, 9, 2, 1, 1, 8, 6, 3, 9, 5, 2, 4, 7, 7, 5, 3, 2, 1, 4, 6, 8, 9, 2, 9,
         4, 8, 7, 6, 1, 5, 3],
        [4, 7, 9, 8, 3, 5, 6, 1, 2, 6, 2, 5, 7, 4, 1, 8, 3, 9, 1, 3, 8, 6, 2, 9, 5, 7, 4, 8, 4, 6, 9, 7, 3, 2, 5, 1, 9,
         1, 7, 2, 5, 4, 3, 8, 6, 2, 5, 3, 1, 8, 6, 9, 4, 7, 3, 9, 2, 5, 1, 7, 4, 6, 8, 7, 8, 4, 3, 6, 2, 1, 9, 5, 5, 6,
         1, 4, 9, 8, 7, 2, 3]]"""

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

    """def get_nb_grilles(cls, niveau):
        if niveau == 1:
            return len(cls.grillesfacile)
        elif niveau == 2:
            return len(cls.grillesmoyen)
        else:
            return len(cls.grillesdifficile)"""

    #get_nb_grilles = classmethod(get_nb_grilles)

    def get_grille(cls, niveau, grille):
        """if niveau == 1:
            return cls.grillesfacile[ngrille - 1]
        elif niveau == 2:
            return cls.grillesmoyen[ngrille - 1]
        else:
            return cls.grillesdifficile[ngrille - 1]"""

        g = random.choice(cls.grilles)

        diff = 0.5 + (niveau-1)*0.1
        for x in range(0, grille.largeur):
            for y in range(0, grille.hauteur):
                if random.random() > diff:
                    grille.getCaseByCoords(x, y).setNumber(g[y*grille.largeur+x])
        return grille
    get_grille = classmethod(get_grille)

    """def get_grille_solution(cls, niveau, ngrille):
        if niveau == 1:
            return cls.grillesfacile_solution[ngrille - 1]
        elif niveau == 2:
            return cls.grillesmoyen_solution[ngrille - 1]
        else:
            return cls.grillesdifficile_solution[ngrille - 1]"""

    #get_grille_solution = classmethod(get_grille_solution)

class grilleGenerator:
    ""

    @staticmethod
    def generer(grille, diff):
        print("Création de la grille en cours")
        for i in range(1,10):
            if not(grilleGenerator.genererNombre(grille, i)):
                #grilleGenerator.viderGrille(grille)
                #return grilleGenerator.generer(grille, diff)
                return grille

        """diff = 0.5 - (diff-1)*0.1
        for x in range(0, grille.largeur):
            for y in range(0, grille.hauteur):
                if random.random() > diff:
                    grille.getCaseByCoords(x, y).setNumber(0)"""
        return grille

    @staticmethod
    def genererNombre(grille, nb):
        print("Génération du chiffre " + str(nb) + " dans la grille")
        for y in range(0,3):
            for x in range(0,3):
                print("Génération du chiffre " + str(nb) + " dans la sous-grille " + str((x,y)))
                point = (1+x*3, 1+y*3)
                tab2 = grilleGenerator.getSousGrille(grille, point)
                tab2.append(point)
                tab = grilleGenerator.getCasesVide(grille, tab2)
                print("Y1 : " + str(tab) + " : " + str(nb))
                var = random.choice(tab)

                vvv = grille.getCaseByCoords(var[0],var[1]).getNumber()
                hasBackTrack = False
                grille.getCaseByCoords(var[0],var[1]).setNumber(nb)
                while not(grilleGenerator.verifierNombre(grille, var)):
                    if vvv == 0:
                        grille.getCaseByCoords(var[0],var[1]).setNumber(0)
                    tab.remove(var)
                    if len(tab) == 0:
                        print("EMPTY (266) : " + str(tab) + " : " + str(nb) + " : " + str(var) + " : " + str(point))
                        if not(hasBackTrack):
                            hasBackTrack = True
                            print("BACKTRACK V1 : " + str(point))
                            if not(grilleGenerator.backtrackError(grille, grilleGenerator.getPreviousIncidentPoint(point, point), nb, var)):
                                print("BACKTRACK FAILURE : " + str(point))
                                return False
                        else:
                            print("BACKTRACK FAILURE 2 : " + str(point))
                            return False
                        tab = grilleGenerator.getCasesVide(grille, tab2)
                    var = random.choice(tab)
                    vvv = grille.getCaseByCoords(var[0],var[1]).getNumber()
                    grille.getCaseByCoords(var[0],var[1]).setNumber(nb)
                print("Y3 : " + str(tab) + " : " + str(nb) + " : " + str(var))

        return True

    @staticmethod
    def backtrackError(grille, point, nb, pt_verif):

        if point == None:
            print("BACKTRACK NONE : " + str(point))
            return False
        #if (point[0] < 3 and point[1] < 3):
            #raise ValueError("grilleGenerator.backtrackError second argument must not be equal to (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1) or (2,2)")
            #return False
        #elif point[0] < 3:
            #point = (8, point[1]-3)
        #else:
            #point = (point[0]-3, point[1])
        print("Begin BackTrack for " + str(point) + " : " + str(nb))

        grille.getCaseByCoords(pt_verif[0], pt_verif[1]).setNumber(nb)
        if grilleGenerator.verifierNombre(grille, (pt_verif[0], pt_verif[1])):
            grille.getCaseByCoords(pt_verif[0], pt_verif[1]).setNumber(0)
            return grilleGenerator.backtrackError(grille, point, nb, pt_verif)

        point2 = (point[0], point[1])
        tab2 = grilleGenerator.getSousGrille(grille, point2)
        tab2.append(point2)
        pt = grilleGenerator.containNbSousGrille(grille, tab2, nb)
        #if (grilleGenerator.getPointIncidence(pt, pt_verif) == 1):

        print("test Tab : " + str(tab2) + " : " + str(pt))
        tab2.remove(pt)
        grille.getCaseByCoords(pt[0],pt[1]).setNumber(0)
        tab = grilleGenerator.getCasesVide(grille, tab2)

        var = random.choice(tab)
        vvv = grille.getCaseByCoords(var[0],var[1]).getNumber()
        hasBackTrack = False
        grille.getCaseByCoords(var[0],var[1]).setNumber(nb)
        while not(grilleGenerator.verifierNombre(grille, var)):
            if vvv == 0:
                grille.getCaseByCoords(var[0],var[1]).setNumber(0)
            tab.remove(var)
            if len(tab) == 0:
                print("EMPTY (320) : " + str(tab) + " : " + str(nb) + " : " + str(var) + " : " + str(point))
                if not(hasBackTrack):
                    hasBackTrack = True
                    print("BACKTRACK V2 : " + str(point) + " : " + str(hasBackTrack))
                    if not(grilleGenerator.backtrackError(grille, grilleGenerator.getPreviousIncidentPoint(point, pt_verif), nb, pt_verif)):
                        if not(grilleGenerator.backtrackError(grille, grilleGenerator.getPreviousIncidentPoint(point, pt_verif), nb, point)):
                            return False
                        else:
                            grille.getCaseByCoords(pt_verif[0], pt_verif[1]).setNumber(nb)
                            if (grilleGenerator.verifierNombre(grille, (pt_verif[0], pt_verif[1]))):
                                grille.getCaseByCoords(pt_verif[0], pt_verif[1]).setNumber(0)
                                break
                            else:
                                if not(grilleGenerator.backtrackError(grille, grilleGenerator.getPreviousIncidentPoint(point, pt_verif), nb, pt_verif)):
                                    if not(grilleGenerator.backtrackError(grille, grilleGenerator.getPreviousIncidentPoint(point, pt_verif), nb, point)):
                                        return False
                    else:
                        grille.getCaseByCoords(pt_verif[0], pt_verif[1]).setNumber(nb)
                        if (grilleGenerator.verifierNombre(grille, (pt_verif[0], pt_verif[1]))):
                            grille.getCaseByCoords(pt_verif[0], pt_verif[1]).setNumber(0)
                            break
                        else:
                            if not(grilleGenerator.backtrackError(grille, grilleGenerator.getPreviousIncidentPoint(point, pt_verif), nb, pt_verif)):
                                if not(grilleGenerator.backtrackError(grille, grilleGenerator.getPreviousIncidentPoint(point, pt_verif), nb, point)):
                                    return False
                else:
                    return False
                tab = grilleGenerator.getCasesVide(grille, tab2)
            var = random.choice(tab)
            vvv = grille.getCaseByCoords(var[0],var[1]).getNumber()
            grille.getCaseByCoords(var[0],var[1]).setNumber(nb)
        print("BACKTRACK SUCCESS : " + str(point))
        return True

    @staticmethod
    def getPreviousPoint(point):
        if (point[0] < 3 and point[1] < 3):
            raise ValueError("grilleGenerator.getPreviousPoint argument must not be equal to (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1) or (2,2)")
            return False
        elif point[0] < 3:
            return (8, point[1]-3)
        else:
            return (point[0]-3, point[1])

    @staticmethod
    def getPreviousIncidentPoint(point, target):
        temp = point
        while grilleGenerator.getPointIncidence(temp, target) == 0:
            try:
                temp = getPeviousPoint(temp)
            except:
                return None
        return temp

    @staticmethod
    def getPointIncidence(point, target):
        nx = round((point[0]-point[0]%3)/3)
        ny = round((point[1]-point[1]%3)/3)
        nx2 = round((target[0]-target[0]%3)/3)
        ny2 = round((target[1]-target[1]%3)/3)
        if (nx == nx2 and ny == ny2):
            return 0 # pas d'incidence
        elif (nx == nx2):
            return 1 # incidence horizontale
        elif (ny == ny2):
            return 2 # incidence verticale
        else:
            return 0 # pas d'incidence

    @staticmethod
    def getCasesVide(grille, tab):
        ret = []
        for i in tab:
            if grille.getCaseByCoords(i[0],i[1]).getNumber() == 0:
                ret.append(i)
        return ret

    @staticmethod
    def corrigerLigne(grille, y):
        tab = grilleGenerator.missingNumberLigne(grille,y)
        for x in range(grille.largeur):
            if grille.getCaseByCoords(x,y).getNumber() == 0:
                for i in tab:
                    grille.getCaseByCoords(x,y).setNumber(i)
                    if GrillesDeJeu.verifierNombre(grille, (x,y)):
                        tab.remove(i)
                        break
        return len(grilleGenerator.missingNumberLigne(grille,y)) == 0

    @staticmethod
    def viderGrille(grille):
        for i in range(grille.largeur*grille.hauteur):
            grille.getCase(i).setNumber(0)

    @staticmethod
    def viderSousGrille(grille, point):
        nx = round((point[0]-point[0]%3)/3)
        ny = round((point[1]-point[1]%3)/3)
        for y in range(0,3):
            for x in range(0,3):
                grille.getCaseByCoords(nx+x,ny+y).setNumber(0)

    @staticmethod
    def verifierSousGrille(grille, point):
        nx = round((point[0]-point[0]%3)/3)
        ny = round((point[1]-point[1]%3)/3)
        tab2 = []
        for y in range(0,3):
            for x in range(0,3):
                if not(grilleGenerator.verifierNombre(grille, (nx+x,ny+y))):
                    tab2.append((nx+x,ny+y))
        return tab2

    # Fonction getSousGrille
    #
    # grille : la grille sur laquelle vérifier.
    # point : tuple représentant les coordonnées du nombre a vérifier. ex (x, y)
    #
    # Cette fonction retourne une liste de tuples representant les coordonnées relatives au point passé en argument et
    # representant, en combinant la liste retounée et l'argument "point", une sous-grille de taille 3x3 tirée de la grille
    # passée en argument.
    #
    @staticmethod
    def getSousGrille(grille, point):
        tab = []
        nx = round((point[0]-point[0]%3)/3)
        ny = round((point[1]-point[1]%3)/3)

        for x in range(0,3):
            for y in range(0,3):
                tab.append(((nx*3)+x, (ny*3)+y))

        tab.remove(point)
        return tab

    # Fonction getSousLigne
    #
    # grille : la grille sur laquelle vérifier.
    # x : point sur lequel verifier
    #
    # Cette fonction retourne une liste d'asbscisses representant les coordonnées relatives au point passé en argument et
    # representant, en combinant la liste retounée et l'argument "point", une ligne de taille 3 tirée de la grille
    # passée en argument.
    #
    @staticmethod
    def getSousLigne(grille, x):
        tab = []
        nx = round((x-x%3)/3)

        for x in range(0,3):
            tab.append((nx*3)+x)

        return tab

    @staticmethod
    def containNb(grille, nb):
        for x in range(grille.largeur):
            for y in range(grille.hauteur):
                if nb == grille.getCaseByCoords(x,y).getNumber():
                    return (x, y)
        return None

    @staticmethod
    def containNbSousGrille(grille, tab, nb):
        for i in tab:
            print("TEST SG : " + str(tab) + " : " + str(i) + " : " + str(grille.getCaseByCoords(i[0], i[1]).getNumber()) + " : " + str(nb))
            if (nb == grille.getCaseByCoords(i[0], i[1]).getNumber()):
                return i
        return None

    @staticmethod
    def missingNumbersSousGrille(tab, point):
        ret = []
        for i in range(1,10):
            if not(GrillesDeJeu.containNbSousGrille(tab, i, point)):
                ret.append(i)
        return ret;

    @staticmethod
    def missingNumberLigne(grille, y):
        tab = [1,2,3,4,5,6,7,8,9]
        ret = []
        for x in range(grille.largeur):
            if grille.getCaseByCoords(x,y).getNumber() > 0:
                ret.append(grille.getCaseByCoords(x,y).getNumber())

        for i in ret:
            print("YOLO2 : " + str(tab) + " : " + str(i))
            try:
                tab.remove(i)
            except:
                print("ERROR : " + str(i) + " : " + str(tab))
        return tab

    # Fonction verifierNombreLigne
    #
    # grille : la grille sur laquelle vérifier.
    # point : tuple représentant les coordonnées du nombre a vérifier. ex (x, y)
    #
    # Cette méthode vérifie si un nombre placé sur la grille n'a pas de doublon sur la ligne.
    #
    @staticmethod
    def verifierNombreLigne(grille, point):
        for x in range(grille.largeur):
            if (x == point[0]):
                continue
            if (grille.getCaseByCoords(x, point[1]).getNumber() == grille.getCaseByCoords(point[0], point[1]).getNumber()):
                return False
        return True

    # Fonction verifierNombreSousGrille
    #
    # grille : la grille sur laquelle vérifier.
    # point : tuple représentant les coordonnées du nombre a vérifier. ex (x, y)
    #
    # Cette méthode vérifie si un nombre placé sur la grille n'a pas de doublon dans sa SousGrille.
    #
    @staticmethod
    def verifierNombreSousGrille(grille, point):
        tab = GrillesDeJeu.getSousGrille(grille, point)

        for pt in tab:
            if (grille.getCaseByCoords(pt[0], pt[1]).getNumber() == grille.getCaseByCoords(point[0], point[1]).getNumber()):
                return False

        return True


    # Fonction verifierNombre
    #
    # grille : la grille sur laquelle vérifier.
    # point : tuple représentant les coordonnées du nombre a vérifier. ex (x, y)
    #
    # Cette méthode vérifie si un nombre placé sur la grille est correctement placé et respecte les règles du sudoku.
    #
    @staticmethod
    def verifierNombre(grille, point):
        for x in range(grille.largeur):
            if (x == point[0]):
                continue
            if (grille.getCaseByCoords(x, point[1]).getNumber() == grille.getCaseByCoords(point[0], point[1]).getNumber()):
                return False

        for y in range(grille.hauteur):
            if (y == point[1]):
                continue
            if (grille.getCaseByCoords(point[0], y).getNumber() == grille.getCaseByCoords(point[0], point[1]).getNumber()):
                return False

        tab = grilleGenerator.getSousGrille(grille, point)

        for pt in tab:
            if (grille.getCaseByCoords(pt[0], pt[1]).getNumber() == grille.getCaseByCoords(point[0], point[1]).getNumber()):
                return False

        return True
