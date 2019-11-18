from src.Grille import Grille, Loto_Case
from src.LTO import *


class IA_Loto():

    def __init__(self,jeu):
        self.grilles = [Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case), Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)]
        self.nom = "IA"
        self.jeu = jeu

    def reset(self):
        Menu_LotoChoose.generateRandomContenuGrille(self.grilles[0])
        Menu_LotoChoose.generateRandomContenuGrille(self.grilles[1])

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
