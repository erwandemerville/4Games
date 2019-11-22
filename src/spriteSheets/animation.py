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

    # Fonction setLoop
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # loop : argument indiquant si l'animation doit tourner sur elle même
    #
    # Fonction permettant de définir si l'animation peut tourner sur elle même.
    #
    def setLoop(self, loop):
        self.loop = loop


    # Fonction scale
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # nw : nouvelle largeur de l'animation
    # nh : nouvelle hauteur de l'animation
    #
    # Permet de changer la taille des frames de l'animation.
    #
    def scale(self, nw, nh):
        for i in self.frames:
            pygame.transform.scale(i, (nw, nh))

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
