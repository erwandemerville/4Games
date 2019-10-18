import pygame
try:
    import animation;
except:
    from spriteSheets import animation;

class SpriteSheet:

    def __init__(self, filename, nbLignes, nbColonnes = 1):
        try:
            self.sheet = pygame.image.load(filename).convert()
            if nbLignes < 1:
                raise ValueError("nbLignes argument of SpriteSheet constructor must be > 1")
            elif nbColonnes <1:
                raise ValueError("nbColonnes argument of SpriteSheet constructor must be > 1")
            self.frames = []
            sheetsize = self.sheet.get_size()
            w = sheetsize / nbColonnes
            h = sheetsize / nbLignes
            for c in range(nbColonnes):
                for l in range(nbLignes):
                    rct = pygame.Rect((w*c,h*l,w*c+w-1,h*l+h-1))
                    img = pygame.Surface(rct.size()).convert()
                    img.blit(self.sheet, (0,0), rct)
                    self.frames.append(img)

        except pygame.error, message:
            print 'Unable to load spritesheet image:', filename
            raise SystemExit, message

    def getFrame(self, i):
        return self.frames[i]

    def getNbFrames(self):
        return len(self.frames)

    def getanimation(self):
        return animation.Animation(self.frames)
