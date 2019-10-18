import pygame

class Animation:

    # Constructeur de l'Animation
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # frames : les images de l'animation
    # loop : boolean indiquant si l'animation loop
    #
    # Instancie une Case.
    #
    def __init__(self, frames=[], loop=False):
        self.frames = frames
        self.loop = loop
        self.currentFrame = 0
        self.done = False

    # Fonction draw
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # surface : surface sur laquelle dessiner le rectangle
    # rect : partie de la surface sur laquelle dessiner le rectangle.(l'animation sera dessinée sur toute la surface si non précisé)
    #
    # Dessine l'image actuelle sur la surface passées en argument puis passe a l'image suivante.
    #
    def draw(self, surface, rect=None):
        surface.blit(self.frames[self.currentFrame], rect)
        self.currentFrame = self.currentFrame+1
        if self.currentFrame >= len(self.frames):
            if self.loop:
                self.currentFrame = 0
            else:
                self.done = True
