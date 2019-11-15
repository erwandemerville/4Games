#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

# Code écrit dans le cadre du projet Algorithmique et Developpement
# Écrit en septembre 2019 par Lucas Raulier

import pygame
from pygame.locals import *
import math

from Grille import Loto_Case
from Grille import Sudoku_Case
from Grille import Bataille_Navale_Case


class Grille:
    """Classe permettant de gérer la grille"""

    # Constructeur de la grille
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # largeur : nombre de case de large
    # hauteur : nombre de cases de haut
    # x1 : coordonnée horizontale du point le plus en haut a gauche de la grille
    # y1 : coordonnée verticale du point le plus en haut a gauche de la grille
    # x2 : coordonnée horizontale du point le plus en bas a droite de la grille
    # y2 : coordonnée verticlae du point le plus en bas a droite de la grille
    # module : module contenant une classe nommée "Case" qui sera instancié par la grille (largeur * hauteur) fois.
    #
    # Permet d'instancier une grille simple contenant (largeur * hauteur) case qui sera
    # contenue dans le rectangle formé par les points (x1, y1) et (x2, y2).
    #
    def __init__(self, largeur, hauteur, x1, y1, x2, y2, module):
        if module == Bataille_Navale_Case:
            self.showShips = True
        else:
            self.showShips = None
        self.largeur = largeur
        self.hauteur = hauteur
        self.x = x1
        self.x2 = x2
        self.y = y1
        self.y2 = y2
        self.case = []  # Création d'une liste de cases
        for i in range(0, self.largeur * self.hauteur):  # Initialisation des cases de la grille
            if module == Loto_Case:
                self.case.append(module.Case(i + 1))
            else:
                self.case.append(module.Case())

    def getListeNumeros(self):
        """Fonction récupérant le numéro de chaque case pour en constituer une liste.
        Retourne cette liste."""

        listenumeros = []
        for i in range(self.largeur * self.hauteur):
            listenumeros.append(self.case[i].getNumber())

        return listenumeros

    def fillByListNumeros(self, list):
        for i in range(len(list)):
            self.case[i].setNumber(list[i])

    # Fonction getCase
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # id : identifiant de la case pouvant être retrouvé via l'opération suivante :
    # y * Largeur_de_la_grille + x => x représentant une colonne de la grille et y représente un ligne.
    #
    # Fonction retournant une case via l'id passé en argument.
    # Cette fonction est adaptée pour un appel via une boucle for.
    #
    def getCase(self, id):
        if (id < self.largeur * self.hauteur):
            return self.case[id]
        else:
            return None

    # Fonction getCaseByCoords
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # x : colonne sur laquelle la case se trouve.
    # y : ligne sur laquelle la case se trouve.
    #
    # Fonction retournant une case via le point (x, y) passé en argument.
    # Cette fonction est adaptée pour un appel normale.
    #
    def getCaseByCoords(self, x, y):
        if y * self.largeur + x < self.largeur * self.hauteur:
            return self.case[y * self.largeur + x]
        else:
            return None

    # Fonction getCaseByClick
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # x : coordonée horizontale du clic.
    # y : coordonée verticale du clic.
    #
    # Fonction retournant une case via le point (x, y) passé en argument.
    # Cette fonction est adaptée pour un appel provoqué par un clic de souris.
    #
    def getCaseByClick(self, x, y):
        if x <= self.x or y <= self.y or x >= self.x2 or y >= self.y2:
            return None

        cx = int(math.floor((x - self.x) / ((abs(self.x2 - self.x) / self.largeur))))
        cy = int(math.floor((y - self.y) / ((abs(self.y2 - self.y) / self.hauteur))))

        return self.getCaseByCoords(cx, cy)

    # Fonction selectCase
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # x : coordonée horizontale du clic.
    # y : coordonée verticale du clic.
    #
    # Fonction marque comme sélectionnée la case pointée par le point (x, y) passé en argument
    # et marque comme non-sélectionnée toutes les cases non pointées par le point (x, y).
    # Cette fonction est adaptée pour un appel provoqué par un clic de souris.
    #
    def selectCase(self, x, y):
        case = self.getCaseByClick(x, y)
        if case != None:
            case.select()
            for i in range(0, self.largeur * self.hauteur):
                if self.getCase(i) is not case:
                    self.getCase(i).deselect()
        else:
            for i in range(0, self.largeur * self.hauteur):
                self.getCase(i).deselect()

    # Fonction hoverCase
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # x : coordonée horizontale du clic.
    # y : coordonée verticale du clic.
    #
    # Définition du terme "hovered" : une case est considérée comme "hovered" quad le pointeur de la souris
    # désigne cette case.
    #
    # Fonction marque comme hovered la case pointée par le point (x, y) passé en argument
    # et marque comme non-sélectionnée toutes les cases non pointées par le point (x, y).
    # Cette fonction est adaptée pour un appel provoqué par un clic de souris.
    #
    def hoverCase(self, x, y):
        case = self.getCaseByClick(x, y)
        if case is not None:
            case.hover()
            for i in range(0, self.largeur * self.hauteur):
                if self.getCase(i) is not case:
                    self.getCase(i).unhover()
        else:
            for i in range(0, self.largeur * self.hauteur):
                self.getCase(i).unhover()

    # Fonction estVide
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction retournant un booleen indiquant si cette grille est considérée comme vide
    #
    def estVide(self):
        for i in range(0, self.hauteur):
            for j in range(0, self.largeur):
                if not (self.getCase(j, i).estVide()):
                    return False
        return True

    def getSelectedCase(self):
        for i in range(len(self.case)):
            if self.case[i].isSelected():
                return (self.case[i], i)
        return (None, -1)

    # Fonction contient
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # X : objet a tester
    #
    # Fonction retournant un booleen indiquant si une case de la grille contient l'objet X.
    #
    def contient(self, X):
        for i in range(0, self.hauteur):
            for j in range(0, self.largeur):
                if self.getCase(j, i).contient(X):
                    return True
        return False

    def getBoundingBox(self):
        return (self.x, self.y, self.x2, self.y2)

        # Fonction showShip
        #
        # self : instance de la classe, ne doit pas être mis en argument.
        #
        # Marque que cette case doit afficher le bateau qu'elle contient (si elle en contient un)
        #

    def showShip(self):
        self.showShips = True;

        # Fonction unshowShip
        #
        # self : instance de la classe, ne doit pas être mis en argument.
        #
        # Marque que cette case ne doit pas afficher le bateau qu'elle contient (si elle en contient un)
        #

    def unshowShip(self):
        self.showShips = False;

        # Fonction isShowingSelected
        #
        # self : instance de la classe, ne doit pas être mis en argument.
        #
        # Retourne un booleen indiquant si cette case doit afficher le bateau qu'elle contient (si elle en contient un).
        #

    def isShowingSelected(self):
        return self.showShips;

    # Fonction draw
    #
    # ARGUMENTS OBLIGATOIRES :
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # surface : surface sur laquelle dessiner la grille, doit être la surface représentant la fenêtre entière.
    # couleur : tuple représentant la couleur avec laquelle les lignes de la grille doivent être déssinées.
    #
    # ARGUMENTS OPTIONELS :
    #
    # x : coordonnée horizontale du point le plus en haut a gauche de la zone ou dessiner la grille.
    # y : coordonnée verticale du point le plus en haut a gauche de la zone ou dessiner la grille.
    # x2 : coordonnée horizontale du point le plus en bas a droite de la zone ou dessiner la grille.
    # y2 : coordonnée verticale du point le plus en bas a droite de la zone ou dessiner la grille.
    #
    # Si une ou plusieurs des coordonnées ne sont pas précisées, les points de la grille seront
    # pris comme référence pour les points non précisés.
    # Les tailles de la grille et des cases sont déterminées en fontion des points utilisés.
    #
    # caseSelectColor : couleur appliquée sur une case marquée comme sélectionée.
    # caseHoverColor : couleur appliquée sur une case marquée comme hovered (Le pointeur de la souris se trouve sur la case).
    # caseSelectHoverColor : couleur appliquée sur une case marquée comme sélectionée et hovered.
    #
    # Si une ou plusieurs des couleurs ne sont pas précisées,
    # elles seront calculées en utilisant l'argument couleur comme base.
    #
    def draw(self, surface, couleur, caseSelectColor=None, caseHoverColor=None,
             caseSelectHoverColor=None):
        x = self.x
        x2 = self.x2
        y = self.y
        y2 = self.y2

        largeur = abs(x2 - x)
        hauteur = abs(y2 - y)
        case_Largeur = largeur / self.largeur
        case_Hauteur = hauteur / self.hauteur
        effectiveCase_Largeur = case_Largeur+1
        effectiveCase_Hauteur = case_Hauteur+1

        if caseSelectColor == None:
            caseSelectColor = (min(couleur[0]-27, 0),min(couleur[1]-27, 0),min(couleur[2]-27, 0))

        if caseSelectHoverColor == None:
            caseSelectHoverColor = (min(couleur[0]-33, 0),min(couleur[1]-33, 0),min(couleur[2]-33, 0))

        if caseHoverColor == None:
            caseHoverColor = (min(couleur[0]-45, 0),min(couleur[1]-45, 0),min(couleur[2]-45, 0))

        for i in range(0, self.hauteur):
            for j in range(0, self.largeur):
                self.getCaseByCoords(j, i).draw(surface, x + j * case_Largeur, y + i * case_Hauteur, effectiveCase_Largeur,
                                                effectiveCase_Hauteur, selectFill=caseSelectColor,
                                                hoverFill=caseHoverColor, bothFill=caseSelectHoverColor)

        pygame.draw.line(surface, couleur, (x, y), (x2, y))
        pygame.draw.line(surface, couleur, (x, y), (x, y2))
        pygame.draw.line(surface, couleur, (x2, y), (x2, y2))
        pygame.draw.line(surface, couleur, (x, y2), (x2, y2))
        for i in range(0, self.hauteur):
            ny = y + (case_Hauteur * i)
            pygame.draw.line(surface, couleur, (x, ny), (x + largeur, ny))

        for i in range(0, self.largeur):
            nx = x + (case_Largeur * i)
            pygame.draw.line(surface, couleur, (nx, y), (nx, y + hauteur))

    def drawForSudoku(self, surface, couleur, casesBase, casesErr, caseSelectColor=None, caseHoverColor=None,
             caseSelectHoverColor=None, errColor=(184, 3, 3), notBaseColor=(60, 139, 204)):
        x = self.x
        x2 = self.x2
        y = self.y
        y2 = self.y2

        largeur = abs(x2 - x)
        hauteur = abs(y2 - y)
        case_Largeur = largeur / self.largeur
        case_Hauteur = hauteur / self.hauteur
        effectiveCase_Largeur = case_Largeur+1
        effectiveCase_Hauteur = case_Hauteur+1

        if caseSelectColor == None:
            caseSelectColor = (min(couleur[0]-27, 0),min(couleur[1]-27, 0),min(couleur[2]-27, 0))

        if caseSelectHoverColor == None:
            caseSelectHoverColor = (min(couleur[0]-33, 0),min(couleur[1]-33, 0),min(couleur[2]-33, 0))

        if caseHoverColor == None:
            caseHoverColor = (min(couleur[0]-45, 0),min(couleur[1]-45, 0),min(couleur[2]-45, 0))

        for i in range(0, self.hauteur):
            for j in range(0, self.largeur):
                if casesErr[i*self.largeur+j] != 0 and casesBase[i*self.largeur+j] != 0:
                    self.getCaseByCoords(j, i).draw(surface, x + j * case_Largeur, y + i * case_Hauteur, effectiveCase_Largeur,
                                                    effectiveCase_Hauteur, selectFill=caseSelectColor,
                                                    hoverFill=caseHoverColor, bothFill=caseSelectHoverColor, textFill=(errColor[0]+50, errColor[1]+50, errColor[2]+50))
                elif casesErr[i*self.largeur+j] != 0:
                    self.getCaseByCoords(j, i).draw(surface, x + j * case_Largeur, y + i * case_Hauteur, effectiveCase_Largeur,
                                                    effectiveCase_Hauteur, selectFill=caseSelectColor,
                                                    hoverFill=caseHoverColor, bothFill=caseSelectHoverColor, textFill=errColor)
                elif casesBase[i*self.largeur+j] != 0:
                    self.getCaseByCoords(j, i).draw(surface, x + j * case_Largeur, y + i * case_Hauteur, effectiveCase_Largeur,
                                                    effectiveCase_Hauteur, selectFill=caseSelectColor,
                                                    hoverFill=caseHoverColor, bothFill=caseSelectHoverColor)
                else:
                    self.getCaseByCoords(j, i).draw(surface, x + j * case_Largeur, y + i * case_Hauteur, effectiveCase_Largeur,
                                                    effectiveCase_Hauteur, selectFill=caseSelectColor,
                                                    hoverFill=caseHoverColor, bothFill=caseSelectHoverColor, textFill=notBaseColor)

        pygame.draw.line(surface, couleur, (x, y), (x2, y))
        pygame.draw.line(surface, couleur, (x, y), (x, y2))
        pygame.draw.line(surface, couleur, (x2, y), (x2, y2))
        pygame.draw.line(surface, couleur, (x, y2), (x2, y2))
        for i in range(0, self.hauteur):
            ny = y + (case_Hauteur * i)
            pygame.draw.line(surface, couleur, (x, ny), (x + largeur, ny))

        for i in range(0, self.largeur):
            nx = x + (case_Largeur * i)
            pygame.draw.line(surface, couleur, (nx, y), (nx, y + hauteur))
        pygame.draw.line(surface,(255,255,255),(x+3*case_Largeur,y),(x+3*case_Largeur,y2),3)
        pygame.draw.line(surface,(255,255,255),(x+6*case_Largeur,y),(x+6*case_Largeur,y2),3)
        pygame.draw.line(surface,(255,255,255),(x,y+3*case_Hauteur),(x2,y+3*case_Hauteur),3)
        pygame.draw.line(surface,(255,255,255),(x,y+6*case_Hauteur),(x2,y+6*case_Hauteur),3)
