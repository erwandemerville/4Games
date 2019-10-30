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
