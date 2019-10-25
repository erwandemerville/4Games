import pygame
import math

class Particule:
    "Classe de base de particule."

    def __init__(self, position, life, couleur=(255,255,255), vitesse=1, direction=0, deathFrames=1, gravity=0):
        self.life = life
        self.couleur = couleur
        self.v = vitesse
        self.vitesse = (vitesse*math.cos(direction), vitesse*math.sin(direction))
        self.position = position
        self.alpha = 1.0
        self.alphaDiff = 1.0 / deathFrames
        self.gravity = gravity

    def tick(self):
        if self.life > 0:
            self.life = self.life-1
        else:
            self.alpha = self.alpha - self.alphaDiff

    def isDead(self):
        return self.alpha <= 0.0

    def getPos(self):
        return self.position

    def draw(self, frame):
        frame.fill(self.couleur, (self.position, (1,1)))

    def clone(self, position):
        return Particule(position, self.life, self.couleur, self.v, self.direction, 1.0 / self.alphaDiff)
