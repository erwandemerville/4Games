#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

# Code écrit dans le cadre du projet Algorithmique et Developpement
# Écrit en septembre 2019 par Lucas Raulier
from pygame.locals import *

class Case:
    'Classe servant de base pour les Cases'

    # Constructeur de la Case
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    #
    # Instancie une Case.
    #
    def __init__(self):
        self.selected = False;
        self.hovered = False;

    # Fonction select
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque cette case comme sélectionée
    #
    def select(self):
        self.selected = True;

    # Fonction deselect
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque cette case comme non-sélectionée
    #
    def deselect(self):
        self.selected = False;

    # Fonction isSelected
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Retourne un booleen indiquant si cette case est marquée comme sélectionée.
    #
    def isSelected(self):
        return self.selected;

    # Fonction hover
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque cette case comme hovered
    #
    def hover(self):
        self.hovered = True;

    # Fonction unhover
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Marque cette case comme non-hovered
    #
    def unhover(self):
        self.hovered = False;

    # Fonction isHovered
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Retourne un booleen indiquant si cette case est marquée comme hovered.
    #
    def isHovered(self):
        return self.hovered;

    # Fonction estVide
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction retournant un booleen indiquant si cette case est considérée comme vide
    #
    def estVide(self):
        return True;

    # Fonction contient
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # X : objet a tester
    #
    # Fonction retournant un booleen indiquant si cette case contient l'objet X.
    #
    def contient(self, X):
        return False;

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
    # Si une case n'est pas marquée comme sélectionée ou hovered, cette case sera affichée comme vide.
    #
    def draw(self, surface, x, y, x2, y2, selectFill=(0,0,255), hoverFill=(0,255,0), bothFill=(255,0,0)):
        if self.isSelected() and self.isHovered():
            pygame.draw.rect(surface, bothFill, (x, y), (x2, y2))
        elif self.isSelected():
            pygame.draw.rect(surface, selectFill, (x, y), (x2, y2))
        elif self.isHovered():
            pygame.draw.rect(surface, hoverFill, (x, y), (x2, y2))
