import pygame
from pygame.locals import *

from src import SubMenu
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

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            # Cas où il apuuie sur "Lancer la partie"
            self.data.setEtat("Loto_Play")

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (70, 70, 70), (150, 120, frame.get_width()-300, 270))
        #pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        frame.blit(self.police.render("Pause", True, (255,255,255)), (285, 120))
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)

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

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            # Cas où il apuuie sur "Lancer la partie"
            self.data.setEtat("Loto_End")
        elif self.boutons[1].isCursorInRange():
            # Cas où il appuie sur bingo
            print("Bingo!")

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (0, 95, 70), (200, 120, frame.get_width()-300, 270))
        #pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        frame.blit(self.police.render("Pause", True, (255,255,255)), (285, 120))
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
        self.titre = Title(20,20,frame.get_width()-40,50,2,"Fin de partie",(170, 170, 170),self.police,(255,255,255))

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            # Cas où il apuuie sur "Lancer la partie"
            self.data.setEtat("main")
        elif self.boutons[1].isCursorInRange():
            # Cas où il apuuie sur "Rejouer"
            self.data.setEtat("Loto_Choose")

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (70, 70, 70), (0, 0, frame.get_width(), frame.get_height()))
        #pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        frame.blit(self.police.render("Perdu !", True, (255,255,255)), ((frame.get_width()/2)-27,frame.get_height()*0.3,))
        self.titre.draw(frame)
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)