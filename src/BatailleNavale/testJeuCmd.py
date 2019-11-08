import BatailleNavale

class testBN:

    def __init__(self):
        test = BatailleNavale.GameBN()
        test.cmd()
        for y in range(test.grille_J1.hauteur):
            for x in range(test.grille_J1.largeur):
                print(test.grille_J1.getCaseByCoords(x, y).contenu, end=" ")
            print()