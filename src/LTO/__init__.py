import pygame

from src import SubMenu
from src import Data as da
from src import UiPygame as ui

class Menu_LotoChoose(SubMenu.Menu_G):
    "Menu pause du Loto"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
            [ui.Bouton(10, 10, frame.get_width()/4 - 20, 50, 2, (45, 45, 45),
                       "Valider", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            self.data.partie.draw(frame, da.Data.menus[4])
            self.data.setEtat(4)
        elif (self.boutons[1].isCursorInRange() or self.boutons[2].isCursorInRange()):

            if self.boutons[1].isCursorInRange():
                self.data.partie.sauvegarder_grille()

            frame.blit(self.data.fond, (0, 0))
            self.data.setEtat(0)

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (70, 70, 70), (150, 120, frame.get_width()-300, 270))
        #pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        frame.blit(self.police.render("Pause", True, (255,255,255)), (285, 120))
        self.boutons[0].draw(frame)

class Menu_LotoPlay(SubMenu.Menu_G):
    "Menu jeu du Loto"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, 10, frame.get_width()/4 - 20, 50, 2, (45, 45, 45),
                                    "Valider", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)


class Menu_LotoEnd(SubMenu.Menu_G):
    "Menu de fin du Loto"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, 10, frame.get_width()/4 - 20, 50, 2, (45, 45, 45),
                                    "Valider", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)