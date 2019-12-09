import pygame
try:
    import animation;
except:
    from spriteSheets import animation;

class SpriteSheet:
    "Classe représentant un SpriteSheet"

    # Constructeur de la classe SpriteSheet
    #
    # ARGUMENTS OBLIGATOIRES :
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # filename : fichier ou récupérer l'image entière
    # nbLignes : nombres de lignes du spriteSheet
    #
    # ARGUMENTS OPTIONELS :
    #
    # nbColonnes : nombre de colonnes du SpriteSheet, si non précisé, égal a 1
    #
    def __init__(self, filename, nbLignes, nbColonnes = 1):
        try:
            self.sheet = self.fond = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", filename)).convert()
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

    # Focntion getFrame
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # i : l'index de la frame a récuperer
    #
    # Fonction permettant de récuperer une frame du spriteSheet
    #
    def getFrame(self, i):
        return self.frames[i]

    # Focntion getNbFrames
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction retournant le nombre de frames total de l'animation
    #
    def getNbFrames(self):
        return len(self.frames)

    # Fonction getanimation
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction permettant de récuperer une animation a partir de ce spriteSheet
    #
    def getanimation(self):
        return animation.Animation(self.frames)
