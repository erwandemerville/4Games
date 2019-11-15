import BatailleNavale

class testBN:

    def __init__(self, data):
        test = BatailleNavale.GameBN(data)
        test.cmd()
        for y in range(test.grille_J1.hauteur):
            for x in range(test.grille_J1.largeur):
                case = test.grille_J1.getCaseByCoords(x, y)
                if (case.isShot()):
                    if (case.estVide()):
                        print("*", end=" ")
                    else:
                        print("X", end=" ")
                else:
                    print(case.contenu, end=" ")
            print()
        if test.checkVictory(test.grille_J1):
            print("Bien ouej mon reuf")