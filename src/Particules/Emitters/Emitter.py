import random, math

class Emitter:
    "Classe de base des Emetteurs"

    # constructeur de la classe Emitter
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # system : système de particules
    # particules : tableau contenant les particules qui seront crées
    #
    def __init__(self, system, particules):
        self.system = system
        self.particules = particules

    # Fonction isDead
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction retournant un boolean indiquant si cet Emetteur est encore en fonctionnement ou non
    #
    def isDead(self):
        return False

    # Fonction spawn
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # position: position ou créer les particules
    #
    # Fonction servant a créer des particules et a les ajouter au système
    #
    def spawn(self, position):
        for i in self.particules:
            self.system.addParticule(i.clone((position[0]+i.getPos()[0], position[1]+i.getPos()[1])))

class CircleEmitter(Emitter):
    "Classe pour des Emetteurs Circulaires"

    # constructeur de la classe CircleEmitter
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # system : système de particules
    # particules : tableau contenant les particules qui seront crées
    # rayon : rayon de création des particules
    #
    def __init__(self, system, particules, rayon):
        super().__init__(system, particules)
        self.rayon = rayon

    # Fonction spawn
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # position: position du centre du cercle ou créer les particules
    #
    # Fonction servant a créer des particules et a les ajouter au système
    #
    def spawn(self, position):
        for x in range(int(position[0]-self.rayon), int(position[0]+self.rayon)):
            for y in range(int(position[1]-self.rayon), int(position[1]+self.rayon)):
                p = random.choice(self.particules).clone((x, y))
                xDelta = x - self.position[0]
                yDelta = y - self.position[1]
                distCenter = math.sqrt(xDelta * xDelta + yDelta * yDelta)
                distRatio = distCenter / self.rayon
                if distRatio < 1:
                    p.couleur  = (min(p.couleur[0],255), min(p.couleur[1],255), min(p.couleur[2],255))
                    p.life = p.life * (1 - distRatio)
                    self.system.addParticule(p)
