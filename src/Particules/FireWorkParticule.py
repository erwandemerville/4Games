import Particule
from Emitters import Emitter
import random

class FireworkEmitter(Emitters.CircleEmitter):
    def __init__(self, system, particules, rayon, life, position, vitesse, gravity=0, explode=-1):
        super.__init__(system, particules, rayon)
        self.life = life
        self.position = position
        self.vitesse = vitesse
        self.gravity = gravity
        self.explode = explode

    def isDead(self):
        return life <= 0

    def explode(self): #TODO finir explosion feux d'artifice
        Nrayon = self.rayon * (1.2 + random.random())
        for x in range(position[0]-Nrayon, position[0]+Nrayon):
            for y in range(position[1]-Nrayon, position[1]+Nrayon):
                p = random.choice(self.particules).clone((x, y))
                xDelta = x - position[0]
                yDelta = y - position[1]
                distCenter = math.sqrt(xDelta * xDelta + yDelta * yDelta)
                distRatio = distCenter / Nrayon
                p.couleur = (p.couleur[0] * distRatio, p.couleur[1] * distRatio, p.couleur[2] * distRatio)
                p.life = p.life * distRatio
                self.system.addParticule(p)
        pass

    def tick(self):
        if life > 0:
            self.life = self.life - 1
            self.spawn(self.position)
            self.position = (self.position[0]+self.vitesse[0], self.position[1]+self.vitesse[1])

class FireworkParticule(Particule.Particule):
    def __init__(self, position, life, couleur=(255,255,255), vitesse=1, direction=0, deathFrames=1, gravity=0, firstCouleurTime=1):
        super().__init__(position, life, couleur, vitesse, direction, deathFrames, gravity)
        self.firstCouleurTime = self.life - firstCouleurTime
        self.couleurDiff = (couleur[0]/firstCouleurTime, couleur[1]/firstCouleurTime, couleur[2]/firstCouleurTime)

    def tick(self):
        if self.life < self.firstCouleurTime:
            self.couleur = (self.couleur[0]-self.couleurDiff[0], self.couleur[1]-self.couleurDiff[1], self.couleur[2]-self.couleurDiff[2])
        super().tick()
