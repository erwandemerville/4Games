# Code écrit dans le cadre du projet Algorithmique et Developpement
# Écrit en septembre 2019 par Lucas Raulier

import math;
try:
    import Loto_Case;
except:
    from Grille import Loto_Case;

class Grille:
  'Classe permettant de gérer la grille'

  # Constructeur de la grille
  #
  # self : instance crée par le constructeur, ne doit pas être mis en argument.
  # largeur : nombre de case de large
  # hauteur : nombre de cases de haut
  # x1 : coordonnée horizontale du point le plus en haut a gauche de la grille
  # y1 : coordonnée verticale du point le plus en haut a gauche de la grille
  # x2 : coordonnée horizontale du point le plus en bas a droite de la grille
  # y2 : coordonnée verticlae du point le plus en bas a droite de la grille
  # module : module contenant une classe nommée "Case" qui sera instancié par la grille (largeur * hauteur) fois.
  #
  # Permet d'instancier une grille simple contenant (largeur * hauteur) case qui sera
  # contenue dans le rectangle formé par les points (x1, y1) et (x2, y2).
  #
  def __init__(self, largeur, hauteur, x1, y1, x2, y2, module):
    self.largeur = largeur;
    self.hauteur = hauteur;
    self.x = x1;
    self.x2 = x2;
    self.y = y1;
    self.y2 = y2;
    self.case = [];
    for i in range(0, self.largeur * self.hauteur):
        if module == Loto_Case:
            self.case.append(module.Case(i+1));
        else:
            self.case.append(module.Case());

  # Fonction getCase
  #
  # self : instance de la classe, ne doit pas être mis en argument.
  # id : identifiant de la case pouvant être retrouvé via l'opération suivante :
  # y * Largeur_de_la_grille + x => x représentant une colonne de la grille et y représente un ligne.
  #
  # Fonction retournant une case via l'id passé en argument.
  # Cette fonction est adaptée pour un appel via une boucle for.
  #
  def getCase(self, id):
    if (id < self.largeur * self.hauteur):
      return self.case[id];
    else:
      return None;

  # Fonction getCaseByCoords
  #
  # self : instance de la classe, ne doit pas être mis en argument.
  # x : colonne sur laquelle la case se trouve.
  # y : ligne sur laquelle la case se trouve.
  #
  # Fonction retournant une case via le point (x, y) passé en argument.
  # Cette fonction est adaptée pour un appel normale.
  #
  def getCaseByCoords(self, x, y):
    if y * self.largeur + x < self.largeur * self.hauteur:
      return self.case[y * self.largeur + x];
    else:
      return None;


  # Fonction getCaseByClick
  #
  # self : instance de la classe, ne doit pas être mis en argument.
  # x : coordonée horizontale du clic.
  # y : coordonée verticale du clic.
  #
  # Fonction retournant une case via le point (x, y) passé en argument.
  # Cette fonction est adaptée pour un appel provoqué par un clic de souris.
  #
  def getCaseByClick(self, x, y):
    if x <= self.x or y <= self.y or x >= self.x2 or y >= self.y2 :
        return None;

    cx = int(math.floor((x-self.x) / ((abs(self.x2-self.x) / self.largeur))));
    cy = int(math.floor((y-self.y) / ((abs(self.y2-self.y) / self.hauteur))));

    return self.getCaseByCoords(cx, cy);

  # Fonction selectCase
  #
  # self : instance de la classe, ne doit pas être mis en argument.
  # x : coordonée horizontale du clic.
  # y : coordonée verticale du clic.
  #
  # Fonction marque comme sélectionnée la case pointée par le point (x, y) passé en argument
  # et marque comme non-sélectionnée toutes les cases non pointées par le point (x, y).
  # Cette fonction est adaptée pour un appel provoqué par un clic de souris.
  #
  def selectCase(self, x, y):
    case = self.getCaseByClick(x, y);
    if case != None:
        case.select();
        for i in range(0, self.largeur * self.hauteur):
            if self.getCase(i) != case:
                self.getCase(i).deselect();
    else:
        for i in range(0, self.largeur * self.hauteur):
            self.getCase(i).deselect();

  # Fonction hoverCase
  #
  # self : instance de la classe, ne doit pas être mis en argument.
  # x : coordonée horizontale du clic.
  # y : coordonée verticale du clic.
  #
  # Définition du terme "hovered" : une case est considérée comme "hovered" quad le pointeur de la souris
  # désigne cette case.
  #
  # Fonction marque comme hovered la case pointée par le point (x, y) passé en argument
  # et marque comme non-sélectionnée toutes les cases non pointées par le point (x, y).
  # Cette fonction est adaptée pour un appel provoqué par un clic de souris.
  #
  def hoverCase(self, x, y):
    case = self.getCaseByClick(x, y);
    if case != None:
        case.hover();
        for i in range(0, self.largeur * self.hauteur):
            if self.getCase(i) != case:
                self.getCase(i).unhover();
    else:
        for i in range(0, self.largeur * self.hauteur):
            self.getCase(i).unhover();

  # Fonction estVide
  #
  # self : instance de la classe, ne doit pas être mis en argument.
  #
  # Fonction retournant un booleen indiquant si cette grille est considérée comme vide
  #
  def estVide(self):
    for i in range(0, self.hauteur):
        for j in range(0, self.largeur):
            if not(self.getCase(j, i).estVide()):
                return False;
    return True;

  # Fonction contient
  #
  # self : instance de la classe, ne doit pas être mis en argument.
  # X : objet a tester
  #
  # Fonction retournant un booleen indiquant si une case de la grille contient l'objet X.
  #
  def contient(self, X):
    for i in range(0, self.hauteur):
        for j in range(0, self.largeur):
            if self.getCase(j, i).contient(X):
                return True;
    return False;

  # Fonction draw
  #
  # ARGUMENTS OBLIGATOIRES :
  #
  # self : instance de la classe, ne doit pas être mis en argument.
  # canvas : canvas sur lequel dessiner la grille
  # couleur : couleur avec laquelle les lignes de la grille doivent être déssinées.
  #
  # ARGUMENTS OPTIONELS :
  #
  # x : coordonnée horizontale du point le plus en haut a gauche de la zone ou dessiner la grille.
  # y : coordonnée verticale du point le plus en haut a gauche de la zone ou dessiner la grille.
  # x2 : coordonnée horizontale du point le plus en bas a droite de la zone ou dessiner la grille.
  # y2 : coordonnée verticlae du point le plus en bas a droite de la zone ou dessiner la grille.
  #
  # Si une ou plusieurs des coordonnées ne sont pas précisées, les points de la grille seront
  # pris comme référence pour les points non précisés.
  # Les tailles de la grille et des cases sont déterminées en fontion des points utilisés.
  #
  # caseSelectColor : couleur appliquée sur une case marquée comme sélectionée.
  # caseHoverColor : couleur appliquée sur une case marquée comme hovered (Le pointeur de la souris se trouve sur la case).
  # caseSelectHoverColor : couleur appliquée sur une case marquée comme sélectionée et hovered.
  #
  # Si une ou plusieurs des couleurs ne sont pas précisées,
  # elles seront calculées en utilisant l'argument couleur comme base.
  #
  def draw(self, canvas, couleur, x = -1, y = -1, x2 = -1, y2 = -1, caseSelectColor=None, caseHoverColor=None, caseSelectHoverColor=None):
    if x == -1:
        x = self.x;
    if x2 == -1:
        x2 = self.x2;

    if y == -1:
        y = self.y;
    if y2 == -1:
        y2 = self.y2;
    largeur = abs(x2-x);
    hauteur = abs(y2-y);
    case_Largeur = largeur / self.largeur;
    case_Hauteur = hauteur / self.hauteur;

    if caseSelectColor == None:
        caseSelectColor = "#"+hex((int(couleur[1:], 16)-0x0b0b0b))[2:];

    if caseSelectHoverColor == None:
        caseSelectHoverColor = "#"+hex((int(couleur[1:], 16)-0x040404))[2:];

    if caseHoverColor == None:
        caseHoverColor = "#"+hex((int(couleur[1:], 16)-0x080808))[2:];

    for i in range(0, self.hauteur):
        for j in range(0, self.largeur):
            self.getCaseByCoords(j, i).draw(canvas, x+j * case_Largeur, y+i * case_Hauteur, x+(j*case_Largeur) + case_Largeur, y+(i*case_Hauteur) + case_Hauteur, selectFill=caseSelectColor, hoverFill=caseHoverColor, bothFill=caseSelectHoverColor);

    canvas.create_line(x, y, x2, y, fill=couleur);
    canvas.create_line(x, y, x, y2, fill=couleur);
    canvas.create_line(x2, y, x2, y2, fill=couleur);
    canvas.create_line(x, y2, x2, y2, fill=couleur);
    for i in range(0, self.hauteur):
        canvas.create_line(x, y + (case_Hauteur*i), x + largeur, y + (case_Hauteur*i), fill=couleur);

    for i in range(0, self.largeur):
        canvas.create_line(x + (case_Largeur*i), y, x + (case_Largeur*i), y + hauteur, fill=couleur);
