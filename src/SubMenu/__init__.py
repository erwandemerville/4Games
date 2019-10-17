import pygame
from pygame.locals import *
from abc import ABC, abstractmethod

class Menu_G(ABC):

    def __init__(self,data):
        # Constructeur prenant la classe Data définie dans le main.py

        self.data = data

    @abstractmethod
    def draw(self):
        # Permet d'afficher le menu
        pass


class Menu_Optn(Menu_G):

    def __init__(self,data):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data)

    def draw(self):
        print("héhé")
