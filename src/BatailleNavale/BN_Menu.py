import pygame
import SubMenu
import Data as da
import BatailleNavale
import UiPygame as ui

class BN_Place_Boats(SubMenu.Menu_G):
    "Menu de placement des bateau de la bataille Navale"

    # Constructeur
    def __init__(self, data, boutons):
        super().__init__(data, boutons)
        self.titles = []

    # Fonction click
    def click(self, frame):
        if pygame.mouse.get_pressed()[2]: # Si le clic droit de la souris est pressé
            self.data.partie.TournerBateau() # Alors on tourne le bateau
        elif pygame.mouse.get_pressed()[0]: # Sinon, si c'est le clic gauche qui est pressé
            if self.data.partie.placeData[6] == -1: # Si aucun bateau n'est actuellement selectionné
                self.data.partie.selectBateau() # On selection le bateau sur lequel se trouve le curseur
            else:
                self.data.partie.placeBateau() # On place le bateau actuellement selectionné a la position du curseur

        if self.boutons[0].isCursorInRange(): # Si le bouton "Valider" est pressé
            if self.data.partie.allBoatsPlaced(): # On vérifie que tous les bateaux soient placés
                self.data.partie.createIA()                         #
                self.data.partie.draw(frame, da.Data.menus[12])     # Démarrage de la partie
                self.data.setEtat("BN_Play")                        #
            else:
                # On place le titre indiquant que la partie ne peut pas démarrer
                self.titles.append(ui.Title(frame.get_width()/5.5, 60, 400, 50,
                                            text="Vous devez placer tous les bateaux avant de pouvoir commencer.",
                                            rgb=None, police=pygame.font.SysFont('Impact',18), rgb_text=(255, 15, 15)))
        elif self.boutons[1].isCursorInRange(): # Si le bouton "Retour au menu" est pressé
            self.data.setEtat("main") # Retour au menu principal
            self.data.partie = None # Suppression de la partie de la classe Data
            del self.titles  # Suppression du titre indiquant
            self.titles = [] # que la partie ne peut pas démarrer
            del self # Effacement de la partie de la mémoire
        else:
            # Sinon on redessine le menu
            self.data.partie.draw(frame, self.data.getCurrentMenu())

    def draw(self, frame):
        for i in self.boutons:
            i.draw(frame)
        for i in self.titles:
            i.draw(frame)


class BN_Jouer(SubMenu.Menu_G):
    "Menu de jeu de la bataille Navale"

    # Constructeur
    def __init__(self, data, boutons):
        super().__init__(data, boutons)

    # Fonction click
    def click(self, frame):
        if self.data.partie.currentPlayData[0] == 1: # Si c'est au tour du joueur
            if self.boutons[0].isCursorInRange(): # Si le bouton "voir la grille de l'adversaire"/"voir votre grille" est pressé
                self.data.partie.currentPlayData[1] = 2 if self.data.partie.currentPlayData[1] == 1 else 1 # On change de grille a afficher
                self.data.partie.invert_Grilles_Pos() # On inverse les positions des grilles
                self.data.partie.placeData[5] = 2 if self.data.partie.placeData[5] == 1 else 1
                self.boutons[0].text = "voir votre grille" if self.data.partie.currentPlayData[1] == 2 else "voir la grille de l'adversaire" # On change le bouton en fonction de la grille affichée
                self.boutons[1].rgb_when_change = (185, 75, 75) if self.data.partie.currentPlayData[1] == self.data.partie.currentPlayData[0] else (45, 45, 45) # On change la couleur du bouton "Tirer" quand il est marqué comme "hovered" (le curseur de la souris se trouve dessus)
                self.data.partie.draw(frame) # On dessine la partie
            elif self.boutons[1].isCursorInRange() and self.data.partie.currentPlayData[1] != self.data.partie.currentPlayData[0]: # Si le bouton "Tirer" est pressé et que le joueur peut tirer.
                self.data.partie.playTir() # On joue l'animation de tir
                self.data.partie.draw(frame)
            elif self.boutons[2].isCursorInRange(): # Si le bouton "Pause" est pressé
                self.data.setEtat("BN_Pause") # On enclenche la pause
                self.data.getCurrentMenu().draw(frame)
            else:
                pos = pygame.mouse.get_pos()
                self.data.partie.getGrille().selectCase(pos[0], pos[1])

    def draw(self, frame):
        for i in self.boutons:
            i.draw(frame)

class BN_GGAGNER(SubMenu.Menu_G):
    "Menu de victoire/défaite de la bataille navale."

    def __init__(self, data, boutons):
        super().__init__(data, boutons)
        self.win = True # Variable servant a déterminer qui a gagné

    def click(self, frame):
        if self.boutons[0].isCursorInRange(): # Si le bouton "Rejouer" est pressé
            del self.data.partie                                    # Reset de la partie
            self.data.partie = BatailleNavale.GameBN(self.data)     # Reset de la partie
            self.data.setEtat("BN_Place") # On repart au menu de placement des bateaux
            self.data.partie.draw(frame)
            self.data.particules.clear()
            self.data.soundSystem.stopMusic("triste")
        elif self.boutons[1].isCursorInRange(): # Si le bouton "Retour au menu" est pressé
            del self.data.partie                    # Suppression de la partie
            self.data.partie = None                 # Suppression de la partie
            self.data.setEtat("main") # On part vers le menu principal
            self.data.getCurrentMenu().draw(frame)
            self.data.particules.clear()
            self.data.soundSystem.stopMusic("triste")
        pass

    def setWin(self, win):
        self.win = win

    def draw(self, frame):
        frame.fill((10,10,10))

        police15 = pygame.font.SysFont('Impact', 15)
        police = pygame.font.SysFont('Impact', 60)
        if self.data.partie.winner == 1:
            frame.blit(police.render("Gagné!", True, (25, 245, 25)), ((frame.get_width() - police.size("Gagné!")[0])/2, 140))
        else:
            frame.blit(police.render("Perdu!", True, (245, 25, 25)), ((frame.get_width() - police.size("Perdu!")[0])/2, 140))
        l = "Partie gagnée par le joueur " + str(self.data.partie.winner-1) + " avec une précision de " + str(self.data.partie.precision(self.data.partie.winner-1)) + "%."
        frame.blit(police15.render(l, True, (255, 255, 255)), ((frame.get_width())/2 - (police15.size(l)[0])/2, 220))
        for i in self.boutons:
            i.draw(frame)

class BN_Pause(SubMenu.Menu_G):
    "Menu de pause de la bataille navale"

    # Constructeur
    def __init__(self, data, boutons):
        super().__init__(data, boutons)

    # Fonction click
    def click(self, frame):
        if self.boutons[0].isCursorInRange(): # Si le bouton "Reprendre" est pressé
            self.data.setEtat("BN_Play") # Reprise de la partie
            self.data.partie.draw(frame, self.data.getCurrentMenu())
        elif self.boutons[1].isCursorInRange(): # Si le bouton "Quitter" est pressé
            self.data.setEtat("main") # Retour au menu pricipal
            self.data.partie = None  # Suppression de la partie
            del self                 # Suppression de la partie

    def draw(self, frame):
        police = pygame.font.SysFont('Impact',25)
        pygame.draw.rect(frame, (70, 70, 70), (230, 120, 180, 180)) # Dessin du rectangle contenant les boutons
        frame.blit(police.render("Pause", True, (255,255,255)), (285, 120))
        for i in self.boutons:
            i.draw(frame)
