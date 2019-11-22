from Grille import Loto_Case, Grille
from random import *

class IA_Loto():

    def __init__(self,jeu):
        self.grilles = [Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case), Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)]
        self.nom = "IA"
        self.jeu = jeu

    def existInList(self,cont,value):
        for j in cont:
            if(j == value):
                return True
        return False
    def generateRandomContenuGrille(self,grille):
        cont = [randint(1, 90)]
        for i in range(14):
            val = randint(1, 90)
            while self.existInList(cont, val):
                val = randint(1, 90)
            cont.append(val)
        grille.fillByListNumeros(cont)

    def reset(self):
        for grill in self.grilles:
            self.generateRandomContenuGrille(grill)

    def isOneGrilleWinner(self,grille):
        for i in grille.case:
            if not(self.jeu.containsNbInBoulesSorties(i.getNumber())):
                return False
        return True
    def isWinner(self):
        for i in self.grilles:
            if(self.isOneGrilleWinner(i)):
                return True
        return False
