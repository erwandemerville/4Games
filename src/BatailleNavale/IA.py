import random
import math

class BN_IA:
    "classe definissant l'IA jouant a la bataille navale"

    # Constructeur de la classe IA
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # grille : grille de l'IA
    # partie : instance de la partie ou se trouve l'IA
    #
    def __init__(self, grille, partie):
        self.tirs = []
        len_tirs = grille.largeur * grille.hauteur
        self.partie = partie
        self.grille = grille
        for i in range(len_tirs): # Génération d'un tableau contenant les case qui restent a viser
            self.tirs.append(i)
        self.played = False

    # Fonction determinerTirCase
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction servant a determiner ou tirer. A noter que l'IA ne tirera jamias 2 fois au même endroit
    #
    def determinerTirCase(self):
        case = random.randint(0, len(self.tirs)-1)              # On tire à un endroit
        return self.tirs[case]                                  # aléatoire de la grille

    # Fonction tirer
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction servant a l'IA pour tirer
    #
    def tirer(self):
        case = self.determinerTirCase()
        self.tirs.remove(case)
        self.partie.playTir(case=(case%self.grille.largeur, math.floor(case/self.grille.largeur)))

    # Fonction generateGrille
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction plaçant les bateaux dans la grille de l'IA
    #
    def generateGrille(self):
        l = list(self.partie.bateauStr.values()) # On récupère tous les types de bateaux
        k = 0
        for i in range(len(l)): # Pour chaque type de bateau
            x = 1
            y = 1
            direction = "Horizontale" if random.random() > 0.5 else "Verticale" # Génération aléatoire d'une direction
            if direction == "Horizontale":
                Verif = True
                while Verif:
                    x = random.randint(1, self.grille.largeur - len(l[i]) + 1)  # On génère des coordonnées
                    y = random.randint(1, 10)                                   # aléatoires pour placer le bateau
                    # On tente de placer le bateau et si on peut pas, on recommence
                    Verif = not self.partie.peutAjouterBateau(self.grille, direction, (x, y), list(self.partie.bateauStr.keys())[k])
            elif direction == "Verticale":
                Verif = True
                while Verif:
                    y = random.randint(1, self.grille.hauteur - len(l[i]) + 1)  # On génère des coordonnées
                    x = random.randint(1, 10)                                   # aléatoires pour placer le bateau
                    # On tente de placer le bateau et si on peut pas, on recommence
                    Verif = not self.partie.peutAjouterBateau(self.grille, direction, (x, y), list(self.partie.bateauStr.keys())[k])
            self.partie.ajouter_Bateau(self.grille, direction, (x, y), list(self.partie.bateauStr.keys())[k]) # On ajoute le bateau dans la grille
            k = k + 1

    # Fonction play
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction permettant a l'IA de jouer
    #
    def play(self):
        if not self.played: # On teste si l'IA ne vient pas de jouer
            self.partie.invert_Grilles_Pos()    # On se place sur la grille du joueur
            self.partie.currentPlayData[1] = 1  # On se place sur la grille du joueur
            self.partie.data.getCurrentMenu().boutons[0].text = "voir la grille de l'adversaire" # On change le boutons "voir la grille de l'adversaire"/"voir votre grille"
            self.ticks = True
            self.played = True
            self.tirer()
