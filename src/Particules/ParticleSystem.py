class ParticleSystem:
    "Classe du Système de Particules"

    def __init__(self):
        self.emitters = []
        self.particules = []

    def tick(self):
        for i in self.particules:
            if i.isDead():
                self.particules.remove(i)
            else:
                i.tick()
        for i in self.emitters:
            if i.isDead():
                self.emitters.remove(i)
            else:
                i.tick()

    def draw(self, frame):
        for i in self.particules:
            i.draw(frame)

    def addParticule(self, particle):
        self.particules.append(particle)

    def addEmitter(self, emitter):
        self.emitters.append(emitter)

    def removeEmitter(self, emitter):
        self.emitters.remove(emitter)

    def isEmpty(self):
        return len(self.particules)==0 and len(self.emitters)==0
