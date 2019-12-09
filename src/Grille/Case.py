#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

# Code écrit dans le cadre du projet Algorithmique et Developpement
# Écrit en septembre 2019 par Lucas Raulier et modifiée en Novembre 2019 par BendoTV
import pygame
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
        self.number = 0;

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

    # Fonction getNumber
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # retourne la valeur de l'attribut number
    #
    def getNumber(self):
        return self.number

    # Fonction setNumber
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # valeur : nouvelle valeur contenue dans l'attribut number de la case
    #
    # change la valeur de l'attribut number par la valeur donnée en entrée
    #
    def setNumber(self,valeur):
        self.number = valeur

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
    def draw(self, surface, x, y, width, height, selectFill=(0,0,255), hoverFill=(0,255,0), bothFill=(255,0,0)):
        if self.isSelected() and self.isHovered():
            pygame.draw.rect(surface, bothFill, (x, y, width, height))
        elif self.isSelected():
            pygame.draw.rect(surface, selectFill, (x, y, width, height))
        elif self.isHovered():
            pygame.draw.rect(surface, hoverFill, (x, y, width, height))
