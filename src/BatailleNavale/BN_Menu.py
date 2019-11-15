import pygame
import SubMenu

class BN_Place_Boats(SubMenu.Menu_G):
    "Menu de placement des bateau de la bataille Navale"

    def __init__(self, data, boutons):
        super().__init__(data, boutons)

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            self.data.partie.draw(frame, da.Data.menus[4])
            self.data.setEtat("BN_Play")

class BN_Jouer(SubMenu.Menu_G):
    "Menu de jeu de la bataille Navale"

    def __init__(self, data, boutons):
        super().__init__(data, boutons)

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            self.data.partie.draw(frame, da.Data.menus[4])
            pass
