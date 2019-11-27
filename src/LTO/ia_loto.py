from Grille import Loto_Case, Grille

# Classe gérant une IA


class IA_Loto():

    def __init__(self,jeu):
        self.grilles = [Grille.Grille(9, 3, 0, 0, 300, 90, Loto_Case), Grille.Grille(9, 3, 0, 0, 300, 90, Loto_Case)]
        self.nom = "IA"
        self.jeu = jeu

    # Vérifie si une valeur value est dans cont
    @staticmethod
    def existInList(cont,value):
        for j in cont:
            if(j == value):
                return True
        return False

    # Détermine si la grille entrée en paramètre est gagnante
    def isOneGrilleWinner(self,grille):
        for i in grille.case:
            if not(self.jeu.containsNbInBoulesSorties(i.getNumber())) and not(i.getNumber== -1):
                return False
        return True
    # Détermine si l'IA a gagné
    def isWinner(self):
        for i in self.grilles:
            if(self.isOneGrilleWinner(i)):
                return True
        return False
