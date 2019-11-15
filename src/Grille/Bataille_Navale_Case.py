# Code écrit dans le cadre du projet Algorithmique et Developpement
# Écrit en septembre 2019 par Lucas Raulier

import pygame
try:
    import Case;
except:
    from Grille import Case;

class Case(Case.Case):
    'Case pour la bataille navale'

    shotTexture = ["*", "X"]

    # Constructeur de la Case
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    #
    # Instancie une Case.
    #
    def __init__(self):
        super().__init__();
        self.contenu = None;
        self.shot = False;

    # Fonction shoot
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque que cette case à déjà été tiré dessus
    #
    def shoot(self):
        self.shot = True;

    # Fonction isShot
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Retourne un booleen indiquant si cette case est marquée comme tiré
    #
    def isShot(self):
        return self.shot;

    # Fonction setContenu
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # contenu : le contenu qui sera placé dans las case.
    #
    # Place l'argument contenu dans la case
    #
    def setContenu(self, contenu):
        self.contenu = contenu;

    # Fonction removeContenu
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Vide la case de son contenu
    #
    def removeContenu(self):
        self.contenu = None;

    # Fonction getcontenu
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Retourne le contenu de la case
    #
    def getcontenu(self):
        return self.contenu;

    # Fonction estVide
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction retournant un booleen indiquant si cette case est considérée comme vide
    #
    def estVide(self):
        return self.contenu == None;

    # Fonction contient
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # X : objet a tester
    #
    # Fonction retournant un booleen indiquant si cette case contient l'objet X.
    #
    def contient(self, X):
        return self.contenu == X;

    # Fonction draw
    #
    # ARGUMENTS OBLIGATOIRES :
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # surface : surface sur laquelle dessiner la case, doit être la surface représentant la fenêtre entière.
    # x : coordonnée horizontale du point le plus en haut a gauche de la zone ou dessiner la case.
    # y : coordonnée verticale du point le plus en haut a gauche de la zone ou dessiner la case.
    # x2 : coordonnée horizontale du point le plus en bas a droite de la zone ou dessiner la case.
    # y2 : coordonnée verticale du point le plus en bas a droite de la zone ou dessiner la case.
    #
    # ARGUMENTS OPTIONELS :
    #
    # selectFill : couleur avec laquelle remplir la case si elle est marquée comme selectionnée
    # hoverFill : couleur avec laquelle remplir la case si elle est marquée comme hovered
    # bothFill : couleur avec laquelle remplir la case si elle est marquée comme selectionnée et comme hovered
    #
    # Si selectFill n'est pas précisé, selectFill sera bleu.
    # Si hoverFill n'est pas précisé, hoverFill sera vert.
    # Si bothFill n'est pas précisé, bothFill sera rouge.
    #
    def draw(self, surface, x, y, width, height, selectFill=(0,0,255), hoverFill=(0,255,0), bothFill=(255,0,0)):
        #TODO : Ajouter l'affichage de pinned et showShip quand les images seront faites.
        if self.isSelected() and self.isHovered():
            pygame.draw.rect(surface, bothFill, (x, y, width, height))
        elif self.isSelected():
            pygame.draw.rect(surface, selectFill, (x, y, width, height))
        elif self.isHovered():
            pygame.draw.rect(surface, hoverFill, (x, y, width, height))

    def drawBoat(self, surface, x, y, width, height):
        surface.blit(self.contenu, (x, y), (0, 0, width, height))
        pass