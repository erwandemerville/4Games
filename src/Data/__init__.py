import pygame
from pygame.locals import *

class Data:

        def __init__(self, frame):
            # Cette variable représente les différents états dans lequel le jeu peut se trouver.
            #
            # 0 - Menu principal
            # 1 - options
            # 2 - demande si on reprend la grille du Sudoku
            # 3 - choix du niveau de difficulté au Sudoku (peut être généralisé si tout les mini-jeux possèdent exactement 3 niveaux de difficulté)
            # 4 - En partie de Sudoku
            # 5 - Gain/Perte de la partie du Sudoku
            #
            self.etat = 0

            # Cette variable représente la partie au cas ou on en aurait besoin.
            self.partie = None;

            # Ces variables permettent d'activer et désactiver le son/musique
            self.sound_active = True;
            self.music_active = True;

        # Fonction setEtat(e)
        #
        # e : le nouvel état du jeu
        #
        def setEtat(self, e):
            self.etat = e

        # Fonction setSound(e)
        #
        # e : boolean pour activer ou non les sons
        #
        def setSound(self,e):
            self.sound_active = e

        # Fonction setSound(e)
        #
        # e : boolean pour activer ou non les sons
        #
        def setMusic(self,e):
            self.music_active = e


