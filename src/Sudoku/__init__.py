#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

"""Fichier d'initialisation du module Sudoku.
Ce fichier contient la classe Partie qui initialise une partie de Sudoku.
La classe est adaptée à la fois pour une utilisation sur interface en lignes de commandes,
et pour une utilisation sur interface graphique.
"""

import pygame
import UiPygame as ui
import pickle
import sys
import os, math
from Grille.Grille import Grille
from Grille import Sudoku_Case
from Sudoku.grillesDeJeu import *
import Data as da
import time
from Particules import FireWorkParticule, Particule

class PartieG:
    """Classe principal du module Sudoku, permet de lancer le jeu.
    Pour démarrer une partie de sudoku, simplement saisir 'PartieG()'.
    Une partie pourra être sauvegardée pour être reprise plus tard.
    La grille sera alors sauvegardée dans un fichier grilleEnCours
    Cette classe sera utilisée pour les applications graphiques
    Attributs :
    niveau = 1 (facile), 2 (intermédiaire) ou 3 (hardcore)
    grille_jeu (Attribut de type Grille contenant la grille de jeu)
    etat_partie (1 = Partie en cours, 2 = Partie gagnée, 3 = Partie pedue)
    """

    # Constructeur de la classe PartieG
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # frame : instance de la fenetre
    # data : instance de la classe data
    #
    # Permet d'instancier et d'initialiser une partie de sudoku avec affichage graphique
    #
    def __init__(self, frame, data):
        """CONSTRUCTEUR : Fonction qui gère le déroulement général du jeu 'Sudoku'.
        Pour passer d'un affichage en lignes de commandes à un affichage graphique,
        remplacer 'cmd' dans les noms de fonctions par 'gui'"""

        self.time = 0 #variable du chronomètre
        self.diff = 1 #variable de diffculté
        self.erreur = 0 #variable du nombre d'erreurs
        # Vérifie si une grille est en cours.
        if self.charger_grille():
            data.setEtat("Sudoku_Saved")
        else:
            # Affiche le menu de choix du niveau :
            data.setEtat("Sudoku_Diff")

        data.getCurrentMenu().draw(frame)

    # Fonction creerGrille
    #
    # self : instance de la partie, ne pas mettre en argument
    # niveau : niveau de difficulté de la grille, allant de 1 (inclus) à 3 (inclus)
    #
    # Fonction servant a créer la grille et a l'ajouter dans la partie.
    # Cette fonction initialise aussi toutes les cases de la grille comme étant correctes.
    #
    def creerGrille(self, niveau):
        self.time = 0 # Défini le chromètre sur 0
        self.diff = niveau
        self.erreur = 0 # Défini le nombre d'erreur sur 0
        self.grille_jeu = Grille(9, 9, 50, 65, 400, 405, Sudoku_Case)
        self.liste_numeros_init = GrillesDeJeu.get_grille(niveau, self.grille_jeu).getListeNumeros()
        self.wrongCase = []
        for i in range(81):
            self.wrongCase.append(0)
        #self.liste_numeros_init = grilleGenerator.generer(self.grille_jeu, niveau)

    # Fonction charger_grille
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Cette fonction charge une partie de sudoku depuis le fichier grilleEnCours
    #
    def charger_grille(self):
        try:
            with open('grilleEnCours', 'rb') as fichier:
                mon_depickler = pickle.Unpickler(fichier)
                grille_recup = mon_depickler.load()
                fichier.close()
        except FileNotFoundError:
            return False
        else:
            if not grille_recup:
                return False
            else:
                if len(grille_recup) != 165:
                    return False
                self.grille_jeu = Grille(9, 9, 50, 65, 400, 405, Sudoku_Case)
                self.grille_jeu.fillByListNumeros(grille_recup[:81])
                self.liste_numeros_init = grille_recup[81:162]
                self.time = grille_recup[-3]
                self.diff = grille_recup[-2]
                self.erreur = grille_recup[-1]
                self.wrongCase = []
                for i in range(81):
                    if not(grilleGenerator.verifierNombre(self.grille_jeu, (i%self.grille_jeu.largeur, math.floor(i/self.grille_jeu.largeur)))):
                        self.wrongCase.append(1)
                    else:
                        self.wrongCase.append(0)
                return True

    # Fonction sauvegarder_grille
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Cette fonction sauvegarde une partie de sudoku dans le fichier grilleEnCours
    #
    def sauvegarder_grille(self):
        """Fonction sauvegardant la grille afin de pouvoir la reprendre plus tard."""
        liste_grilles = self.grille_jeu.getListeNumeros() + self.liste_numeros_init
        liste_grilles.append(self.time)
        liste_grilles.append(self.diff)
        liste_grilles.append(self.erreur)

        try:
            with open('grilleEnCours', 'wb') as fichier:
                mon_pickler = pickle.Pickler(fichier)
                mon_pickler.dump(liste_grilles)
                fichier.close()
        except FileNotFoundError:
            return 0
        else:
            return 1

    # Fonction effacer_sauvegarde
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Cette fonction efface le fichier grilleEnCours, ce qui a pour effet d'effacer la sauvegarde actuelle du sudoku.
    #
    def effacer_sauvegarde(self):
        if(self.charger_grille()):
            os.remove('grilleEnCours')

    # Function verifier_numero_init
    #
    # self : instance de la partie, ne pas mettre en argument
    # position : position ou on doit vérifier
    #
    # Cette Fonction verifie si le nombre dans la grille a la position "position" est un nombre
    # se trouvant dans la grille depuis le début de la partie.
    #
    def verifier_numero_init(self, position):
        """Fonction permettant de vérifier si le joueur ne tente pas de modifier un des numéros
        présents initialement sur la grille de jeu."""

        if self.liste_numeros_init[position] != 0:
            return 0
        else :
            return 1

    # Fonction keyPressed
    #
    # self : instance de la partie, ne pas mettre en argument
    # key : tableau contenant les touches du clavier
    # data : instance de la classe Data
    #
    # Cette fonction determine quoi faire en fonction des valeurs de tab
    #
    def keyPressed(self, key, data):
        k = -1
        for i in range(len(key)-1):
            if key[i] == 1:
                k = i
                break

        if k == -1:
            return False
        else:
            if k == 18:
                case = self.grille_jeu.getSelectedCase()
                if case[0] != None:
                    if self.liste_numeros_init[case[1]] == 0:
                        case[0].setNumber(0)
                        for l in range(81):
                            if not(PartieG.verifierNombre(self.grille_jeu, (l%self.grille_jeu.largeur, math.floor(l/self.grille_jeu.largeur)))):
                                self.wrongCase[l] = 1
                            else:
                                self.wrongCase[l] = 0
            else:
                k = (k+1+(math.floor(k/9))) %10
                case = self.grille_jeu.getSelectedCase()
                if case[0] != None:
                    if case[0].estVide() and self.liste_numeros_init[case[1]] == 0:
                        case[0].setNumber(k)
                        if not(PartieG.verifierNombre(self.grille_jeu, (case[1]%self.grille_jeu.largeur, math.floor(case[1]/self.grille_jeu.largeur)))):
                            self.erreur = self.erreur+1
                        for l in range(81):
                            if not(PartieG.verifierNombre(self.grille_jeu, (l%self.grille_jeu.largeur, math.floor(l/self.grille_jeu.largeur)))):
                                self.wrongCase[l] = 1
                            else:
                                self.wrongCase[l] = 0
                    if self.partieFinie():
                        data.setEtat(5)
                        self.effacer_sauvegarde()
                        self.victoire(data);
                        da.Data.menus[5].draw(frame)
            return True

    # Fonction partieFinie
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction qui renvoie True si la partie est gagné, sinon renvoie False.
    #
    def partieFinie(self):
        for i in range(len(self.grille_jeu.case)):
            case = self.grille_jeu.getCase(i)
            if case.getNumber() == 0 or GrillesDeJeu.verifierNombre(i, case.getNumber()) == 0:
                return False
        return True

    # Fonction compareTimes
    #
    # self : instance de la partie, ne pas mettre en argument
    # tab : tableau contenant les scores sous la forme : [temps1, temps2, erreurs1, erreurs2]
    #
    # Fonction comparant 2 scores et retourne True si le premier score est le meilleur, sinon retourne False
    #
    def compareTimes(self, tab):
        tA = time.strptime(tab[0], "%M:%S")
        tB = time.strptime(tab[1], "%M:%S")
        return tA.tm_min*60+tA.tm_sec+tab[2]*60>tB.tm_min*60+tB.tm_sec+tab[3]*60

    # Fonction victoire
    #
    # self : instance de la partie, ne pas mettre en argument
    # data : instance de la classe Data
    #
    # Fonction appellée en cas de victoire qui ajouter le score au classement et active les
    # feux d'artifices de victoire
    #
    def victoire(self,data):
        data.classements[0].ajouterScore(("TEST", self.getStringTime(), self.erreur))
        data.classements[0].sort(self.compareTimes)
        data.classements[0].save("Classements_Sudoku.yolo")
        rayon = 4
        data.particules.addEmitter(FireWorkParticule.FireworkEmitter(data.particules, [Particule.Particule((100,100), 60, (230, 60, 60))], [(235, 0, 0), (0, 0, 0)], rayon, 60, (320, 480), (0, -4) , 0, 2))

    # Fonction getDiff
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction retournant la difficulté de la partie sous forme de nombre
    #
    def getDiff(self):
        return self.diff

    # Fonction getDiffStr
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction retournant la difficulté de la partie sous forme de string
    #
    def getDiffStr(self):
        if self.diff == 1:
            return "Facile"
        elif self.diff == 2:
            return "Moyen"
        elif self.diff == 3:
            return "Difficile"
        else:
            return "Inconnu"

    # Fonction timerTick
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction appellée toute les secondes pour performer des actions
    #
    def timerTick(self):
        self.time = self.time+1
        return 4

    # Fonction getStringTime
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction retournant la durée de la partie sous forme de string
    #
    def getStringTime(self):
        return time.strftime('%M:%S', time.gmtime(self.time))

    # Fonction getDiff
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction retournant le nombre d'erreurs de la partie sous forme de nombre
    #
    def getNbErreurs(self):
        return self.erreur

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

        tab = PartieG.getSousGrille(grille, point)

        for pt in tab:
            if (grille.getCaseByCoords(pt[0], pt[1]).getNumber() == grille.getCaseByCoords(point[0], point[1]).getNumber()):
                return False

        return True

    # Fonction draw
    #
    # ARGUMENTS OBLIGATOIRES :
    #
    # self : instance de la partie, ne pas mettre en argument
    # frame : instance de la fenetre
    #
    # ARGUMENTS OPTIONELS :
    #
    # menu : menu a dessiner par dessus la partie
    #
    # Fonction servant a dessiner la partie
    #
    def draw(self, frame, menu=None):
        frame.fill((0,0,0))
        self.grille_jeu.drawForSudoku(frame, (190,190,190), self.liste_numeros_init, self.wrongCase, (104,104,104), (92,92,92), (73,73,73))
        if menu != None:
            menu.draw(frame)
        pygame.display.flip()
