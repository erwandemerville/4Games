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

liste_pos_l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
lettre_to_chiffre = {'A': 0, 'B': '1', 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8}
liste_pos_c = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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

    def __init__(self):
        """CONSTRUCTEUR : Fonction qui gère le déroulement général du jeu 'Sudoku'.
        Pour passer d'un affichage en lignes de commandes à un affichage graphique,
        remplacer 'cmd' dans les noms de fonctions par 'gui'"""

        continuer = False

        # Vérifie si une grille est en cours.
        if self.charger_grille():
            # Demande à l'utilisateur s'il souhaite reprendre la grille en cours
            reprendre = self.reprendre_grille_cmd()
            if reprendre:
                liste_num = self.charger_grille()
                continuer = True

        if not continuer:
            # Afficher le menu de choix du niveau :
            self.niveau = self.choixniveau_cmd()
            self.liste_numeros_init = self.choixgrille_cmd()
            liste_num = self.liste_numeros_init

        # Chargement de la grille de jeu à partir de la liste des numéros
        self.grille_jeu = Grille(9, 9, 0, 0, 0, 0, Sudoku_Case, liste_num)

        # L'état de la partie passe à "En cours"
        self.etat_partie = 1

        # ARRET EXCEPTIONNEL DU PROGRAMME (car programme non terminé)
        #sys.exit()

        # Attente de l'action du joueur
        partie_terminee = False  # Booléen indiquant si la partie est terminée ou non
        while not partie_terminee:
            # Affichage de la grille
            self.grille_jeu.draw_cmd()

            self.action_joueur_cmd()  # Attente d'une action de la part du joueur

            """# On vérifie si la grille est complétée (si la fonction retourne True)
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

        self.afficher_messagefin()"""

    @staticmethod
    def choixniveau_cmd():
        """COMMAND-LINE : Invite l'utilisateur à choisir un mode de difficulté."""

        print("Bienvenue sur le jeu du Sudoku !\n"
              "Choisissez un niveau de difficulté (saisir 1, 2 ou 3) :\n"
              "1 - Mode facile\n"
              "2 - Mode intermédiaire\n"
              "3 - Mode hardcore\n")
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

                self.liste_numeros_init = grille_recup[81:162]
                return grille_recup

    @staticmethod
    def reprendre_grille_cmd():
        """COMMAND-LINE : Invite l'utilisateur à reprendre la grille en cours."""
        print("Une partie a été sauvegardée.\n"
              "Souhaitez-vous la reprendre ?\n"
              "1 - Oui"
              "2 - Non")

        nb_saisi = None

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

    def sauvegarder_grille(self):
        """Fonction sauvegardant la grille afin de pouvoir la reprendre plus tard."""
        liste_grilles = self.grille_jeu.getListeNumeros() + self.liste_numeros_init

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
        else :
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
                    self.grille_jeu.case[numero_case] = chiffre_ajouter
                    return 1
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
                    self.grille_jeu.case[numero_case] = 0
                    ok = True
                    return 1
                else:
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
                              "4 - Retour\n")

                        nb_saisi2 = input("Veuillez saisir votre choix : ")

                        try:
                            nb_saisi2 = int(nb_saisi2)
                            assert 1 <= nb_saisi2 <= 4
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
                            else:
                                ok2 = True
                elif nb_saisi == 2:
                    if self.effacer_chiffre_cmd():
                        print("Effacé !\n")
                        ok = True
                    else:
                        print("Vous ne pouvez pas effacer un numéro présent initialement sur la grille !\n")
                else:
                    if self.saisie_chiffre_cmd():
                        print("Ajouté !\n")
                        ok = True
                    else:
                        print("Vous ne pouvez pas modifier un numéro présent initialement sur la grille !\n")



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
