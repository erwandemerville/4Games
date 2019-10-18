import pygame
from pygame.locals import *
import Sudoku
from abc import ABC, abstractmethod
from SubMenu import TitleManager
import Data as da

class Menu_G(ABC):
    "Classe générale représentant un menu"

    def __init__(self,data,boutons):
        # Constructeur prenant la classe Data définie dans le main.py

        self.data = data
        self.boutons = boutons

    @abstractmethod
    def click(self, frame):
        #indique comment le menu doit réagir quand un clic de souris est effectué
        pass

    def hover(self, frame):
        for b in self.boutons:
            b.update(frame)

    def draw(self, frame):
        for i in self.boutons:
            i.draw(frame)

        pygame.display.flip()
        pass

class Main_Menu(Menu_G):
    "classe représentant le menu principal"

    def __init__(self, data, boutons):
        super().__init__(data,boutons)

    def click(self, frame):
        if(self.boutons[0].isCursorInRange()):
            self.data.partie = Sudoku.PartieG(frame, self.data)
        elif(self.boutons[1].isCursorInRange()):
            print("Lancement du loto")
        elif(self.boutons[2].isCursorInRange()):
            print("Lancement de la bataille navale")
        elif(self.boutons[3].isCursorInRange()):
            print("Lancement du poker")
        elif(self.boutons[4].isCursorInRange()):
            self.data.setEtat(1)
            da.Data.menus[1].draw(frame)
        elif(self.boutons[5].isCursorInRange()):
            print("Lancement du profil")
        elif(self.boutons[6].isCursorInRange()):
            self.data.fin = True
        pass

class Menu_Optn(Menu_G):
    "classe représentant le menu des options"

    def __init__(self,data, boutons,titles):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,boutons)
        self.titles = TitleManager.TitleManager(titles)

    def click(self, frame):
        #indique comment le menu doit réagir quand un clic de souris est effectué
        if(self.boutons[0].isCursorInRange()):
            # Bouton sauvegarde enfoncé
            print("Sauvegarde en cours ... ")
        elif(self.boutons[1].isCursorInRange()):
            # Bouton retour au menu
            self.data.etat = 0
            frame.blit(self.data.fond, (0,0))
            da.Data.menus[0].draw(frame)
        

    def draw(self, frame):
        #print("héhé")
        frame.blit(self.data.fond,(0,0))
        
        self.titles.draw(frame)
        super().draw(frame)

class Menu_SavedGrille(Menu_G):
    "classe représentant le menu qui s'affiche pour demander si l'on utilise la grille sauvegardée"

    def __init__(self,data, boutons, titles):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,boutons)
        self.titles = TitleManager.TitleManager(titles)

    def click(self, frame):
        if (self.boutons[0].isCursorInRange()):
            self.data.partie.charger_grille()
            self.data.setEtat(4)
            self.data.partie.draw(frame)
        elif (self.boutons[1].isCursorInRange()):
            self.data.setEtat(3)

        da.Data.menus[self.data.etat].draw(frame)
        pass

    def draw(self, frame):
        frame.fill((0,0,0))
        for i in self.boutons:
            i.draw(frame)
        self.titles.draw(frame)
        pygame.display.flip()

class Menu_Diff(Menu_G):
    "classe du menu de difficulté"

    def __init__(self,data, boutons, titles):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,boutons)
        self.titles = TitleManager.TitleManager(titles)

    def click(self, frame):
        if (self.boutons[0].isCursorInRange()):
            self.data.partie.creerGrille(1)
        elif (self.boutons[1].isCursorInRange()):
            self.data.partie.creerGrille(2)
        elif (self.boutons[2].isCursorInRange()):
            self.data.partie.creerGrille(3)

        if(self.boutons[0].isCursorInRange() or self.boutons[1].isCursorInRange() or self.boutons[2].isCursorInRange()):
            self.data.setEtat(4);

            # L'état de la partie passe à "En cours"
            self.data.partie.etat_partie = 1;
            self.data.partie.draw(frame)
            da.Data.menus[4].draw(frame)
        pass

    def draw(self, frame):
        frame.fill((0,0,0))
        for i in self.boutons:
            i.draw(frame)
        self.titles.draw(frame)
        pygame.display.flip()

class Menu_Sudoku(Menu_G):
    "Menu contenant le bouton pause du Sudoku"

    def __init__(self,data, boutons):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,boutons)
        self.police = pygame.font.SysFont('Impact',20)

    def click(self, frame):
        pos = pygame.mouse.get_pos()
        self.data.partie.grille_jeu.selectCase(pos[0], pos[1])
        self.data.partie.draw(frame, self)

        if (self.boutons[0].isCursorInRange()):
            self.data.setEtat(6)

    def draw(self, frame):
        pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        frame.blit(self.police.render("Temps :", True, (255,255,255)), (525, 120))
        frame.blit(self.police.render(self.data.partie.getStringTime(), True, (255,255,255)), (530, 150))
        super().draw(frame)

class Menu_SudokuEnd(Menu_G):
    "Menu s'affichant quand on gagne la partie de sudoku"

    def __init__(self,data, boutons):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,boutons)
        self.police = pygame.font.SysFont('Impact',25)
        self.police20 = pygame.font.SysFont('Impact',20)

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            self.data.setEtat(4)
            self.data.partie.creerGrille(self.data.partie.getDiff())
            self.data.partie.draw(frame)
        elif self.boutons[1].isCursorInRange():
            self.data.setEtat(0)
            frame.blit(self.data.fond, (0,0))
            da.Data.menus[0].draw(frame)

    def draw(self, frame):
        frame.fill((0,0,0))
        frame.blit(self.police.render("Partie Terminée", True, (255,255,255)), (230, 120))
        frame.blit(self.police20.render("Grille niveau " + self.data.partie.getDiffStr() + " terminée en " + self.data.partie.getStringTime(), True, (255,255,255)), (160, 150))
        super().draw(frame)

class Menu_SudokuP(Menu_G):
    "Menu pause du Sudoku"

    def __init__(self,data, boutons):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,boutons)
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
        pygame.draw.rect(frame, (70, 70, 70), (150, 120, frame.get_width()-300, 270))
        
        frame.blit(self.police.render("Pause", True, (255,255,255)), (285, 120))
        for i in self.boutons:
            i.draw(frame)
        pygame.display.flip()
