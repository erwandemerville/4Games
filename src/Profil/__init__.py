import os
from random import randint

import pygame

import LTO
import UiPygame as ui
import SubMenu
from Grille import Grille, Loto_Case
from UiPygame import Title

class Menu_ProfilM(SubMenu.Menu_G):
    "Menu principal du profil"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, frame.get_height()-60, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Abandonner", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(10, frame.get_height()-120, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Bingo !", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(50, frame.get_height()-185, 40, 40, 2, (45, 45, 45),
                                    "<", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(280, frame.get_height()-185, 40, 40, 2, (45, 45, 45),
                                    ">", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])

    def click(self, frame):
        pass


class Menu_ProfilIns(SubMenu.Menu_G):
    "Menu inscription du profil"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, frame.get_height()-60, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Abandonner", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(10, frame.get_height()-120, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Bingo !", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(50, frame.get_height()-185, 40, 40, 2, (45, 45, 45),
                                    "<", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(280, frame.get_height()-185, 40, 40, 2, (45, 45, 45),
                                    ">", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
    def click(self, frame):
        pass


class Menu_ProfilCo(SubMenu.Menu_G):
    "Menu connexion du profil"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, frame.get_height()-60, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Abandonner", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(10, frame.get_height()-120, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Bingo !", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(50, frame.get_height()-185, 40, 40, 2, (45, 45, 45),
                                    "<", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(280, frame.get_height()-185, 40, 40, 2, (45, 45, 45),
                                    ">", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
    def click(self, frame):
        pass