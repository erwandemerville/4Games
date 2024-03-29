# Code écrit dans le cadre du projet Algorithmique et Developpement
# Écrit en septembre 2019 par Lucas Raulier

import pygame
import math
try:
    import Case;
except:
    from Grille import Case;

class Case(Case.Case):
    'Case pour la bataille navale'

    # Constructeur de la Case
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    #
    # Instancie une Case.
    #
    def __init__(self):
        super().__init__();
        self.contenu = None; # Sert a contenir l'image de la partie du bateau a dessiner dans cette case
        self.shot = False; # Booleen indiquant que cette case a déjà été tirée dessus ou non

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
    def draw(self, surface, x, y, width, height, selectFill=(0,0,255), hoverFill=(0,255,0), bothFill=(255,0,0), showShip=False):
        if self.isSelected() and self.isHovered():
            pygame.draw.rect(surface, bothFill, (x, y, width, height))
        elif self.isSelected():
            pygame.draw.rect(surface, selectFill, (x, y, width, height))
        elif self.isHovered():
            pygame.draw.rect(surface, hoverFill, (x, y, width, height))

        # On determine si on doit dessiner le contenu de l'image et on le dessine si oui
        if self.contenu != None and showShip:
            surface.blit(self.contenu, (x, y, width, height))

        # On determine quoi dessiner si la case est marquée comme "tirée"
        if self.shot:
            if self.estVide(): # On dessiner un cercle bleu foncée
                pygame.draw.circle(surface, (1, 20, 60), (math.ceil(x+width/2), math.ceil(y + height/2)), 12)
            else: # On dessine une croix
                pygame.draw.line(surface, (145, 30, 50), (x+1, y+1), (x+width-1, y+height-1), 4)
                pygame.draw.line(surface, (145, 30, 50), (x+width-1, y+1), (x-1, y+height-1), 4)
