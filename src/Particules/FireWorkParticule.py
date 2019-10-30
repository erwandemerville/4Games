from Particules import Particule
from Particules.Emitters import Emitter as PE
import random, math

class FireworkEmitter(PE.CircleEmitter):
    def __init__(self, system, particules, rayon, life, position, vitesse, gravity=0, explode=0):
        super().__init__(system, particules, rayon)
        self.life = life
        self.position = position
        self.vitesse = vitesse
        self.gravity = gravity*0.1
        self.explode = explode

    def isDead(self):
        return self.life <= 0

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
                    p.couleur = (min(p.couleur[0],255), min(p.couleur[1],255), min(p.couleur[2],255))
                    p.life = p.life * (8 - (8*distRatio) - (1.25*math.pow(distRatio, 2)))
                    self.system.addParticule(p)

        nb = 4+random.random()*4
        for i in range(1, int(nb)):
            self.system.addEmitter(FireworkEmitter(self.system, self.particules, self.rayon/2, 1000, self.position, ((2*self.explode) * math.cos(math.radians(i * (360/nb))), (2*self.explode) * math.sin(math.radians(i * (360/nb)))), 1, 0))

        pass

    def applyGravity(self):
        self.vitesse = (self.vitesse[0], self.vitesse[1]+self.gravity)

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
