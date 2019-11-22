# Code écrit dans le cadre du projet Algorithmique et Developpement
# Écrit en septembre 2019 par Lucas Raulier

import pygame
try:
    import Case;
except:
    from Grille import Case;

class Case(Case.Case):
    'Case pour le loto'

    # Constructeur de la Case
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # number : le nombre qui sera contenu dans cette case. Ce nombre sera constant
    #
    # Instancie une Case.
    #
    def __init__(self, number):
        super().__init__();
        self.number = number;
        self.choosen = False;
        self.jetonIn = False;

    # Fonction choose
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque cette case comme choisie
    #
    def choose(self):
        self.choosen = True;

    # Fonction choose
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque cette case comme non-choisie
    #
    def unChoose(self):
        self.choosen = False;

    # Fonction choose
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # retourne le nombre contenu dans cette case.
    #
    def getNumber(self):
        return self.number;

    # Fonction estVide
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction retournant un booleen indiquant si cette case est considérée comme vide
    #
    def estVide(self):
        return not(self.choosen);

    # Fonction contient
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # X : objet a tester
    #
    # Fonction retournant un booleen indiquant si cette case contient l'objet X.
    #
    def contient(self, X):
        return self.number == X;

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
    # selectFill : tuple représentant la couleur avec laquelle remplir la case si elle est marquée comme selectionnée
    # hoverFill : tuple représentant la couleur avec laquelle remplir la case si elle est marquée comme hovered
    # bothFill : tuple représentant la couleur avec laquelle remplir la case si elle est marquée comme selectionnée et comme hovered
    # textFill : tuple représentant la couleur avec laquelle écrire le nombre contenu dans la case (si celui-ci est valide).
    # textFont : police d'écriture avec laquelle écrire le nombre contenu dans la case (si celui-ci est valide).
    # choosenFill : tuple représentant la couleur avec laquelle remplir la case si elle est marquée comme choisie
    #
    # Si selectFill n'est pas précisé, selectFill sera (0,0,255)).
    # Si hoverFill n'est pas précisé, hoverFill sera (0,255,0)).
    # Si bothFill n'est pas précisé, bothFill sera (255,0,0)).
    # Si textFill n'est pas précisé, textFill sera (0,0,0)).
    # Si textFont n'est pas précisé, textFont sera "Impact".
    # Si choosenFill n'est pas précisé, choosenFill sera (117,117,0).
    #
    def draw(self, surface, x, y, width, height, selectFill=(0,0,255), hoverFill=(0,255,0), bothFill=(255,0,0), textFill=(0,0,0), textFont="Impact", choosenFill=(117,117,0)):
        # TODO: faire la classe quand le hud sera fait
        if self.isSelected() and self.choosen and self.isHovered():
            pygame.draw.rect(surface, (choosenFill[0]-49,choosenFill[1]-49, choosenFill[2]), (x, y, width, height))
        elif self.isSelected() and self.choosen:
            pygame.draw.rect(surface, (choosenFill[0]-24,choosenFill[1]-24, choosenFill[2]), (x, y, width, height))
        elif self.choosen:
            pygame.draw.rect(surface, choosenFill, (x, y, width, height))
        elif self.isSelected() and self.isHovered():
            pygame.draw.rect(surface, bothFill, (x, y, width, height))
        elif self.isSelected():
            pygame.draw.rect(surface, selectFill, (x, y, width, height))
        elif self.isHovered():
            pygame.draw.rect(surface, hoverFill, (x, y, width, height))

        if self.number != 0:
            fontSize = height-6;
            if self.number > 9:
                fontSize -= 6;
            police = pygame.font.SysFont(textFont,int(fontSize))
            label = police.render(str(self.number), 1, textFill)
            surface.blit(label, (x+width/3, y))
        if self.jetonIn:
            pygame.draw.circle(surface,(0,0,0),(int(x+width/2),int(y+height/2)),14)
            pygame.draw.circle(surface,(242,255,128),(int(x+width/2),int(y+height/2)),13)
