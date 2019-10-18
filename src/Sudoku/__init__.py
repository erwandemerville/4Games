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

liste_pos_l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
lettre_to_chiffre = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}
liste_pos_c = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Partie:
    """Classe principal du module Sudoku, permet de lancer le jeu.

    Pour démarrer une partie de sudoku, simplement saisir 'Partie()'.

    Une partie pourra être sauvegardée pour être reprise plus tard.
    La grille sera alors sauvegardée dans un fichier grilleEnCours

    Attributs :
    niveau = 1 (facile), 2 (intermédiaire) ou 3 (difficile)
    grille_jeu (Attribut de type Grille contenant la grille de jeu)
    etat_partie (1 = Partie en cours, 0 = Partie terminée)
    """

    def __init__(self):
        """CONSTRUCTEUR : Fonction qui gère le déroulement général du jeu 'Sudoku'.
        Pour passer d'un affichage en lignes de commandes à un affichage graphique,
        remplacer 'cmd' dans les noms de fonctions par 'gui'"""

        liste_numeros_solution, liste_num = None, None
        continuer = False

        # Vérifie si une grille est en cours.
        if self.charger_grille():
            # Demande à l'utilisateur s'il souhaite reprendre la grille en cours
            reprendre = self.reprendre_grille_cmd()
            if reprendre:
                grille_recup = self.charger_grille()
                liste_num = grille_recup[0:81]
                self.liste_numeros_init = grille_recup[81:162]
                liste_numeros_solution = grille_recup[162:243]
                continuer = True

        if not continuer:
            # Afficher le menu de choix du niveau :
            self.niveau = self.choixniveau_cmd()
            L = self.choixgrille_cmd()
            self.liste_numeros_init = L[0]
            liste_numeros_solution = L[1]
            liste_num = self.liste_numeros_init

        # Chargement de la grille de jeu à partir de la liste des numéros
        self.grille_jeu = Grille(9, 9, 0, 0, 0, 0, Sudoku_Case, liste_num)
        self.grille_jeu_solution = Grille(9, 9, 0, 0, 0, 0, Sudoku_Case, liste_numeros_solution)

        # L'état de la partie passe à "En cours"
        self.etat_partie = 1

        # ARRET EXCEPTIONNEL DU PROGRAMME (car programme non terminé)
        # sys.exit()

        # Attente de l'action du joueur
        self.etat_partie = 1  # Booléen indiquant si la partie est en cours ou non
        while self.etat_partie:  # Tant que la partie est en cours
            # Affichage de la grille
            self.grille_jeu.draw_cmd()

            self.action_joueur_cmd()  # Attente d'une action de la part du joueur

            # On vérifie si la grille est complétée (si la fonction retourne True)
            if self.get_etatgrille():
                print("Félicitations ! Vous avez résolu la grille !")
                self.etat_partie = 0  # Partie passe de "en cours" à "terminée"

        self.afficher_messagefin_cmd()

    @staticmethod
    def choixniveau_cmd():
        """COMMAND-LINE : Invite l'utilisateur à choisir un mode de difficulté."""

        print("Bienvenue sur le jeu du Sudoku !\n"
              "Choisissez un niveau de difficulté (saisir 1, 2 ou 3) :\n"
              "1 - Mode facile\n"
              "2 - Mode intermédiaire\n"
              "3 - Mode difficile\n")
        nb_saisi = None

        ok = False
        while not ok:
            nb_saisi = input("Veuillez saisir votre choix : ")

            try:
                nb_saisi = int(nb_saisi)
                assert 0 < nb_saisi <= 3
            except ValueError:
                print("Vous devez saisir un nombre. Veuillez recommencer :\n")
            except AssertionError:
                print("Vous devez saisir un chiffre entre 1 et 3. Veuillez recommencer :\n")
            else:
                ok = True

        return nb_saisi

    @staticmethod
    def choixniveau_gui():
        """INTERFACE GRAPHIQUE : Affiche un menu proposant 3 niveaux de difficulté.
        L'utilisateur doit cliquer sur le niveau de son choix."""

    def choixgrille_cmd(self):
        """COMMAND-LINE: Récupère le nombre de grilles dans le fichier .txt approprié au niveau de difficulté.
        Invite l'utilisateur a saisir le numéro d'une grille."""

        nb_grilles = GrillesDeJeu.get_nb_grilles(self.niveau)
        nb_saisi = None

        print("Quelle grille souhaitez-vous jouer ?")
        for i in range(nb_grilles):
            print("Grille n° {}".format(i + 1))

        ok = False
        while not ok:
            nb_saisi = input("\nVeuillez saisir votre choix : ")

            try:
                nb_saisi = int(nb_saisi)
                assert 1 <= nb_saisi <= nb_grilles
            except ValueError:
                print("Vous devez saisir un nombre. Veuillez recommencer :\n")
            except AssertionError:
                print("Cette grille n'existe pas. Veuillez recommencer :\n")
            else:
                ok = True

        liste = [GrillesDeJeu.get_grille(self.niveau, nb_saisi - 1),
             GrillesDeJeu.get_grille_solution(self.niveau, nb_saisi - 1)]
        return liste

    def choixgrille_gui(self):
        """INTERFACE GRAPHIQUE : Récupère dans fichier .txt le nombre de grille.
        Affiche un choix de grilles.
        Invite l'utilisateur à cliquer sur le bouton correspondant à la grille souhaitée."""

    def charger_grille(self):

        try:
            with open('grilleEnCours', 'rb') as fichier:
                mon_depickler = pickle.Unpickler(fichier)
                grille_recup = mon_depickler.load()
                fichier.close()
        except FileNotFoundError:
            return 0
        else:
            if not grille_recup:
                return 0
            else:

                return grille_recup

    @staticmethod
    def effacer_sauvegarde():
        """Fonction sauvegardant la grille afin de pouvoir la reprendre plus tard."""
        liste_grilles = []

        try:
            with open('grilleEnCours', 'wb') as fichier:
                mon_pickler = pickle.Pickler(fichier)
                mon_pickler.dump(liste_grilles)
                fichier.close()
        except FileNotFoundError:
            return 0
        else:
            return 1

    def reprendre_grille_cmd(self):
        """COMMAND-LINE : Invite l'utilisateur à reprendre la grille en cours."""
        print("Une partie a été sauvegardée.\n"
              "Souhaitez-vous la reprendre ?\n"
              "1 - Oui\n"
              "2 - Non (et effacer la sauvegarder)\n"
              "3 - Non (et conserver la sauvegarde)")

        nb_saisi = None

        ok = False
        while not ok:
            nb_saisi = input("Veuillez saisir votre choix : ")
            try:
                nb_saisi = int(nb_saisi)
                assert 1 <= nb_saisi <= 3
            except ValueError:
                print("Vous devez saisir un nombre. Veuillez recommencer :\n")
            except AssertionError:
                print("Vous devez saisir un chiffre entre 1 et 3. Veuillez recommencer :\n")
            else:
                ok = True

        if nb_saisi == 1:
            return 1
        elif nb_saisi == 2:
            self.effacer_sauvegarde()
            return 0
        else:
            return 0

    @staticmethod
    def reprendre_grille_gui():
        """INTERFACE GRAPHIQUE : Invite l'utilisateur à reprendre la grille en cours."""

    def sauvegarder_grille(self):
        """Fonction sauvegardant la grille afin de pouvoir la reprendre plus tard."""
        liste_grilles = self.grille_jeu.getListeNumeros() + self.liste_numeros_init + self.grille_jeu_solution.getListeNumeros()

        try:
            with open('grilleEnCours', 'wb') as fichier:
                mon_pickler = pickle.Pickler(fichier)
                mon_pickler.dump(liste_grilles)
                fichier.close()
        except FileNotFoundError:
            return 0
        else:
            return 1

    def verifier_numero_init(self, position):
        """Fonction permettant de vérifier si le joueur ne tente pas de modifier un des numéros
        présents initialement sur la grille de jeu."""

        if self.liste_numeros_init[position] != 0:
            return 0
        else:
            return 1

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

    def saisie_chiffre_cmd(self):
        """COMMAND-LINE : Fonction permettant au joueur de saisir un chiffre à ajouter dans la grille de jeu."""

        global liste_pos_c, liste_pos_l, lettre_to_chiffre
        numero_case = None

        ok = False
        continuer = False
        while not ok:
            try:
                choixp = input("Veuillez choisir une position (ex : A8) : ")
                assert len(choixp) == 2 and choixp[0] in liste_pos_l and int(choixp[1]) in liste_pos_c
            except AssertionError:
                print("La position doit être comprise entre A1 et I9.")
            else:
                numero_case = lettre_to_chiffre[choixp[0]] * 9 + (int(choixp[1]) - 1)
                if self.verifier_numero_init(numero_case):  # Si ce n'est pas un chiffre présent de base dans la grille
                    ok = True
                    continuer = True
                else:
                    print("Vous ne pouvez pas modifier un numéro présent initialement dans la grille.\n")

        if continuer:
            ok2 = False
            while not ok2:
                chiffre_ajouter = input("Veuillez choisir un chiffre à ajouter à cette case : ")

                try:
                    chiffre_ajouter = int(chiffre_ajouter)
                    assert 1 <= chiffre_ajouter <= 9
                except ValueError:
                    print("Vous devez saisir un chiffre.\n")
                except AssertionError:
                    print("Le chiffre doit être compris entre 1 et 9.\n")
                else:
                    ok2 = True
                    if self.verifier_numero_cl(numero_case, chiffre_ajouter):
                        self.grille_jeu.case[numero_case].setNumber(int(chiffre_ajouter))
                        return 1
                    else:
                        print("Ce chiffre est déjà présent sur cette ligne ou cette colonne.")
                        return 0
        else:
            return 0

    def effacer_chiffre_cmd(self):
        """COMMAND-LINE : Fonction permettant au joueur de saisir un chiffre à ajouter dans la grille de jeu."""

        global liste_pos_c, liste_pos_l, lettre_to_chiffre

        ok = False

        while not ok:
            try:
                choixp = input("Veuillez choisir une position (ex : A8) : ")
                assert len(choixp) == 2 and choixp[0] in liste_pos_l and int(choixp[1]) in liste_pos_c
            except AssertionError:
                print("La position doit être comprise entre A1 et I9.")
            else:

                numero_case = lettre_to_chiffre[choixp[0]] * 9 + (int(choixp[1]) - 1)
                if self.verifier_numero_init(numero_case):  # Si le chiffre à effacer n'est pas présent initialement
                    self.grille_jeu.case[numero_case].setNumber(0)
                    ok = True
                    return 1
                else:
                    print("Vous ne pouvez pas effacer un numéro présent initialement sur la grille !\n")
                    return 0

    def action_joueur_cmd(self):
        """COMMAND-LINE : Menu affichée en haut de la partie.
        Propose les options suivantes :
        - Saisir un chiffre
        - Sauvegarder grille
        - Réinitialiser grille
        - Changer de grille"""

        ok = False
        ok2 = None
        nb_saisi = None
        nb_saisi2 = None

        while not ok:
            print("Veuillez choisir une option :\n"
                  "1 - Ajouter un chiffre\n"
                  "2 - Effacer un chiffre\n"
                  "3 - Afficher d'autres options")

            nb_saisi = input("Veuillez saisir votre choix : ")

            try:
                nb_saisi = int(nb_saisi)
                assert 1 <= nb_saisi <= 3
            except ValueError:
                print("Vous devez saisir un chiffre. Veuillez recommencer :\n")
            except AssertionError:
                print("Ce choix n'existe pas. Veuillez recommencer :\n")
            else:

                if nb_saisi == 3:

                    ok2 = False
                    while not ok2:
                        print("Voici les options disponibles :\n"
                              "1 - Sauvegarder la partie\n"
                              "2 - Réinitialiser la grille\n"
                              "3 - Changer de grille\n"
                              "4 - Quitter le jeu\n"
                              "5 - Retour\n")

                        nb_saisi2 = input("Veuillez saisir votre choix : ")

                        try:
                            nb_saisi2 = int(nb_saisi2)
                            assert 1 <= nb_saisi2 <= 5
                        except ValueError:
                            print("Vous devez saisir un chiffre. Veuillez recommencer.\n")
                        except AssertionError:
                            print("Ce choix n'existe pas. Veuillez recommencer.\n")
                        else:
                            if nb_saisi2 == 1:  # Sauvegarde de la grille
                                if self.sauvegarder_grille():
                                    print("La partie a bien été enregistrée !\n")
                                    self.grille_jeu.draw_cmd()
                                    ok2 = True
                                else:
                                    print("Le fichier de sauvegarde n'existe pas et n'a pas pu être créé.\n"
                                          "Essayez d'exécuter le jeu avec les droits administrateur.")
                            elif nb_saisi2 == 2:
                                self.grille_jeu = Grille(9, 9, 0, 0, 0, 0, Sudoku_Case, self.liste_numeros_init)
                                print("La grille a bien été réinitialisée !\n")
                                self.grille_jeu.draw_cmd()
                                ok2 = True
                            elif nb_saisi2 == 3:
                                self.liste_numeros_init = self.choixgrille_cmd()
                                self.grille_jeu = Grille(9, 9, 0, 0, 0, 0, Sudoku_Case, self.liste_numeros_init)
                                print("La grille a bien été chargée !\n")
                                self.grille_jeu.draw_cmd()
                                ok2 = True
                            elif nb_saisi2 == 4:
                                self.etat_partie = 0  # Partie passe de "en cours" à "terminée"
                                ok2 = True
                                ok = True
                            else:
                                ok2 = True
                elif nb_saisi == 2:
                    if self.effacer_chiffre_cmd():
                        print("Effacé !\n")

                    ok = True
                else:
                    if self.saisie_chiffre_cmd():
                        print("Ajouté !\n")

                    ok = True

    def get_etatgrille(self):

        ok = True
        i = 0
        while i in range(81):
            if self.grille_jeu.case[i].getNumber() == 0:
                ok = False
                i = 82
            else:
                i += 1

        if ok:
            return 1
        else:
            return 0

    @staticmethod
    def afficher_messagefin_cmd():
        print("Merci d'avoir joué au Sudoku !\n"
              "N'hésitez pas à relancer une nouvelle partie quand vous voulez !")

        input("Appuyez sur une touche pour quitter.")


"""
(Fonction de test d'affichage sur console)
def draw_cmd():
    print("    1 2 3   4 5 6   7 8 9  \n"
          "   ˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍˍ \n"
          "A | _ _ _ | 0 0 0 | 0 0 0 |\n"
          "B | _ _ _ | 0 0 0 | 0 0 0 |\n"
          "C | 0 0 0 | 0 0 0 | 0 0 0 |\n"
          "  | --------------------- |\n"
          "D | 0 0 0 | 0 0 0 | 0 0 0 |\n"
          "E | 0 0 0 | 0 0 0 | 0 0 0 |\n"
          "F | 0 0 0 | 0 0 0 | 0 0 0 |\n"
          "  | --------------------- |\n"
          "G | 0 0 0 | 0 0 0 | 0 0 0 |\n"
          "H | 0 0 0 | 0 0 0 | 0 0 0 |\n"
          "I | 0 0 0 | 0 0 0 | 0 0 0 |\n"
          "   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ \n")
"""



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
        # Vérifie si une grille est en cours.
        if self.charger_grille():
            data.etat = 2
        else:
            # Afficher le menu de choix du niveau :
            data.etat = 3

        da.Data.menus[data.etat].draw(frame)

    def creerGrille(self, niveau):
        self.time = 0
        self.diff = niveau
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
                if len(grille_recup) != 163:
                    return False
                self.grille_jeu = Grille(9, 9, 50, 65, 400, 405, Sudoku_Case)
                self.grille_jeu.fillByListNumeros(grille_recup[:81])
                self.liste_numeros_init = grille_recup[81:162]
                self.time = grille_recup[-1]
                self.wrongCase = []
                for i in range(81):
                    if not(grilleGenerator.verifierNombre(self.grille_jeu, (i%self.grille_jeu.largeur, math.floor(i/self.grille_jeu.largeur)))):
                        self.wrongCase.append(1)
                    else:
                        self.wrongCase.append(0)
                return True

    def sauvegarder_grille(self): #Corriger ça
        """Fonction sauvegardant la grille afin de pouvoir la reprendre plus tard."""
        liste_grilles = self.grille_jeu.getListeNumeros() + self.liste_numeros_init
        liste_grilles.append(self.time);

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
                k = (k+1)%10
                case = self.grille_jeu.getSelectedCase()
                if case[0] != None:
                    if case[0].estVide() and self.liste_numeros_init[case[1]] == 0:
                        case[0].setNumber(k)

                        for l in range(81):
                            if not(grilleGenerator.verifierNombre(self.grille_jeu, (l%self.grille_jeu.largeur, math.floor(l/self.grille_jeu.largeur)))):
                                self.wrongCase[l] = 1
                            else:
                                self.wrongCase[l] = 0
                    if self.partieFinie():
                        data.setEtat(5)
            return True

    def partieFinie(self):
        for i in range(len(self.grille_jeu.case)):
            case = self.grille_jeu.getCase(i)
            if case.getNumber() == 0 or self.verifier_numero_cl(i, case.getNumber()) == 0:
                return False
        return True

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

    def getStringTime(self):
        return time.strftime('%M:%S ', time.gmtime(self.time))

    def draw(self, frame, menu=None):
        frame.fill((0,0,0))
        self.grille_jeu.drawForSudoku(frame, (190,190,190), self.liste_numeros_init, self.wrongCase, (104,104,104), (92,92,92), (73,73,73))
        if menu != None:
            menu.draw(frame)
        pygame.display.flip()
