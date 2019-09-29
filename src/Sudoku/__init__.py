#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

"""Fichier d'initialisation du module Sudoku.

Ce fichier contient la classe Partie qui initialise une partie de Sudoku.
La classe est adaptée à la fois pour une utilisation sur interface en lignes de commandes,
et pour une utilisation sur interface graphique.
"""

import pickle
import sys
from Grille.Grille import Grille
from Grille import Sudoku_Case
from Sudoku.grillesDeJeu import *


class Partie:
    """Classe principal du module Sudoku, permet de lancer le jeu.

    Pour démarrer une partie de sudoku, simplement saisir 'Partie()'.

    Une partie pourra être sauvegardée pour être reprise plus tard.
    La grille sera alors sauvegardée dans un fichier grilleEnCours

    Attributs :
    niveau = 1 (facile), 2 (intermédiaire) ou 3 (hardcore)
    grille_jeu (Attribut de type Grille contenant la grille de jeu)
    etat_partie (1 = Partie en cours, 2 = Partie gagnée, 3 = Partie pedue)
    """

    def __init__(self, liste_numeros=None):
        """CONSTRUCTEUR : Fonction qui gère le déroulement général du jeu 'Sudoku'.
        Pour passer d'un affichage en lignes de commandes à un affichage graphique,
        remplacer 'cmd' dans les noms de fonctions par 'gui'"""

        continuer = False

        # Vérifie si une grille est en cours.
        if self.grille_en_cours():
            # Demande à l'utilisateur s'il souhaite reprendre la grille en cours
            reprendre = self.reprendre_grille_cmd()
            if reprendre:
                liste_numeros = self.grille_en_cours()
                continuer = True

        if not continuer:
            # Afficher le menu de choix du niveau :
            self.niveau = self.choixniveau_cmd()
            liste_numeros = self.choixgrille_cmd()

        # Chargement de la grille de jeu à partir de la liste des numéros
        self.grille_jeu = Grille(9, 9, 0, 0, 0, 0, Sudoku_Case, liste_numeros)

        # L'état de la partie passe à "En cours"
        self.etat_partie = 1

        # Affichage de la grille
        self.grille_jeu.draw_cmd()

        # ARRET EXCEPTIONNEL DU PROGRAMME (car programme non terminé)
        sys.exit()

        # Attente de l'action du joueur
        partie_terminee = False  # Booléen indiquant si la partie est terminée ou non
        while not partie_terminee:
            self.action_joueur_cmd()  # Attente d'une action de la part du joueur

            # On vérifie si la grille est complétée (si la fonction retourne True)
            if self.get_etatgrille():
                # On vérifie si la grille est correcte
                if self.verifier_grille():
                    self.etat_partie = 2  # Partie gagnée
                else:
                    self.etat_partie = 3  # Partie perdue

            if self.etat_partie == 2:  # Si partie gagnée
                partie_terminee = True
            if self.etat_partie == 3:  # Si partie perdue
                if self.choix_perdu() == 1:  # Si le joueur choisit d'arrêter la partie
                    partie_terminee = True
                if self.choix_perdu() == 2:  # Si le joueur choisit d'arrêter et afficher la solution
                    partie_terminee = True
                    self.afficher_solution()

        self.afficher_messagefin()

    @staticmethod
    def choixniveau_cmd(nb_saisi=None):
        """COMMAND-LINE : Invite l'utilisateur à choisir un mode de difficulté."""

        print("Bienvenue sur le jeu du Sudoku !\n"
              "Choisissez un niveau de difficulté (saisir 1, 2 ou 3) :\n"
              "1 - Mode facile\n"
              "2 - Mode intermédiaire\n"
              "3 - Mode hardcore\n")

        ok = False
        while not ok:
            nb_saisi = input("Veuillez saisir votre choix : ")

            try:
                nb_saisi = int(nb_saisi)
                assert nb_saisi > 0 and nb_saisi <= 3
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

    def choixgrille_cmd(self, nb_saisi=None):
        """COMMAND-LINE: Récupère le nombre de grilles dans le fichier .txt approprié au niveau de difficulté.
        Invite l'utilisateur a saisir le numéro d'une grille."""

        nb_grilles = GrillesDeJeu.get_nb_grilles(self.niveau)

        print("Quelle grille souhaitez-vous jouer ?\n")
        for i in range(nb_grilles):
            print("Grille n° {}".format(i + 1))

        ok = False
        while not ok:
            nb_saisi = input("Veuillez saisir votre choix : ")

            try:
                nb_saisi = int(nb_saisi)
                assert 1 <= nb_saisi <= nb_grilles
            except ValueError:
                print("Vous devez saisir un nombre. Veuillez recommencer :\n")
            except AssertionError:
                print("Cette grille n'existe pas. Veuillez recommencer :\n")
            else:
                ok = True

        return GrillesDeJeu.get_grille(self.niveau, nb_saisi - 1)

    def choixgrille_gui(self):
        """INTERFACE GRAPHIQUE : Récupère dans fichier .txt le nombre de grille.
        Affiche un choix de grilles.
        Invite l'utilisateur à cliquer sur le bouton correspondant à la grille souhaitée."""

    @staticmethod
    def grille_en_cours():

        try:
            with open('grilleEnCours', 'rb') as fichier:
                mon_depickler = pickle.Unpickler(fichier)
                grille_en_cours = mon_depickler.load()
                fichier.close()
        except FileNotFoundError:
            return 0
        else:
            if not grille_en_cours:
                return 0
            else:
                return grille_en_cours

    @staticmethod
    def reprendre_grille_cmd(nb_saisi=None):
        """COMMAND-LINE : Invite l'utilisateur à reprendre la grille en cours."""
        print("Une partie a été sauvegardée.\n"
              "Souhaitez-vous la reprendre ?\n"
              "1 - Oui"
              "2 - Non")

        ok = False
        while not ok:
            nb_saisi = input("Veuillez saisir votre choix : ")
            try:
                nb_saisi = int(nb_saisi)
                assert nb_saisi == 1 or nb_saisi == 2
            except ValueError:
                print("Vous devez saisir un nombre. Veuillez recommencer :\n")
            except AssertionError:
                print("Vous devez saisir un chiffre entre 1 et 2. Veuillez recommencer :\n")
            else:
                ok = True

        if nb_saisi == 1:
            return 1
        else:
            return 0

    @staticmethod
    def reprendre_grille_gui():
        """INTERFACE GRAPHIQUE : Invite l'utilisateur à reprendre la grille en cours."""

    @staticmethod
    def menuingame_cmd():
        """COMMAND-LINE : Menu affichée en haut de la partie.
        Propose les options suivants :
        - Réinitialiser grille
        - Sauvegarder grille"""


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
