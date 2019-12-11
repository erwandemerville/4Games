# Crée par BendoTv pour le projet d'algorithmique et développement
# Réalisé en Décembre 2019
import pygame

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
        # TODO
        return False
    # Appelée pour déconnecter le joueur courant
    def deconnecte(self):
        # TODO
        print("Déconnexion")
    # Retourne le pseudo du joueur courant
    def getPseudo(self):
        # TODO
        return "Jacky32X"
    # Retoune le nombre de crédits
    def getCredits(self):
        # TODO
        return 50

    # Appelée pour dessiner la fenetre
    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (0, 0, 0), (0, 0, frame.get_width(), frame.get_height()))
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
        self.police27 = pygame.font.SysFont("Impact", 27)
        self.titre = Title(20, 20, frame.get_width() - 40, 50, 2, "S'inscrire", (12, 12, 251), self.police27,
                           (255, 255, 255))
    # Appelée lorsque le joueur clique
    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            self.data.setEtat("Profil_Main")
            self.data.soundSystem.playSound("Clique")
        elif self.boutons[1].isCursorInRange():
            # TODO
            print("submit")
            self.data.soundSystem.playSound("Clique")
    # Affichage du menu
    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (0, 0, 0), (0, 0, frame.get_width(), frame.get_height()))
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)
        self.titre.draw(frame)

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
        self.police27 = pygame.font.SysFont("Impact", 27)
        self.titre = Title(20, 20, frame.get_width() - 40, 50, 2, "Se connecter", (12, 12, 251), self.police27,
                           (255, 255, 255))
    # Fonction appelée lorsque le joueur clique
    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            self.data.setEtat("Profil_Main")
            self.data.soundSystem.playSound("Clique")
        elif self.boutons[1].isCursorInRange():
            # TODO
            print("submit")
            self.data.soundSystem.playSound("Clique")
    # fonction appelée pour dessiner la fenetre
    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (0, 0, 0), (0, 0, frame.get_width(), frame.get_height()))
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)
        self.titre.draw(frame)