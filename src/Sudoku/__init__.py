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

    def __init__(self, frame, data):
        """CONSTRUCTEUR : Fonction qui gère le déroulement général du jeu 'Sudoku'.
        Pour passer d'un affichage en lignes de commandes à un affichage graphique,
        remplacer 'cmd' dans les noms de fonctions par 'gui'"""

        #varaible du chronomètre
        self.time = 0
        self.diff = 1
        self.erreur = 0
        # Vérifie si une grille est en cours.
        if self.charger_grille():
            data.setEtat("Sudoku_Saved")
        else:
            # Afficher le menu de choix du niveau :
            data.setEtat("Sudoku_Diff")

        data.getCurrentMenu().draw(frame)

    def creerGrille(self, niveau):
        self.time = 0
        self.diff = niveau
        self.erreur = 0
        self.grille_jeu = Grille(9, 9, 50, 65, 400, 405, Sudoku_Case)
        self.liste_numeros_init = GrillesDeJeu.get_grille(niveau, self.grille_jeu).getListeNumeros()
        self.wrongCase = []
        for i in range(81):
            self.wrongCase.append(0)
        #self.liste_numeros_init = grilleGenerator.generer(self.grille_jeu, niveau)

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

    def effacer_sauvegarde(self):
        if(self.charger_grille()):
            os.remove('grilleEnCours')

    def verifier_numero_init(self, position):
        """Fonction permettant de vérifier si le joueur ne tente pas de modifier un des numéros
        présents initialement sur la grille de jeu."""

        if self.liste_numeros_init[position] != 0:
            return 0
        else :
            return 1

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
                            if not(grilleGenerator.verifierNombre(self.grille_jeu, (l%self.grille_jeu.largeur, math.floor(l/self.grille_jeu.largeur)))):
                                self.wrongCase[l] = 1
                            else:
                                self.wrongCase[l] = 0
            else:
                k = (k+1+(math.floor(k/9))) %10
                case = self.grille_jeu.getSelectedCase()
                if case[0] != None:
                    if case[0].estVide() and self.liste_numeros_init[case[1]] == 0:
                        case[0].setNumber(k)
                        if not(grilleGenerator.verifierNombre(self.grille_jeu, (case[1]%self.grille_jeu.largeur, math.floor(case[1]/self.grille_jeu.largeur)))):
                            self.erreur = self.erreur+1
                        for l in range(81):
                            if not(grilleGenerator.verifierNombre(self.grille_jeu, (l%self.grille_jeu.largeur, math.floor(l/self.grille_jeu.largeur)))):
                                self.wrongCase[l] = 1
                            else:
                                self.wrongCase[l] = 0
                    if self.partieFinie():
                        data.setEtat(5)
                        self.effacer_sauvegarde()
                        self.victoire(data);
                        da.Data.menus[5].draw(frame)
            return True

    def partieFinie(self):
        for i in range(len(self.grille_jeu.case)):
            case = self.grille_jeu.getCase(i)
            if case.getNumber() == 0 or self.verifier_numero_cl(i, case.getNumber()) == 0:
                return False
        return True

    def compareTimes(self, a, b, c, d):
        tA = time.strptime(a, "%M:%S")
        tB = time.strptime(b, "%M:%S")
        return tA.tm_min*60+tA.tm_sec+c*60>tB.tm_min*60+tB.tm_sec+d*60

    def victoire(self,data):
        data.classements[0].ajouterScore(("TEST", self.getStringTime(), self.erreur))
        #data.classements[0].sort(lambda a,b,c,d : print(str(a)+"_:_"+str(b)+"_:_"+str(c)+"_:_"+str(d)))
        data.classements[0].sort(self.compareTimes)
        data.classements[0].save("Classements_Sudoku.yolo")
        rayon = 4
        data.particules.addEmitter(FireWorkParticule.FireworkEmitter(data.particules, [Particule.Particule((100,100), 60, (230, 60, 60))], [(235, 0, 0), (0, 0, 0)], rayon, 60, (320, 480), (0, -4) , 0, 2))

    def verifier_numero_cl(self, position, number):
        """Cette fonction vérifie si le numéro entré n'est pas présent sur la même ligne ou colonne."""

        ok = True
        n = 0
        i = 0
        while i <= 80:
            i += 9
            if n <= position < i:
                for j in range(n, i):
                    if position != j:
                        if number == self.grille_jeu.case[j].getNumber():
                            ok = False
            n += 9

        if ok:
            u = position
            while not (0 <= u <= 8):
                u -= 9

            k = u
            while k in range(u, (u+9*8)+1):
                if position != k:
                    if number == self.grille_jeu.case[k].getNumber():
                        ok = False

                k += 9

        if not ok:
            return 0
        else:
            return 1

    def getDiff(self):
        return self.diff

    def getDiffStr(self):
        if self.diff == 1:
            return "Facile"
        elif self.diff == 2:
            return "Moyen"
        elif self.diff == 3:
            return "Difficile"
        else:
            return "Inconnu"

    def timerTick(self):
        self.time = self.time+1
        return 4

    def getStringTime(self):
        return time.strftime('%M:%S', time.gmtime(self.time))

    def getNbErreurs(self):
        return self.erreur

    def draw(self, frame, menu=None):
        frame.fill((0,0,0))
        self.grille_jeu.drawForSudoku(frame, (190,190,190), self.liste_numeros_init, self.wrongCase, (104,104,104), (92,92,92), (73,73,73))
        if menu != None:
            menu.draw(frame)
        pygame.display.flip()
