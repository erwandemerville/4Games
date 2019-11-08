import pygame

class ParticleSystem:
    "Classe du Système de Particules"

    def __init__(self):
        self.emitters = []
        self.particules = []
        self.mustDrawV = False
        self.time = 0

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

    def draw(self, frame):
        if self.mustDraw:
            pArray = pygame.PixelArray(frame)
            for i in self.particules:
                i.draw(pArray)

    def addParticule(self, particle):
        particle.life = self.time + particle.life
        self.particules.append(particle)

    def addEmitter(self, emitter):
        self.emitters.append(emitter)

    def removeEmitter(self, emitter):
        self.emitters.remove(emitter)

    def isEmpty(self):
        return len(self.particules)==0 and len(self.emitters)==0

    def mustDraw(self):
        return self.mustDrawV

    def clear(self):
        while len(self.emitters) > 0:
            self.emitters.remove(self.emitters[0])
        while len(self.particules) > 0:
            self.particules.remove(self.particules[0])
