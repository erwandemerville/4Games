# Crée par BendoTv pour le projet d'algorithmique et développement
# Réalisé en Décembre 2019
import pygame
from pygame.locals import *

import UiPygame as ui
import SubMenu
from Grille import Grille, Loto_Case
from UiPygame import Title

# Classe du menu principal du profil
class Menu_ProfilM(SubMenu.Menu_G):
    "Menu principal du profil"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, frame.get_height()-170, frame.get_width()/2 - 20, 50, 2, (45, 45, 45),
                                    "Se connecter", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(10+frame.get_width()/2, frame.get_height()-170, frame.get_width()/2 - 20, 50, 2, (45, 45, 45),
                                    "S'inscrire", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(50, frame.get_height()-60, frame.get_width()-100, 50, 2, (45, 45, 45),
                                    "Retour au menu", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(100, frame.get_height()-150, frame.get_width()-200, 50, 2, (45, 45, 45),
                                    "Se déconnecter", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police = pygame.font.SysFont("Impact",65)
        self.police27 = pygame.font.SysFont("Impact", 27)
        self.titre = Title(20, 20, frame.get_width() - 40, 50, 2, "Profil", (12, 12, 251), self.police27,
                           (255, 255, 255))
    # Appelée lorsque le joueur clique
    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            self.data.setEtat("Profil_Co")
            self.data.soundSystem.playSound("Clique")
        elif self.boutons[1].isCursorInRange():
            if self.isConnected():
                self.deconnecte()
            else:
                self.data.setEtat("Profil_Ins")
            self.data.soundSystem.playSound("Clique")
        elif self.boutons[2].isCursorInRange():
            self.data.setEtat("main")
            self.data.soundSystem.playSound("Clique")
        elif self.boutons[3].isCursorInRange():
            if self.isConnected():
                self.deconnecte()
                self.data.soundSystem.playSound("Clique")

    # Détermine si un joueur est connecté
    def isConnected(self):
        return self.data.profilHandler.getcurrentProfil() != None
    # Appelée pour déconnecter le joueur courant
    def deconnecte(self):
        self.data.profilHandler.deconnect()
    # Retourne le pseudo du joueur courant
    def getPseudo(self):
        return self.data.profilHandler.getcurrentProfil()._getPseudo()
    # Retourne le nombre de crédits
    def getCredits(self):
        return self.data.profilHandler.getcurrentProfil()._getCredits()

    # Appelée pour dessiner la fenetre
    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        if self.isConnected():
            self.titre.draw(frame)
            frame.blit(self.police.render(self.getPseudo(), True, (255, 255, 255)),
                       ((frame.get_width() / 2) - self.police.size(self.getPseudo())[0] / 2,
                        frame.get_height() * 0.2))
            frame.blit(self.police27.render((str(self.getCredits())+" jetons"), True, (255, 255, 255)),
                       ((frame.get_width() / 2) - self.police27.size((str(self.getCredits())+" jetons"))[0] / 2,
                        frame.get_height() * 0.4))
            self.boutons[3].draw(frame)
        else:
            self.boutons[0].draw(frame)
            self.boutons[1].draw(frame)
            frame.blit(self.police.render("Aucun profil connecté !", True, (255, 255, 255)),
                       ((frame.get_width() / 2) - self.police.size("Aucun profil connecté !")[0] / 2, frame.get_height() * 0.3))
        self.boutons[2].draw(frame)

# Classe pour le menu d'inscription
class Menu_ProfilIns(SubMenu.Menu_G):
    "Menu inscription du profil"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(50, frame.get_height()-60, frame.get_width()-100, 50, 2, (45, 45, 45),
                                    "Retour au menu", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(50, frame.get_height() - 120, frame.get_width() - 100, 50, 2, (45, 45, 45),
                                    "Inscription", (170, 170, 170), pygame.font.SysFont("Impact", 27),
                                    (255, 255, 255))])
        self.textBoxes = [ui.TextBox(50, 100, 540, 60, 2, placeholder="Pseudo"),
                          ui.TextBox(50, 200, 540, 60, 2, placeholder="MDP", hideChar='*')]
        self.police27 = pygame.font.SysFont("Impact", 27)
        self.titres = [Title(20, 20, frame.get_width() - 40, 50, 2, "S'inscrire", (12, 12, 251), self.police27,
                           (255, 255, 255))]

    # Appelée lorsque le joueur clique
    def click(self, frame):
        if self.boutons[0].isCursorInRange(): # Si le bouton "Retour au menu" est pressé
            self.data.setEtat("Profil_Main") # Retour au menu
            self.data.soundSystem.playSound("Clique")
            # Reset des titres
            del self.titres
            self.titres = [Title(20, 20, frame.get_width() - 40, 50, 2, "S'inscrire", (12, 12, 251), self.police27,
                               (255, 255, 255))]
            # Reset des boutons dans le cas où ils auraient été modifiés
            del self.boutons
            self.boutons = [ui.Bouton(50, frame.get_height()-60, frame.get_width()-100, 50, 2, (45, 45, 45),
                            "Retour au menu", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                            ui.Bouton(50, frame.get_height() - 120, frame.get_width() - 100, 50, 2, (45, 45, 45),
                            "Inscription", (170, 170, 170), pygame.font.SysFont("Impact", 27),
                            (255, 255, 255))]
            # Reset des Textbox
            del self.textBoxes
            self.textBoxes = [ui.TextBox(50, 100, 540, 60, 2, placeholder="Pseudo"),
                              ui.TextBox(50, 200, 540, 60, 2, placeholder="MDP", hideChar='*')]
        elif self.boutons[1].isCursorInRange(): # Si le bouton "Inscription" est pressé
            texts = (self.textBoxes[0].getText(), self.textBoxes[1].getText()) # Récupération du pseudo et Mot de passe
            if texts[0] == "" or texts[0] == None or not texts[0]: # Si le Pseudo est vide
                # Ajout d'un titre demandant d'entrer le Pseudo
                del self.titres
                self.titres = [Title(20, 20, frame.get_width() - 40, 50, 2, "S'inscrire", (12, 12, 251), self.police27,
                                   (255, 255, 255)),
                               Title(20, 280, frame.get_width() - 40, 50, 0, "Veuillez entrer un Pseudo", None,
                                     pygame.font.SysFont('Impact',18), (235, 20, 20))]
            elif self.data.profilHandler.createProfil(texts[0], texts[1]): # Si l'inscription réussi
                # Ajout d'un titre indiquant que le profil a été crée
                del self.titres
                self.titres = [Title(20, 20, frame.get_width() - 40, 50, 2, "S'inscrire", (12, 12, 251), self.police27,
                                   (255, 255, 255)),
                               Title(20, 280, frame.get_width() - 40, 50, 0, "Le profil a été ajouté", None,
                                     pygame.font.SysFont('Impact',18), (20, 235, 20))]
                self.data.profilHandler.connect(texts[0], texts[1])
                self.boutons = [ui.Bouton(50, frame.get_height()-60, frame.get_width()-100, 50, 2, (45, 45, 45),
                                "Retour au menu", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))]
            else: # Si l'inscription échoue
                # Ajout d'un titre disant que le profil existe déjà
                del self.titres
                self.titres = [Title(20, 20, frame.get_width() - 40, 50, 2, "S'inscrire", (12, 12, 251), self.police27,
                                       (255, 255, 255)),
                                   Title(20, 280, frame.get_width() - 40, 50, 0, "Le profil existe déja! Veuillez chosir un autre Pseudo", None,
                                         pygame.font.SysFont('Impact',18), (235, 20, 20))]
            self.data.soundSystem.playSound("Clique")
        else:
            for i in self.textBoxes:
                i.click()

    # Fonction indiquant si le menu possède une TextBox.
    def haveTextBox(self):
        return True

    # Fonction permettant d"ecrire dans une TextBox contenue dans le menu.
    def keyDown(self, keys):
        for p in self.textBoxes:
            p.keyDown(keys[K_a:K_z+1] + keys[K_0:K_COLON] + keys[K_KP0:K_KP_PERIOD] + (keys[59], keys[K_LSHIFT], keys[K_RSHIFT], keys[K_BACKSPACE]))

    def keyUp(self):
        for p in self.textBoxes:
            p.keyUp()

    # Affichage du menu
    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        for t in self.boutons:
            t.draw(frame)
        for t in self.titres:
            t.draw(frame)
        self.textBoxes[0].draw(frame)
        self.textBoxes[1].draw(frame)

# Classe pour le menu de connexion du profil
class Menu_ProfilCo(SubMenu.Menu_G):
    "Menu connexion du profil"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(50, frame.get_height()-60, frame.get_width()-100, 50, 2, (45, 45, 45),
                                    "Retour au menu", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(50, frame.get_height() - 120, frame.get_width() - 100, 50, 2, (45, 45, 45),
                                    "Connexion", (170, 170, 170), pygame.font.SysFont("Impact", 27),
                                    (255, 255, 255))
                          ])
        self.textBoxes = [ui.TextBox(50, 100, 540, 60, 2, placeholder="Pseudo"),
                          ui.TextBox(50, 200, 540, 60, 2, placeholder="MDP", hideChar='*')]
        self.police27 = pygame.font.SysFont("Impact", 27)
        self.titres = [Title(20, 20, frame.get_width() - 40, 50, 2, "Se connecter", (12, 12, 251), self.police27,
                           (255, 255, 255))]
    # Fonction appelée lorsque le joueur clique
    def click(self, frame):
        if self.boutons[0].isCursorInRange(): # Si le bouton "Retour au menu" est pressé
            self.data.setEtat("Profil_Main")
            self.data.soundSystem.playSound("Clique")
            # Reset des titres
            del self.titres
            self.titres = [Title(20, 20, frame.get_width() - 40, 50, 2, "Se connecter", (12, 12, 251), self.police27,
                               (255, 255, 255))]
            # Reset des Textbox
            del self.textBoxes
            self.textBoxes = [ui.TextBox(50, 100, 540, 60, 2, placeholder="Pseudo"),
                              ui.TextBox(50, 200, 540, 60, 2, placeholder="MDP", hideChar='*')]
        elif self.boutons[1].isCursorInRange(): # Si le bouton "Se connecter" est pressé
            texts = (self.textBoxes[0].getText(), self.textBoxes[1].getText()) # Récupération du pseudo et Mot de passe
            if texts[0] == "" or texts[0] == None or not texts[0]: # Si le Pseudo est vide
                # Ajout d'un titre demandant d'entrer le Pseudo
                del self.titres
                self.titres = [Title(20, 20, frame.get_width() - 40, 50, 2, "Se connecter", (12, 12, 251), self.police27,
                                   (255, 255, 255)),
                               Title(20, 280, frame.get_width() - 40, 50, 0, "Veuillez entrer un Pseudo", None,
                                     pygame.font.SysFont('Impact',18), (235, 20, 20))]
            elif self.data.profilHandler.connect(texts[0], texts[1]): # Si l'inscription réussi
                self.data.profilHandler.connect(texts[0], texts[1])
                self.data.setEtat("Profil_Main")
            else:
                if not self.data.profilHandler.ProfilExist(texts[0]):
                    self.titres = [Title(20, 20, frame.get_width() - 40, 50, 2, "Se connecter", (12, 12, 251), self.police27,
                                       (255, 255, 255)),
                                   Title(20, 280, frame.get_width() - 40, 50, 0, "Le profil demandé n'existe pas", None,
                                         pygame.font.SysFont('Impact',18), (235, 20, 20))]
                else:
                    self.titres = [Title(20, 20, frame.get_width() - 40, 50, 2, "Se connecter", (12, 12, 251), self.police27,
                                       (255, 255, 255)),
                                   Title(20, 280, frame.get_width() - 40, 50, 0, "Pseudo où Mot de passe Incorrect.", None,
                                         pygame.font.SysFont('Impact',18), (235, 20, 20))]

            self.data.soundSystem.playSound("Clique")
        else:
            for i in self.textBoxes:
                i.click()

    # Fonction indiquant si le menu possède une TextBox.
    def haveTextBox(self):
        return True

    # Fonction permettant d"ecrire dans une TextBox contenue dans le menu.
    def keyDown(self, keys):
        for p in self.textBoxes:
            p.keyDown(keys[K_a:K_z+1] + keys[K_0:K_COLON] + keys[K_KP0:K_KP_PERIOD] + (keys[59], keys[K_LSHIFT], keys[K_RSHIFT], keys[K_BACKSPACE]))

    def keyUp(self):
        for p in self.textBoxes:
            p.keyUp()

    # Affichage du menu
    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        for t in self.boutons:
            t.draw(frame)
        for t in self.titres:
            t.draw(frame)
        self.textBoxes[0].draw(frame)
        self.textBoxes[1].draw(frame)
