import pygame
from pygame.locals import *
import pickle
import os, math, time
from Grille import Grille
from Grille import Bataille_Navale_Case


class GameBN:

    def __init__(self, data):
        self.data = data
        self.grille_J1 = Grille.Grille(10, 10, 145, 100, 495, 450, Bataille_Navale_Case)
        self.grille_J2 = Grille.Grille(10, 10, 145, -450, 495, -100, Bataille_Navale_Case)
        self.bateauStr = {"Porte-Avion": [pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/Porte-avions_1.png")).convert(),
                                          pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/Porte-avions_2.png")).convert(),
                                          pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/Porte-avions_3.png")).convert(),
                                          pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/Porte-avions_4.png")).convert(),
                                          pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/Porte-avions_5.png")).convert()],
                     "Croiseur": ["C1", "C2", "C3", "C4"],
                     "Contre-Torpilleur": ["CT1", "CT2", "CT3"],
                     "Sous-marin": ["SM1", "SM2", "SM3"],
                     "Torpilleur": ["T1", "T2"]}
        self.placeData = [(30, 240), (0, 0), (0, 0), (0, 0), (0, 0), 1]

    def ajouter_Bateau(self, grille, direction, position, type):

        l = len(self.bateauStr[type])
        if direction == 'Horizontale':
            if position[0] > self.grille_J1.largeur-l+1 or position[0] < 1:
                print("Position invalide")
            else:
                for x in range(l):
                    grille.getCaseByCoords(position[0]+x-1, position[1]-1).setContenu(self.bateauStr[type][x])
        elif direction == 'Verticale':
            if position[1] > self.grille_J1.hauteur-l+1 or position[1] < 1:
                print("Position invalide")
            else:
                for x in range(l):
                    grille.getCaseByCoords(position[0]-1, position[1]+x-1).setContenu(self.bateauStr[type][x])
        else:
            print("Direction invalide")

        pass

    def tir(self, grille, position):
        if position[0] > 10 or position[0] < 1 or position[1] > 10 or position[1] < 1:
            print("Position invalide")
        else:
            grille.getCaseByCoords(position[0]-1, position[1]-1).shoot()

    def checkVictory(self, grille):
        i = 0
        for y in range(grille.hauteur):
            for x in range(grille.largeur):
                if not grille.getCaseByCoords(x, y).estVide() and grille.getCaseByCoords(x, y).isShot():
                    i = i+1
        return i == 17

    def cmd(self):
        self.ajouter_Bateau(self.grille_J1, "Horizontale", (1, 1), "Porte-Avion")
        self.ajouter_Bateau(self.grille_J1, "Horizontale", (1, 2), "Croiseur")
        self.ajouter_Bateau(self.grille_J1, "Horizontale", (1, 3), "Contre-Torpilleur")
        self.ajouter_Bateau(self.grille_J1, "Horizontale", (1, 4), "Sous-marin")
        self.ajouter_Bateau(self.grille_J1, "Horizontale", (1, 5), "Torpilleur")

        self.tir(self.grille_J1, (1, 1))
        self.tir(self.grille_J1, (2, 1))
        self.tir(self.grille_J1, (3, 1))
        self.tir(self.grille_J1, (4, 1))
        self.tir(self.grille_J1, (5, 1))

        self.tir(self.grille_J1, (1, 2))
        self.tir(self.grille_J1, (2, 2))
        self.tir(self.grille_J1, (3, 2))
        self.tir(self.grille_J1, (4, 2))

        self.tir(self.grille_J1, (1, 3))
        self.tir(self.grille_J1, (2, 3))
        self.tir(self.grille_J1, (3, 3))

        self.tir(self.grille_J1, (1, 4))
        self.tir(self.grille_J1, (2, 4))
        self.tir(self.grille_J1, (3, 4))

        self.tir(self.grille_J1, (1, 5))
        self.tir(self.grille_J1, (2, 5))



        """direction = input("Veuillez entrer la direction du porte-avion : ")
        caseX = int(input("Veuillez selectionner la case(X) sur laquelle placer le porte-avion : "))
        caseY = int(input("Veuillez selectionner la case(Y) sur laquelle placer le porte-avion : "))
        self.ajouter_Bateau(self.grille_J1, direction, (caseX, caseY), "Porte-Avion")"""

    def draw(self, frame, menu=None):
        frame.fill((1, 80, 172))
        if self.data.etat == 12:
            pygame.draw.line(frame, (250, 250, 250), (160, 240), (480, 240))
        elif self.data.etat == 11:
            if self.placeData[5] == 1:
                self.grille_J1.draw(frame, (250, 250, 250), (95, 95, 244), (85, 85, 234), (90, 90, 239))
            else:
                self.grille_J2.draw(frame, (250, 250, 250), (95, 95, 244), (85, 85, 234), (90, 90, 239))
            for i in range(len(self.placeData)):
                if self.placeData[i][0] != 0 or self.placeData[i][1] != 0:
                pass # Finir Lucas
        if menu != None:
            menu.draw(frame)
        pass
