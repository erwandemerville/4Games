import pygame
from pygame.locals import *
from random import *

from src import SubMenu
from src.Grille import Grille
from src.Grille import Loto_Case
from src import Data as da
from src import UiPygame as ui
from src.LTO.ia_loto import IA_Loto
from src.UiPygame import Title

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
        self.tab_IA = [IA_Loto(self)]
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
            if(not(self.jeu.containsNbInBoulesSorties(i.getNumber()))):
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

class Menu_LotoChoose(SubMenu.Menu_G):
    "Menu pause du Loto"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
            [ui.Bouton(10, frame.get_height()-60, frame.get_width() - 20, 50, 2, (45, 45, 45),
                       "Jouer avec ces grilles", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
             ui.Bouton(50, frame.get_height()-140, frame.get_width() - 120, 50, 2, (45, 45, 45),
                       "Changer de grilles", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)
        self.grilleToDraw1 = Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)
        self.grilleToDraw2 = Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)
        self.generateRandomContenuGrille(self.grilleToDraw1)
        self.generateRandomContenuGrille(self.grilleToDraw2)

    @staticmethod
    def existInList(cont,value):
        for j in cont:
            if(j == value):
                return True
        return False
    @staticmethod
    def generateRandomContenuGrille(grille):
        cont = [randint(1, 90)]
        for i in range(14):
            val = randint(1,90)
            while Menu_LotoChoose.existInList(cont, val):
                val = randint(1,90)
            cont.append(val)
        grille.fillByListNumeros(cont)

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            # Cas où il appuie sur "Lancer la partie"
            self.data.menus[9].grilleToDraw1 = self.grilleToDraw1
            self.data.menus[9].grilleToDraw2 = self.grilleToDraw2
            self.data.menus[9].partie.addGrilleToMainPlayer(self.grilleToDraw1,self.grilleToDraw2)
            self.data.setEtat("Loto_Play")
            self.data.menus[9].partie.start()
            self.data.menus[9].nbInBoule = 0
        elif self.boutons[1].isCursorInRange():
            # Cas où il appuie sur "Changer de grilles"
            self.generateRandomContenuGrille(self.grilleToDraw1)
            self.generateRandomContenuGrille(self.grilleToDraw2)

    def drawGrille(self,grille,frame,coord):
        surface = pygame.Surface((grille.x2,grille.y2))
        surface.fill((255,255,255))
        grille.draw(surface, (255, 0, 0))
        frame.blit(surface,coord)

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (0, 0, 0), (0, 0, frame.get_width(), frame.get_height()))
        #pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)
        self.drawGrille(self.grilleToDraw1,frame,((frame.get_width()/2)-(self.grilleToDraw1.x2/2),50))
        self.drawGrille(self.grilleToDraw2,frame,((frame.get_width()/2)-(self.grilleToDraw2.x2/2),200))
        #self.grilleToDraw1.draw(frame, (255, 0, 0))

class Menu_LotoPlay(SubMenu.Menu_G):
    "Menu jeu du Loto"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, frame.get_height()-60, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Abandonner", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(10, frame.get_height()-130, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Bingo !", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)
        self.police19 = pygame.font.SysFont("Impact",19)
        self.sizeBoule = round(frame.get_height() / 14)
        self.colorBackground = (0,0,0)
        self.grilleToDraw1 = Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)
        self.grilleToDraw2 = Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)
        self.titre = Title(20,20,frame.get_width()-40,50,2,"Lancement de la partie ...",(12, 12, 251),self.police,(255,255,255))
        self.partie = Loto_Party(frame,data)
        self.data.partie = self.partie
        self.nbInBoule = 0
        self.frame = frame

    def click(self, frame):
            if self.boutons[0].isCursorInRange():
                # Cas où il apuuie sur "Abandon"
                self.data.setEtat("Loto_End")
                self.partie.stop()
                self.nbInBoule = 0
                #self.data.soundSystem.playSound("rire")
                self.data.soundSystem.playMusic("triste")
            elif self.boutons[1].isCursorInRange():
                # Cas où il appuie sur bingo
                self.data.menus[10].asWin = self.partie.isMainPlayerWinner()
                if(not(self.data.menus[10].asWin)):
                    self.data.soundSystem.playMusic("triste")
                self.partie.stop()
                self.nbInBoule = 0
                self.data.setEtat("Loto_End")

    def drawIA(self,frame,ia,x,y):
        surface = pygame.Surface((100,60))
        surface.fill(self.colorBackground)
        if(ia.isWinner()):
            text_on = self.police19.render("Bingo!",True,(255,255,255))
        else:
            text_on = self.police19.render(ia.nom,True,(255,255,255))
        pygame.draw.rect(surface,(12,12,45),(0,35,100,60))
        surface.blit(text_on,(50 - text_on.get_width()/2,35))
        frame.blit(surface,(x,y))

    def drawBouleSortie(self,frame,value):
        surface = pygame.Surface((self.sizeBoule*2,self.sizeBoule*2))
        surface.fill(self.colorBackground)
        pygame.draw.circle(surface,(255,255,255),(self.sizeBoule,self.sizeBoule),self.sizeBoule)
        pygame.draw.circle(surface,(15,255,15),(self.sizeBoule,self.sizeBoule),self.sizeBoule-4)
        text_on = self.police.render(value,True,(255,255,255))
        surface.blit(text_on,(self.sizeBoule - text_on.get_width()/2,self.sizeBoule - text_on.get_height()/2))
        frame.blit(surface,(frame.get_width()-130,frame.get_height()-300))

    def drawGrille(self,grille,frame,coord):
        surface = pygame.Surface((grille.x2,grille.y2))
        surface.fill((255,255,255))
        grille.draw(surface, (255, 0, 0))
        frame.blit(surface,coord)

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, self.colorBackground, (0, 0, frame.get_width(), frame.get_height()))
        if(self.nbInBoule>0):
            self.drawBouleSortie(frame,str(self.nbInBoule))
        self.drawGrille(self.grilleToDraw1,frame,(40,90))
        self.drawGrille(self.grilleToDraw2,frame,(40,200))
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)
        self.drawIA(frame,self.partie.tab_IA[0],370,200)
        self.titre.draw(frame)


class Menu_LotoEnd(SubMenu.Menu_G):
    "Menu de fin du Loto"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, frame.get_height()-100, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Retour au menu", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(10, frame.get_height()-160, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Rejouer", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)
        self.policeTitle = pygame.font.SysFont("Impact",80)
        self.titre = Title(20,20,frame.get_width()-40,50,2,"Fin de partie",(12, 12, 251),self.police,(255,255,255))
        self.asWin = False

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            # Cas où il apuuie sur "Lancer la partie"
            self.data.soundSystem.stopMusic("triste")
            self.data.setEtat("main")
        elif self.boutons[1].isCursorInRange():
            # Cas où il apuuie sur "Rejouer"
            self.data.soundSystem.stopMusic("triste")
            self.data.setEtat("Loto_Choose")
            self.data.menus[9].nbInBoule = 0

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (70, 70, 70), (0, 0, frame.get_width(), frame.get_height()))
        #pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        if(not(self.asWin)):
            self.titre.rgb = (0, 0, 0)
            self.titre.text = "Perdu !"
            frame.blit(self.policeTitle.render("Perdu !", True, (255,12,12)),
                       ((frame.get_width()/2)-self.policeTitle.size("Perdu !")[0]/2,frame.get_height()*0.3))
        else:
            self.titre.rgb = (12, 12, 251)
            self.titre.text = "Gagné !"
            frame.blit(self.policeTitle.render("Gagné !", True, (255,255,255)),
                       ((frame.get_width()/2)-self.policeTitle.size("Gagné !")[0]/2,frame.get_height()*0.3))
        self.titre.draw(frame)
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)