from random import *

from Grille import Grille, Loto_Case
from LTO import ia_loto


class Loto_Party():
    "Classe de lancement de partie de loto"
    def __init__(self,frame,data):
        self.frame = frame
        self.data = data
        self.main_player = 0
        self.grille1_mainplayer = Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)
        self.grille2_mainplayer = Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)
        self.boules_in_game = []
        self.boules_sorties = []
        self.tab_IA = [ia_loto.IA_Loto(self)]
        self.timer = 0
        self.reset()

    def nbCasesLeft(self,grille):
        nb = len(grille.getListeNumeros())
        for i in grille.getListeNumeros():
            if(self.containsNbInBoulesSorties(i)):
                nb = nb - 1
        return nb

    def addGrilleToMainPlayer(self,grilleA,grilleB):
        self.grille1_mainplayer = grilleA
        self.grille2_mainplayer = grilleB

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
        return self.isOneGrilleWinner(self.grille1_mainplayer) or self.isOneGrilleWinner(self.grille2_mainplayer)
    def asWinnerInIA(self):
        for ia in self.tab_IA:
            if(ia.isWinner()):
                return True
        return False
    def start(self):
        self.reset()

    def draw(self,frame,state):
        self.data.menus[9].draw(frame)
    def timerTick(self):
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
            self.data.soundSystem.playMusic("triste")
            self.data.menus[10].asWin = False
        if(self.data.menus[9].nbInBoule==0):
            self.data.menus[9].titre.text = "Début de partie"
        elif(self.timer > 1):
            self.data.menus[9].titre.text = str(5-self.timer)
        else:
            self.data.menus[9].titre.text = "Une nouvelle boule est sortie !"
        return 9

    def stop(self):
        pass

    def printStateGame(self):
        print("Boules sorties : ",self.boules_sorties)
        print("Nombre de cases restantes du perso principal sur : grilleA=",
              self.nbCasesLeft(self.grille1_mainplayer),
              " et grilleB=",self.nbCasesLeft(self.grille2_mainplayer))
        print("GrilleA : ",self.grille1_mainplayer.getListeNumeros())
        print("GrilleB : ",self.grille2_mainplayer.getListeNumeros())
        for ia in self.tab_IA:
            print("Nombre de cases restantes de ",ia.nom," sur : grille1=",
                  self.nbCasesLeft(ia.grilles[0])," et grille2=",
                  self.nbCasesLeft(ia.grilles[1]))
            print("Grille 0 : ",ia.grilles[0].getListeNumeros())
            print("Grille 1 : ",ia.grilles[1].getListeNumeros())

    def sortirUneBoule(self):
        boule = choice(self.boules_in_game)
        self.boules_in_game.remove(boule)
        self.boules_sorties.append(boule)
        return boule
    def reset(self):
        self.boules_sorties.clear();self.boules_in_game.clear()
        for i in range(1,90):
            self.boules_in_game.append(i)
        for ia in self.tab_IA:
            ia.reset()

