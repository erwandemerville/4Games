import pygame

class ParticleSystem:
    "Classe du Système de Particules"

    # Constructeur de la classe ParticleSystem
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    #
    #
    def __init__(self):
        self.emitters = []
        self.particules = []
        self.mustDrawV = False
        self.time = 0

    # Fonction tick
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction executant des actions a chaque itération de la boucle du main
    #
    def tick(self):
        self.mustDrawV = len(self.particules) > 0
        self.time = self.time + 1
        for i in self.particules:
            if i.isDead(self.time):
                self.particules.remove(i)
            else:
                i.tick()
        for i in self.emitters:
            if i.isDead():
                self.emitters.remove(i)
            else:
                i.tick()

    # Fonnction draw
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # frame : instance de la fenêtre
    #
    # Fonction permettant de dessiner le système de particules
    #
    def draw(self, frame):
        if self.mustDraw:
            pArray = pygame.PixelArray(frame)
            for i in self.particules:
                i.draw(pArray)

    # Fonction addParticule
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # particle : particule a ajouter au système
    #
    # Fonction permettant d'ajouter une particule au système de particules
    #
    def addParticule(self, particle):
        particle.life = self.time + particle.life
        self.particules.append(particle)

    # Fonction addEmitter
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # emitter : emetteur a ajouter au système
    #
    # Fonction permettant d'ajouter un emetteur au système de particules
    #
    def addEmitter(self, emitter):
        self.emitters.append(emitter)

    # Fonction removeEmitter
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # emitter : emetteur a retirer du système
    #
    # Fonction permettant de retirer un emetteur du système de particules
    #
    def removeEmitter(self, emitter):
        self.emitters.remove(emitter)

    # Focntion isEmpty
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction permettant de determiner si le système de particules est vide où non
    #
    def isEmpty(self):
        return len(self.particules)==0 and len(self.emitters)==0

    # Focntion mustDraw
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction permettant de determiner si le système de particules doit être dessiné ou non
    #
    def mustDraw(self):
        return self.mustDrawV

    # Focntion clear
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Focntion permettant de vide rle système de particules
    #
    def clear(self):
        while len(self.emitters) > 0:
            self.emitters.remove(self.emitters[0])
        while len(self.particules) > 0:
            self.particules.remove(self.particules[0])
