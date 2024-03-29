#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

# Code écrit dans le cadre du projet Algorithmique et Developpement
# Écrit en septembre 2019 par Lucas Raulier

import pygame
try:
    import Case
except:
    from Grille import Case

class Case(Case.Case):
    'Case pour le sudoku'

    # Constructeur de la Case
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    #
    # Instancie une Case.
    #
    def __init__(self, number=0):
        super().__init__()
        self.number = number

    # Fonction getNumber
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    #
    # Retourne un entier representant le nombre contenu dans la case.
    # Si cette fonction retourne 0, c'est que la case est vide.
    #
    def getNumber(self):
        return self.number

    # Fonction setNumber
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # number : nombre par lequel remplacer le nombre actuellement contenu dans las case.
    #
    # Retourne un entier representant le nombre contenu dans la case.
    # Mettre le nombre contenu dans cette Case à 0 consistera a vider la case.
    #
    def setNumber(self, number):
        self.number = number

    # Fonction estVide
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction retournant un booleen indiquant si cette case est considérée comme vide
    #
    def estVide(self):
        return self.number == 0

    # Fonction contient
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # X : objet a tester
    #
    # Fonction retournant un booleen indiquant si cette case contient l'objet X.
    #
    def contient(self, X):
        return self.number == X

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
    # textFill : couleur avec laquelle écrire le nombre contenu dans la case (si celui-ci est valide).
    # textFont : police d'écriture avec laquelle écrire le nombre contenu dans la case (si celui-ci est valide).
    #
    # Si selectFill n'est pas précisé, selectFill sera bleu.
    # Si hoverFill n'est pas précisé, hoverFill sera vert.
    # Si bothFill n'est pas précisé, bothFill sera rouge.
    # Si textFill n'est pas précisé, textFill sera blanc.
    # Si textFont n'est pas précisé, textFont sera "Comic".
    #
    def draw(self, surface, x, y, width, height, selectFill=(0,0,255), hoverFill=(0,255,0), bothFill=(255,0,0), textFill=(255,255,255), textFont="Impact"):
        # TODO: faire la classe quand le hud sera fait
        super().draw(surface, x, y, width, height, selectFill, hoverFill, bothFill)
        if self.number != 0:
            fontSize = height-6
            police = pygame.font.SysFont(textFont,int(fontSize))
            label = police.render(str(self.number), 1, textFill)
            surface.blit(label, (x+(width-1)/3, y))
