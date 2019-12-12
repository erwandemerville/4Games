import pygame
from pygame.locals import *
import Sudoku, LTO
import BatailleNavale
from abc import ABC, abstractmethod
from SubMenu import TitleManager
import Data as da
import configparser as cp
import Poker.Jeu as pk
import time

class Menu_G(ABC):
    "Classe générale représentant un menu"

    # Contructeur de la classe de base des Menu
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # data : instance de la classe Data
    # boutons : tableaux de boutons contenant les boutons du menu
    #
    def __init__(self,data,boutons):
        # Constructeur prenant la classe Data définie dans le main.py

        self.data = data
        self.boutons = boutons

    # Fonction click
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # frame : instance de la fenêtre
    #
    # Fonction gérant les clicks de souris
    #
    @abstractmethod
    def click(self, frame):
        #indique comment le menu doit réagir quand un clic de souris est effectué
        pass

    # Fonction hover
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # frame : instance de la fenêtre
    #
    # Fonction gérant les movements de souris
    #
    def hover(self, frame):
        for b in self.boutons:
            b.update(frame)

    # Fonction haveTextBox
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction indiquant si le menu possède une TextBox. Sert pour le main.
    #
    def haveTextBox(self):
        return False

    # Fonction keyDown
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # keys : tableau contenant les états de toutes les touches du clavier.
    #
    # Fonction permettant d'ecrire dans une TextBox contenue dans le menu. Sert pour le main.
    #
    def keyDown(self, keys):
        pass

    # Fonction keyUp
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction permettant d'indiquer que plus aucune touche n'est pressée. Sert pour le main.
    #
    def keyUp(self):
        pass

    # Fonction draw_Profil
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # frame : instance de la fenêtre
    #
    # Fonction permettant de dessiner le profil en haut a gauche de la fenêtre. Ne doit être appellé que
    # dans la fonction draw du menu
    #
    def draw_Profil(self, frame):
        pseudo = self.data.profilHandler.getcurrentProfil() # Recupération du joueur actuellement connecté
        if pseudo != None:
            pseudo = pseudo._getPseudo() # Récupération du pseudo du joueur
            txt = "Profil : " + pseudo
            police = pygame.font.SysFont('Impact',20)
            Twidth = police.size(txt)[0]
            Theight = police.size(txt)[1]
            space = 8
            pygame.draw.rect(frame, (255, 255, 255), (-2, -2, Twidth+(space*2), Theight+(space*2)), 2)
            frame.blit(police.render(txt, True, (255, 255, 255)), (space, space))

    # Fonction draw
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    # frame : instance de la fenêtre
    #
    # Fonction permettant de dessiner le menu
    #
    def draw(self, frame):
        for i in self.boutons:
            i.draw(frame)

        self.draw_Profil(frame)

class Main_Menu(Menu_G):
    "classe représentant le menu principal"

    def __init__(self, data, boutons):
        super().__init__(data,boutons)

    def click(self, frame):
        if self.boutons[0].isCursorInRange() or self.boutons[1].isCursorInRange() or self.boutons[2].isCursorInRange() or self.boutons[3].isCursorInRange() or self.boutons[4].isCursorInRange() or self.boutons[5].isCursorInRange() or self.boutons[6].isCursorInRange(): # Si un bouton est pressé et que ce nest pas le bouton "Quitter"
            self.data.soundSystem.playSound("Clique")
        if self.boutons[0].isCursorInRange(): # Si le bouton "Sudoku" est pressé
            # Lancement du Sudoku
            self.data.partie = Sudoku.PartieG(frame, self.data)
        elif self.boutons[1].isCursorInRange(): # Si le bouton "Loto" est pressé
            # Lancement du Loto
            self.data.setEtat("Loto_Choose")
            self.data.partie = LTO.Loto_Party(frame,self.data)
        elif self.boutons[2].isCursorInRange(): # Si le bouton "Bataille Navale" est pressé
            # Lancement de la Bataille Navale
            self.data.partie = BatailleNavale.GameBN(self.data)
            self.data.setEtat("BN_Place")
            self.data.partie.draw(frame, da.Data.menus[self.data.etat])
        elif self.boutons[3].isCursorInRange(): # Si le bouton "Poker" est pressé
            # Lancement du Poker
            self.data.partie = pk.Jeu()
            self.data.partie.lancerPartie(2)
        elif self.boutons[4].isCursorInRange(): # Si le bouton "Options" est pressé
            # Lancement des options
            da.Data.menus[1].readCfg()
            self.data.setEtat("options")
            self.data.getCurrentMenu().draw(frame)
        elif self.boutons[5].isCursorInRange(): # Si le bouton "Profil" est pressé
            # Lancement du profil
            self.data.setEtat("Profil_Main")
        elif self.boutons[6].isCursorInRange(): # Si le bouton "Classements" est pressé
            # Lancement des classements
            self.data.setEtat("Classements")
            self.data.getCurrentMenu().draw(frame)
        elif self.boutons[7].isCursorInRange(): # Si le bouton "Quitter" est pressé
            # On quitte le jeu
            if self.data.sound_active:
                self.data.soundSystem.playSound("byebye")
                sleepTime = 3
                if sleepTime > 0:
                    time.sleep(sleepTime)
            self.data.fin = True
        pass

    def draw(self, frame):
        frame.blit(self.data.fond, (0,0))
        super().draw(frame)

class Menu_Optn(Menu_G):
    "classe représentant le menu des options"

    def __init__(self,data, boutons,titles):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,boutons)
        self.titles = TitleManager.TitleManager(titles)
        self.link_cfg = "fourgame.cfg"
        self.cfg = cp.ConfigParser()

    def click(self, frame):
        #indique comment le menu doit réagir quand un clic de souris est effectué
        if(self.boutons[0].isCursorInRange()):
            # Bouton sauvegarde enfoncé
            print("Sauvegarde en cours ... ")
            if self.boutons[2].getText() == "Activer la musique":
                self.data.music_active = False
            else:
                self.data.music_active = True
            if self.boutons[3].getText() == "Activer les bruitages":
                self.data.sound_active = False
            else:
                self.data.sound_active = True
            self.writeCfg()
        elif(self.boutons[1].isCursorInRange()):
            # Bouton retour au menu
            self.data.setEtat("main")
            frame.blit(self.data.fond, (0,0))
            self.data.getCurrentMenu().draw(frame)
        elif(self.boutons[2].isCursorInRange()):
            # Bouton on/off musique
            if(self.boutons[2].getText() == "Activer la musique"):
                self.boutons[2].setText("Désactiver la musique")
            else:
                self.boutons[2].setText("Activer la musique")

            self.draw(frame)
        elif(self.boutons[3].isCursorInRange()):
            # Bouton on/off bruitages
            if(self.boutons[3].getText() == "Activer les bruitages"):
                self.boutons[3].setText("Désactiver les bruitages")
            else:
                self.boutons[3].setText("Activer les bruitages")
            self.draw(frame)

    def writeCfg(self):
        section = "Sound"
        isIn = False
        for s in self.cfg.sections():
            if(s == 'Sound'):
                isIn = True
        if(not(isIn)):
            self.cfg.add_section(section)
        self.cfg.set(section,"music",str(self.data.music_active))
        self.cfg.set(section,"sound",str(self.data.sound_active))
        self.cfg.write(open(self.link_cfg,'w'))
    def readCfg(self):
        file = self.cfg.read(self.link_cfg)
        if(file == []):
            self.writeCfg()
            file = self.cfg.read(self.link_cfg)
        self.data.setMusic(self.cfg.getboolean("Sound","music"))
        self.data.setSound(self.cfg.getboolean("Sound","sound"))
        if(self.data.music_active):
            self.boutons[2].setText("Désactiver la musique")
        else:
            self.boutons[2].setText("Activer la musique")

        if(self.data.sound_active):
            self.boutons[3].setText("Désactiver les bruitages")
        else:
            self.boutons[3].setText("Activer les bruitages")

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))

        self.titles.draw(frame)
        super().draw(frame)

class Menu_Classements(Menu_G):
    "classe représentant le menu montrant les classements"

    def __init__(self, data, boutons):
        super().__init__(data,boutons)
        self.current_Classement = 0

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            self.current_Classement = 0
        elif self.boutons[1].isCursorInRange():
            self.current_Classement = 1
        elif self.boutons[2].isCursorInRange():
            self.current_Classement = 2
        elif self.boutons[3].isCursorInRange():
            self.current_Classement = 3
        elif self.boutons[4].isCursorInRange():
            self.data.setEtat("main")
            self.data.getCurrentMenu().draw(frame)
        else:
            return 0

        self.draw(frame)

    def draw(self, frame):
        frame.blit(self.data.fond, (0,0))
        for i in self.boutons:
            i.draw(frame)
        if self.data.classements[self.current_Classement] != None:
            self.data.classements[self.current_Classement].draw(frame, 0, 8, (20, 120, frame.get_width() - 40, frame.get_height() - 220))
        else:
            police = pygame.font.SysFont("Impact",30)
            frame.blit(police.render("Non Disponible", True, (255,255,255)), (frame.get_width()/2 - police.size("Non Disponible")[0]/2, frame.get_height()/2-15))
        pass

class Menu_SavedGrille(Menu_G):
    "classe représentant le menu qui s'affiche pour demander si l'on utilise la grille sauvegardée"

    def __init__(self,data, boutons, titles):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,boutons)
        self.titles = TitleManager.TitleManager(titles)

    def click(self, frame):
        if (self.boutons[0].isCursorInRange()):
            self.data.partie.charger_grille()
            self.data.setEtat("Sudoku_Game")
            self.data.partie.draw(frame)
        elif (self.boutons[1].isCursorInRange()):
            self.data.setEtat("Sudoku_Diff")

        self.data.getCurrentMenu().draw(frame)
        pass

    def draw(self, frame):
        frame.fill((0,0,0))
        for i in self.boutons:
            i.draw(frame)
        self.titles.draw(frame)
        self.draw_Profil(frame)

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
            self.data.setEtat("Sudoku_Game")

            # L'état de la partie passe à "En cours"
            self.data.partie.etat_partie = 1
            self.data.partie.draw(frame)
            self.data.getCurrentMenu().draw(frame)
        pass

    def draw(self, frame):
        frame.fill((0,0,0))
        for i in self.boutons:
            i.draw(frame)
        self.titles.draw(frame)
        self.draw_Profil(frame)

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
            self.data.setEtat("Sudoku_Pause")

    def draw(self, frame):
        pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        frame.blit(self.police.render("Difficulté : ", True, (255,255,255)), (553 - self.police.size("Difficulté : ")[0]/2, 40))
        temp = self.data.partie.getDiffStr()
        frame.blit(self.police.render(temp, True, (255,255,255)), (553 - self.police.size(temp)[0]/2, 70))
        frame.blit(self.police.render("Temps : ", True, (255,255,255)), (553 - self.police.size("Temps : ")[0]/2, 120))
        temp = self.data.partie.getStringTime()
        frame.blit(self.police.render(temp, True, (255,255,255)), (553 - self.police.size(temp)[0]/2, 150))
        frame.blit(self.police.render("Nombre d'erreurs : ", True, (255,255,255)), (553 - self.police.size("Nombre d'erreurs : ")[0]/2, 200))
        temp = str(self.data.partie.getNbErreurs())
        frame.blit(self.police.render(temp, True, (255,255,255)), (553 - self.police.size(temp)[0]/2, 230))
        for i in self.boutons:
            i.draw(frame)

class Menu_SudokuEnd(Menu_G):
    "Menu s'affichant quand on gagne la partie de sudoku"

    def __init__(self,data, boutons):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,boutons)
        self.police = pygame.font.SysFont('Impact',25)
        self.police20 = pygame.font.SysFont('Impact',20)

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            self.data.setEtat("Sudoku_Game")
            self.data.partie.creerGrille(self.data.partie.getDiff())
            self.data.partie.draw(frame)
            self.data.particules.clear()
        elif self.boutons[1].isCursorInRange():
            self.data.setEtat("main")
            frame.blit(self.data.fond, (0,0))
            self.data.getCurrentMenu().draw(frame)
            self.data.particules.clear()

    def draw(self, frame):
        frame.fill((0,0,0))
        frame.blit(self.police.render("Partie Terminée", True, (255,255,255)), (230, 120))
        frame.blit(self.police20.render("Grille niveau " + self.data.partie.getDiffStr() + " terminée en " + self.data.partie.getStringTime(), True, (255,255,255)), (160, 150))
        for i in self.boutons:
            i.draw(frame)

class Menu_SudokuP(Menu_G):
    "Menu pause du Sudoku"

    def __init__(self,data, boutons):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,boutons)
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            self.data.setEtat("Sudoku_Game")
            self.data.partie.draw(frame, self.data.getCurrentMenu())
        elif (self.boutons[1].isCursorInRange() or self.boutons[2].isCursorInRange()):

            if self.boutons[1].isCursorInRange():
                self.data.partie.sauvegarder_grille()

            frame.blit(self.data.fond, (0, 0))
            self.data.setEtat("main")
            self.data.getCurrentMenu().draw(frame)

    def draw(self, frame):
        pygame.draw.rect(frame, (70, 70, 70), (150, 120, frame.get_width()-300, 270))

        frame.blit(self.police.render("Pause", True, (255,255,255)), (285, 120))
        for i in self.boutons:
            i.draw(frame)
