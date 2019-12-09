from Particules import Particule
from Particules.Emitters import Emitter as PE
import random, math

class FireworkEmitter(PE.CircleEmitter):
    "Classe pour des Emetteurs de feux d'artifice"

    # constructeur de la classe FireworkEmitter
    #
    # ARGUMENTS OBLIGATOIRES :
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # system : système de particules
    # particules : tableau contenant les particules qui seront crées
    # couleurs : couleurs des extremités de la génération, l'entre deux sera calculé
    # rayon : rayon de créationdes particules, ce rayon sera multiplé lors de l'explosion
    # life : temps de vie de l'Emetteur en itération de la boucle du main
    # position : position de l'Emetteur
    # vitesse : vitesse de l'Emetteur sous forme (vx, vy)
    #
    # ARGUMENTS OPTIONNELS :
    #
    # gravity : force de la gravité a laquelle l'Emetteur est soumis
    # explode : force de l'explosion de l'Emetteur, si non indiqué ou 0, l'Emetteur n'explosera pas
    #
    def __init__(self, system, particules, couleurs, rayon, life, position, vitesse, gravity=0, explode=0):
        super().__init__(system, particules, rayon)
        self.life = life
        self.position = position
        self.vitesse = vitesse
        self.gravity = gravity*0.1
        self.explode = explode
        self.couleurs = couleurs;
        for i in range(0, min(len(self.couleurs), 2)):
            self.couleurs[i] = (max(0, min(self.couleurs[i][0], 255)), max(0, min(self.couleurs[i][1], 255)), max(0, min(self.couleurs[i][2], 255)))
        if len(self.couleurs) > 1:
            self.colorDiff = (self.couleurs[0][0] - self.couleurs[1][0], self.couleurs[0][1] - self.couleurs[1][1], self.couleurs[0][2] - self.couleurs[1][2])
        else:
            self.colorDiff = (0,0,0)

    # Fonction isDead
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction retournant un boolean indiquant si cet Emetteur est encore en fonctionnement ou non
    #
    def isDead(self):
        return self.life < 1

    # Fonction explodeF
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction gérant l'explosion de l'Emetteur
    #
    def explodeF(self): #TODO finir explosion feux d'artifice
        Nrayon = round(self.rayon * (self.explode+1 + random.random()))
        for x in range(int(self.position[0]-Nrayon), int(self.position[0]+Nrayon)):
            for y in range(int(self.position[1]-Nrayon), int(self.position[1]+Nrayon)):
                p = random.choice(self.particules).clone((x, y))
                xDelta = x - self.position[0]
                yDelta = y - self.position[1]
                distCenter = math.sqrt(xDelta * xDelta + yDelta * yDelta)
                distRatio = distCenter / Nrayon
                if distRatio < 1 :
                    distRatioInv = (1-distRatio)
                    p.couleur = (min(self.couleurs[0][0] - self.colorDiff[0]*distRatio,255), min(self.couleurs[0][1] - self.colorDiff[1]*distRatio,255), min(self.couleurs[0][2] - self.colorDiff[2]*distRatio,255))
                    p.life = p.life * (1.4 - (1.4*distRatio) + (0.0390625*math.sqrt(distRatioInv)) + random.random()*1.2)
                    self.system.addParticule(p)

        nb = 4+random.random()*4
        for i in range(0, int(nb)):
            self.system.addEmitter(FireworkEmitter(self.system, self.particules, self.couleurs, self.rayon/2, 1000, self.position, ((2*self.explode) * math.cos(math.radians(i * (360/nb))), (2*self.explode) * math.sin(math.radians(i * (360/nb)))), 1, 0))

        pass

    # Fonction applyGravity
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction appliquant la gravité a l'Emetteur
    #
    def applyGravity(self):
        self.vitesse = (self.vitesse[0], self.vitesse[1]+self.gravity)

    # Fonction spawn
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # position: position ou créer les particules
    #
    # Fonction servant a créer des particules et a les ajouter au système
    #
    def spawn(self, position):
        colorDiff = (self.couleurs[0][0] - self.couleurs[1][0], self.couleurs[0][1] - self.couleurs[1][1], self.couleurs[0][2] - self.couleurs[1][2])
        for x in range(int(position[0]-self.rayon), int(position[0]+self.rayon)):
            for y in range(int(position[1]-self.rayon), int(position[1]+self.rayon)):
                p = random.choice(self.particules).clone((x, y))
                xDelta = x - self.position[0]
                yDelta = y - self.position[1]
                distCenter = math.sqrt(xDelta * xDelta + yDelta * yDelta)
                distRatio = distCenter / self.rayon
                if distRatio < 1:
                    distRatioInv = (1-distRatio)
                    p.couleur = (min(self.couleurs[0][0] - self.colorDiff[0]*distRatio,255), min(self.couleurs[0][1] - self.colorDiff[1]*distRatio,255), min(self.couleurs[0][2] - self.colorDiff[2]*distRatio,255))
                    p.life = p.life * (1 - (1*distRatio) + (0.0390625*math.sqrt(distRatioInv)) + random.random()*(2 - (2*distRatio)))
                    self.system.addParticule(p)
        pass

    # Fonction tick
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction executant des actions a chaque itération de la boucle du main
    #
    def tick(self):
        self.life = self.life - 1
        if self.life > 1:
            self.spawn(self.position)
            self.position = (self.position[0]+self.vitesse[0], self.position[1]+self.vitesse[1])
            self.applyGravity()
            if (self.gravity > 0 and self.position[1] > 480):
                self.life = 0
        elif self.explode != 0:
            self.explodeF()
