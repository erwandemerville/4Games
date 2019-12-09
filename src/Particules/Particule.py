import pygame
import math

class Particule:
    "Classe de base de particule."

    # Constructeur de la classe Particule
    #
    # ARGUMENTS OBLIGATOIRES :
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # position : position ou la particule se trouve
    # life : temps de vie de la particule, en itération de la boucle du main
    #
    # ARGUMENTS OPTIONNELS :
    #
    # couleur : couleur de la particule, blanc si non déclarée
    #
    def __init__(self, position, life, couleur=(255,255,255)):
        self.life = life
        if(couleur[0] <= 255 and couleur[1] <= 255 and couleur[2] <= 255):
            self.couleur = couleur
        else:
            self.couleur = (255,255,255)
        self.position = position

    # Fonction tick
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction executant des actions a chaque itération de la boucle du main
    #
    def tick(self):
        pass

    # Fonction isDead
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # tps : temps a tester
    #
    # Fonction determinant si la particule sera morte dans un temps "tps"
    #
    def isDead(self, tps):
        return self.life < tps

    # Fonction getPos
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction retournant la position actuelle de la particule
    #
    def getPos(self):
        return self.position

    # Fonction draw
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # pxarray : tableau de pixels de la fenêtre. Utilisé car plus rapide quand on utilise des pixels
    #
    # Fonction permettant de dessiner la particule
    #
    def draw(self, pxarray):
        if self.position[0] > -1 and self.position[0] < len(pxarray) and self.position[1] > -1 and self.position[1] < len(pxarray[0]):
            pxarray[self.position[0], self.position[1]] = self.couleur

    # Focntion clone
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # position : position de la nouvelle particule
    #
    # Focntion permettant de cloner une particule
    #
    def clone(self, position):
        return Particule(position, self.life, self.couleur)
