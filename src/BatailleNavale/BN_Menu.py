import pygame
import SubMenu
import Data as da
import BatailleNavale

class BN_Place_Boats(SubMenu.Menu_G):
    "Menu de placement des bateau de la bataille Navale"

    def __init__(self, data, boutons):
        super().__init__(data, boutons)

    def click(self, frame):
        if pygame.mouse.get_pressed()[2]:
            self.data.partie.TournerBateau()
        elif pygame.mouse.get_pressed()[0]:
            if self.data.partie.placeData[6] == -1:
                self.data.partie.selectBateau()
            else:
                self.data.partie.placeBateau()

        if self.boutons[0].isCursorInRange():
            if self.data.partie.allBoatsPlaced():
                self.data.partie.createIA()
                self.data.partie.draw(frame, da.Data.menus[12])
                self.data.setEtat("BN_Play")
            else:
                print("Vous devez placer tous les bateaux avant de pouvoir commencer.")
        else:
            self.data.partie.draw(frame, da.Data.menus[11])


class BN_Jouer(SubMenu.Menu_G):
    "Menu de jeu de la bataille Navale"

    def __init__(self, data, boutons):
        super().__init__(data, boutons)

    def click(self, frame):
        if self.data.partie.currentPlayData[0] == 1:
            if self.boutons[0].isCursorInRange():
                self.data.partie.currentPlayData[1] = 2 if self.data.partie.currentPlayData[1] == 1 else 1
                self.data.partie.invert_Grilles_Pos()
                self.data.partie.placeData[5] = 2 if self.data.partie.placeData[5] == 1 else 1
                self.boutons[0].text = "voir votre grille" if self.data.partie.currentPlayData[1] == 2 else "voir la grille de l'adversaire"
                self.boutons[1].rgb_when_change = None if self.data.partie.currentPlayData[1] == self.data.partie.currentPlayData[0] else (45, 45, 45)
                self.data.partie.draw(frame)
            elif self.boutons[1].isCursorInRange() and self.data.partie.currentPlayData[1] != self.data.partie.currentPlayData[0]:
                self.data.partie.playTir()
                self.data.partie.draw(frame)
            else:
                pos = pygame.mouse.get_pos()
                self.data.partie.getGrille().selectCase(pos[0], pos[1])

class BN_GGAGNER(SubMenu.Menu_G):
    "Menu de victoire/défaite de la bataille navale."

    def __init__(self, data, boutons):
        super().__init__(data, boutons)
        self.win = True

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            del self.data.partie
            self.data.partie = BatailleNavale.GameBN(self.data)
            self.data.setEtat("BN_Place")
            self.data.partie.draw(frame)
            self.data.particules.clear()
        elif self.boutons[1].isCursorInRange():
            del self.data.partie
            self.data.partie = None
            self.data.setEtat("main")
            self.data.getCurrentMenu().draw(frame)
            self.data.particules.clear()
        pass

    def setWin(self, win):
        self.win = win

    def draw(self, frame):
        frame.fill((10,10,10))

        police20 = pygame.font.SysFont('Impact', 20)
        police = pygame.font.SysFont('Impact', 30)
        if self.data.partie.winner == 1:
            frame.blit(police.render("Gagné!", True, (25, 245, 25)), ((frame.get_width() - police.size("Gagné!")[0])/2, 170))
        else:
            frame.blit(police.render("Perdu!", True, (245, 25, 25)), ((frame.get_width() - police.size("Perdu!")[0])/2, 170))
        l = "Partie gagnée par le joueur " + str(self.data.partie.winner-1) + "avec une précision de" + str(self.data.partie.precision(self.data.partie.winner-1)) + "%."
        frame.blit(police20.render(l, True, (255, 255, 255)), ((frame.get_width() - police.size(l)[0])/2, 220))
        super().draw(frame)
