import random
import math

class BN_IA:
    "classe definissant l'IA jouant a la bataille navale"

    def __init__(self, grille, partie):
        self.tirs = []
        len_tirs = grille.largeur * grille.hauteur
        self.partie = partie
        self.grille = grille
        for i in range(len_tirs):
            self.tirs.append(i)
        self.played = False

    def determinerTirCase(self):
        case = random.randint(0, len(self.tirs)-1)
        return self.tirs[case]

    def tirer(self):
        print("TEST")
        case = self.determinerTirCase()
        print("TEST3")
        self.tirs.remove(case)
        print("TEST4 :", (case%self.grille.largeur, math.floor(case/self.grille.largeur)))
        self.partie.playTir(case=(case%self.grille.largeur, math.floor(case/self.grille.largeur)))

    def generateGrille(self):
        l = list(self.partie.bateauStr.values())
        k = 0
        for i in range(len(l)):
            x = 1
            y = 1
            direction = "Horizontale" if random.random() > 0.5 else "Verticale"
            if direction == "Horizontale":
                Verif = True
                while Verif:
                    x = random.randint(1, self.grille.largeur - len(l[i]) + 1)
                    y = random.randint(1, 10)
                    Verif = not self.partie.peutAjouterBateau(self.grille, direction, (x, y), list(self.partie.bateauStr.keys())[k])
            elif direction == "Verticale":
                Verif = True
                while Verif:
                    y = random.randint(1, self.grille.hauteur - len(l[i]) + 1)
                    x = random.randint(1, 10)
                    Verif = not self.partie.peutAjouterBateau(self.grille, direction, (x, y), list(self.partie.bateauStr.keys())[k])
            self.partie.ajouter_Bateau(self.grille, direction, (x, y), list(self.partie.bateauStr.keys())[k])
            k = k + 1

    def play(self):
        if not self.played:
            self.partie.invert_Grilles_Pos()
            self.partie.currentPlayData[1] = 1
            self.partie.data.getCurrentMenu().boutons[0].text = "voir la grille de l'adversaire"
            self.ticks = True
            self.played = True
            self.tirer()
