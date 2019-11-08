import pygame
import math

class Particule:
    "Classe de base de particule."

    def __init__(self, position, life, couleur=(255,255,255)):
        self.life = life
        if(couleur[0] <= 255 and couleur[1] <= 255 and couleur[2] <= 255):
            self.couleur = couleur
        else:
            self.couleur = (255,255,255)
        self.position = position

    def tick(self):
        pass

    def isDead(self, tps):
        return self.life < tps

    def getPos(self):
        return self.position

    def draw(self, pxarray):
        if self.position[0] > -1 and self.position[0] < len(pxarray) and self.position[1] > -1 and self.position[1] < len(pxarray[0]):
            pxarray[self.position[0], self.position[1]] = self.couleur

    def clone(self, position):
        return Particule(position, self.life, self.couleur)
