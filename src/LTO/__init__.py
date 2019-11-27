from random import *

from Grille import Grille, Loto_Case
from LTO import ia_loto
from LTO.ia_loto import IA_Loto

# Classe permettant de gérer une partie de loto
class Loto_Party():
    "Classe de lancement de partie de loto"
    def __init__(self,frame,data):
        self.frame = frame
        self.data = data
        #self.main_player = 0
        self.grilles_mainplayer = []
        self.boules_in_game = []
        self.boules_sorties = []
        self.tab_IA = [ia_loto.IA_Loto(self)]
        self.timer = 0
        self.reset()
        self.isStarted = False

    # Vérifie si une valeur value est dans cont
    @staticmethod
    def existInList(cont,value):
        for j in cont:
            if(j == value):
                return True
        return False

    # Génère à partir d'une grille donnée, une nouvelle grille
    @staticmethod
    def generateRandomContenuGrille(grille):
        cont = []
        for ligne in range(3):
            nb_none = 0
            for p in range(9):
                if (nb_none >= 4) or ((randint(0,1)==1) and not(nb_none <= p-4)):
                    val = randint(0, 9) + p*10
                    while Loto_Party.existInList(cont, val):
                        val = randint(0, 9) + p*10
                    cont.append(val)
                else:
                    cont.append(-1)
                    nb_none = nb_none + 1
        grille.fillByListNumeros(cont)

    # Retourne le nombre de numéros manquants pour faire un bingo
    def nbCasesLeft(self,grille):
        nb = len(grille.getListeNumeros())
        for i in grille.getListeNumeros():
            if(self.containsNbInBoulesSorties(i)):
                nb = nb - 1
        return nb

    def addGrillesToMainPlayer(self,list):
        self.grilles_mainplayer.extend(list)
    def containsNbInBoulesSorties(self,nb):
        for i in self.boules_sorties:
            if(i == nb):
                return True
        return False
    def isOneGrilleWinner(self,grille):
        for i in grille.case:
            if(not(self.containsNbInBoulesSorties(i.getNumber()))):
                return False
        return True
    def isMainPlayerWinner(self):
        for grille in self.grilles_mainplayer:
            if self.isOneGrilleWinner(grille):
                return True
        return False
    def asWinnerInIA(self):
        for ia in self.tab_IA:
            if(ia.isWinner()):
                return True
        return False
    def start(self):
        self.reset()
        self.isStarted = True

    # Fonction qui enlève tous les jetons d'une grille
    @staticmethod
    def removeAllJetonsS(grille):
        for case in grille.case:
            case.jetonIn = False
    # Fonction qui enlève tous les jetons du main_player
    def removeAllJetons(self):
        for grille in self.grilles_mainplayer:
            Loto_Party.removeAllJetonsS(grille)

    # Fonction qui affiche la fenetre
    def draw(self,frame,state):
        self.data.menus[9].draw(frame)
    # Fonction appelée toutes les secondes
    def timerTick(self):
        if self.isStarted:
            # Appelée à chaque seconde
            self.timer = self.timer + 1
            if(self.timer >= 5):
                # appel à après les 5 s
                self.timer = 0
                self.data.menus[9].nbInBoule = self.sortirUneBoule()
                self.printStateGame()
            if self.timer > 2 and (self.asWinnerInIA()):
                self.stop()
                self.data.setEtat("Loto_End")
                self.data.soundSystem.playSound("BingoIA")
                self.data.soundSystem.playMusic("triste")
                self.data.menus[10].asWin = False
            if(self.data.menus[9].nbInBoule==0):
                self.data.menus[9].titre.text = "Début de partie"
            elif(self.timer > 1):
                self.data.menus[9].titre.text = str(5-self.timer)
                self.data.soundSystem.playSound(str(5-self.timer))
            else:
                self.data.menus[9].titre.text = "Une nouvelle boule est sortie !"
        return 9

    #Fonction appelée pour arrêter le jeu
    def stop(self):
        self.isStarted = False

    # Fonction pour afficher l'état du jeu dans la console
    def printStateGame(self):
        print("Boules sorties : ",self.boules_sorties)
        print("Nombre de cases restantes du perso principal sur : grilleA=",
              self.nbCasesLeft(self.grille1_mainplayer),
              " et grilleB=",self.nbCasesLeft(self.grille2_mainplayer))
        print("GrilleA : ",self.grille1_mainplayer.getListeNumeros())
        print("GrilleB : ",self.grille2_mainplayer.getListeNumeros())
        print("List Grilles : ",self.grilles_mainplayer)
        for ia in self.tab_IA:
            print("Nombre de cases restantes de ",ia.nom," sur : grille1=",
                  self.nbCasesLeft(ia.grilles[0])," et grille2=",
                  self.nbCasesLeft(ia.grilles[1]))
            print("Grille 0 : ",ia.grilles[0].getListeNumeros())
            print("Grille 1 : ",ia.grilles[1].getListeNumeros())

    # Fonction appelée pour sortir une boule
    def sortirUneBoule(self):
        boule = choice(self.boules_in_game)
        self.boules_in_game.remove(boule)
        self.boules_sorties.append(boule)
        self.data.soundSystem.playSound("Boule")
        return boule
    # Fonction pour remettre à zéro le jeu
    def reset(self):
        self.boules_sorties.clear();self.boules_in_game.clear();self.grilles_mainplayer.clear()
        self.removeAllJetons()
        for i in range(1,90):
            self.boules_in_game.append(i)
        for ia in self.tab_IA:
            for grille in ia.grilles:
                Loto_Party.generateRandomContenuGrille(grille)

