from Particules import Particule
from Particules.Emitters import Emitter as PE
import random, math

class FireworkEmitter(PE.CircleEmitter):
    def __init__(self, system, particules, rayon, life, position, vitesse, gravity=0, explode=-1):
        super().__init__(system, particules, rayon)
        self.life = life
        self.position = position
        self.vitesse = vitesse
        self.gravity = gravity
        self.explode = explode

    def isDead(self):
        return self.life <= 0

    def explode(self): #TODO finir explosion feux d'artifice
        Nrayon = self.rayon * (2 + random.random())
        for x in range(self.position[0]-Nrayon, self.position[0]+Nrayon):
            for y in range(self.position[1]-Nrayon, self.position[1]+Nrayon):
                p = random.choice(self.particules).clone((x, y))
                xDelta = x - self.position[0]
                yDelta = y - self.position[1]
                distCenter = math.sqrt(xDelta * xDelta + yDelta * yDelta)
                distRatio = distCenter / Nrayon
                p.couleur = (min(p.couleur[0] * distRatio,255), min(p.couleur[1] * distRatio,255), min(p.couleur[2] * distRatio,255))
                print("Explode : ",p.couleur)
                p.life = p.life * distRatio
                self.system.addParticule(p)
        pass

    def tick(self):
        if self.life > 0:
            self.life = self.life - 1
            self.spawn(self.position)
            self.position = (self.position[0]+self.vitesse[0], self.position[1]+self.vitesse[1])
        elif self.explode != -1:
            self.explode()

class FireworkParticule(Particule.Particule):
    def __init__(self, position, life, couleur=(255,255,255), vitesse=1, direction=0, deathFrames=1, gravity=0, firstCouleurTime=1):
        super().__init__(position, life, couleur, vitesse, direction, deathFrames, gravity)
        print("Constructeur : ",couleur)
        self.firstCouleurTime = self.life - firstCouleurTime
        self.couleurDiff = (math.ceil(couleur[0]/firstCouleurTime), math.ceil(couleur[1]/firstCouleurTime), math.ceil(couleur[2]/firstCouleurTime))
        print("const du fw particule : ",self.couleurDiff)

    def tick(self):
        super().tick()
        if self.life < self.firstCouleurTime:
            self.couleur = (min(abs(self.couleur[0]-self.couleurDiff[0]),255), min(abs(self.couleur[1]-self.couleurDiff[1]),255), min(abs(self.couleur[2]-self.couleurDiff[2]),255))
        print("tick du fw particule : ",self.couleur," self.life = ",self.life)
