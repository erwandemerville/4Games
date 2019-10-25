import random, math

class Emitter:

    def __init__(self, system, particules):
        self.system = system
        self.particules = particules

    def isDead(self):
        return False

    def spawn(self, position):
        for i in self.particules:
            self.system.addParticule(i.clone((position[0]+i.getPos()[0], position[1]+i.getPos()[1])))

class CircleEmitter(Emitter):

    def __init__(self, system, particules, rayon):
        super().__init__(system, particules)
        self.rayon = rayon

    def spawn(self, position):
        for x in range(position[0]-self.rayon, position[0]+self.rayon):
            for y in range(position[1]-self.rayon, position[1]+self.rayon):
                p = random.choice(self.particules).clone((x, y))
                xDelta = x - self.position[0]
                yDelta = y - self.position[1]
                distCenter = math.sqrt(xDelta * xDelta + yDelta * yDelta)
                distRatio = distCenter / self.rayon
                p.couleur  = (min(p.couleur[0] * distRatio,255), min(p.couleur[1] * distRatio,255), min(p.couleur[2] * distRatio,255))
                
                p.life = p.life * distRatio
                self.system.addParticule(p)
