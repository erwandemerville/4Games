import pygame
import pickle
import os, math, time
from Grille import Grille
from Grille import Bataille_Navale_Case


class GameBN:

    bateauStr = {"Porte-Avion" : ["A", "B", "C", "D", "E"],
                 "Croiseur": ["", "", "", ""],
                 "Contre-Torpilleur": ["", "", ""],
                 "Sous-marin": ["", "", ""],
                 "Torpilleur": ["", ""]}

    def __init__(self, data):
        #self.grille_J1 = Grille.Grille(10, 10, 210, 245, 430, 465, Bataille_Navale_Case)
        #self.grille_J2 = Grille.Grille(10, 10, 210, 15, 430, 235, Bataille_Navale_Case)
        self.data = data
        self.grille_J1 = Grille.Grille(10, 10, 145, 100, 495, 450, Bataille_Navale_Case)
        self.grille_J2 = Grille.Grille(10, 10, 145, -450, 495, -100, Bataille_Navale_Case)

    def ajouter_Bateau(self, grille, direction, position, type):

        l = len(GameBN.bateauStr[type])
        if direction == 'Horizontale':
            if position[0] > self.grille_J1.largeur-l+1 or position[0] < 0:
                print("Position invalide")
            else:
                for x in range(l):
                    grille.getCaseByCoords(position[0]+x-1, position[1]-1).setContenu(GameBN.bateauStr[type][x])
        elif direction == 'Verticale':
            if position[1] > self.grille_J1.hauteur-l+1 or position[1] < 0:
                print("Position invalide")
            else:
                for x in range(l):
                    grille.getCaseByCoords(position[0]-1, position[1]+x-1).setContenu(GameBN.bateauStr[type][x])
        else:
            print("Direction invalide")

        pass

    def cmd(self):
        direction = input("Veuillez entrer la direction du porte-avion : ")
        caseX = int(input("Veuillez selectionner la case(X) sur laquelle placer le porte-avion : "))
        caseY = int(input("Veuillez selectionner la case(Y) sur laquelle placer le porte-avion : "))
        self.ajouter_Bateau(self.grille_J1, direction, (caseX, caseY), "Porte-Avion")

    def draw(self, frame, menu=None):
        frame.fill((1, 80, 172))
        if self.data.etat == 12:
            pygame.draw.line(frame, (250, 250, 250), (160, 240), (480, 240))
        self.grille_J1.draw(frame, (250, 250, 250), (95, 95, 244), (85, 85, 234), (90, 90, 239))
        self.grille_J2.draw(frame, (250, 250, 250), (95, 95, 244), (85, 85, 234), (90, 90, 239))
        if menu != None:
            menu.draw(frame)
        pass
