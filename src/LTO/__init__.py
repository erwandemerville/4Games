import pygame
from pygame.locals import *

from src import SubMenu
from src.Grille import Grille
from src.Grille import Loto_Case
from src import Data as da
from src import UiPygame as ui
from src.UiPygame import Title


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
        self.grilleToDraw1 = Grille.Grille(10, 3, 30, 120, 330, 210, Loto_Case)

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            # Cas où il apuuie sur "Lancer la partie"
            self.data.setEtat("Loto_Play")

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (70, 70, 70), (0, 0, frame.get_width(), frame.get_height()))
        #pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        frame.blit(self.police.render("Pause", True, (255,255,255)), (285, 120))
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)
        self.grilleToDraw1.draw(frame, (255, 0, 0))

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
        self.sizeBoule = round(frame.get_height() / 14)

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            # Cas où il apuuie sur "Abandon"
            self.data.setEtat("Loto_End")
            #self.data.soundSystem.playSound("rire")
            self.data.soundSystem.playMusic("triste")
        elif self.boutons[1].isCursorInRange():
            # Cas où il appuie sur bingo
            print("Bingo!")

    def drawBouleSortie(self,frame,value):
        surface = pygame.Surface((self.sizeBoule*2,self.sizeBoule*2))
        pygame.draw.circle(surface,(15,255,15),(self.sizeBoule,self.sizeBoule),self.sizeBoule)
        frame.blit(self.policeTitle.render(value, True, (255,12,12),
        (self.sizeBoule-self.policeTitle.size(value)[0]/2,frame.get_height()*0.3)),
                   ())
        frame.blit(surface,(150,150))

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (0, 95, 70), (0, 0, frame.get_width(), frame.get_height()),self.sizeBoule)
        self.drawBouleSortie(frame,"4")
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)


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

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            # Cas où il apuuie sur "Lancer la partie"
            self.data.soundSystem.stopMusic("triste")
            self.data.setEtat("main")
        elif self.boutons[1].isCursorInRange():
            # Cas où il apuuie sur "Rejouer"
            self.data.soundSystem.stopMusic("triste")
            self.data.setEtat("Loto_Choose")

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (70, 70, 70), (0, 0, frame.get_width(), frame.get_height()))
        #pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        if(True):
            self.titre.rgb = (0, 0, 0)
            frame.blit(self.policeTitle.render("Perdu !", True, (255,12,12)),
                       ((frame.get_width()/2)-self.policeTitle.size("Perdu !")[0]/2,frame.get_height()*0.3))
        else:
            self.titre.rgb = (12, 12, 251)
            frame.blit(self.policeTitle.render("Gagné !", True, (255,255,255)),
                       ((frame.get_width()/2)-self.policeTitle.size("Gagné !")[0]/2,frame.get_height()*0.3))
        self.titre.draw(frame)
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)