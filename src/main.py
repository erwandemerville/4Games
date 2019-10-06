import pygame
from pygame.locals import *
import Sudoku
import UiPygame as ui
import os

pygame.init()
frame = pygame.display.set_mode((640,480))

fond = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "background_menu.jpg")).convert()
frame.blit(fond, (0,0))

class Data:

    def __init__(self, frame):
        # Cette variable représente les différents états dans lequel le jeu peut se trouver.
        #
        # 0 - Menu principal
        # 1 - options
        # 2 - demande si on reprend la grille du Sudoku
        # 3 - choix du niveau de difficulté au Sudoku (peut être généralisé si tout les mini-jeux possèdent exactement 3 niveaux de difficulté)
        # 4 - En partie de Sudoku
        # 5 - Gain/Perte de la partie du Sudoku
        #
        self.etat = 0

        # Cette variable représente la partie au cas ou on en aurait besoin.
        self.partie = None;

    # Fonction setEtat(e)
    #
    # e : le nouvel état du jeu
    #
    def setEtat(self, e):
        self.etat = e

data = Data(frame)
police = pygame.font.SysFont('Impact',25)
boutons = [];

def createBoutons(tab):
    tab[:] = []
    tab.append(ui.Bouton(30,30,150,50))
    tab.append(ui.Bouton(30,100,150,50))
    tab.append(ui.Bouton(30,160,150,50))
    tab.append(ui.Bouton(30,220,150,50))

    tab.append(ui.Bouton(300,160,150,50))
    tab.append(ui.Bouton(300,220,150,50))



def drawBoutons(frame, police):
    boutons[0].draw(frame,(180,180,180),"Sudoku",(255,255,255),police)
    boutons[1].draw(frame,(180,180,180),"Loto",(255,255,255),police)
    boutons[2].draw(frame,(180,180,180),"Bataille navale",(255,255,255),police)
    boutons[3].draw(frame,(180,180,180),"Poker",(255,255,255),police)
    boutons[4].draw(frame,(180,180,180),"Options",(255,255,255),police)
    boutons[5].draw(frame,(180,180,180),"Profil",(255,255,255),police)

createBoutons(boutons)
drawBoutons(frame, police)
pygame.display.flip()

fin = False
while(not(fin)):
    for event in pygame.event.get():
        if(event.type == QUIT):
            fin = True
        elif(event.type == MOUSEBUTTONDOWN):
            if (data.etat == 0):
                if(boutons[0].isCursorInRange()):
                    data.partie = Sudoku.PartieG(frame, boutons, data)
                elif(boutons[1].isCursorInRange()):
                    print("Lancement du loto")
                elif(boutons[2].isCursorInRange()):
                    print("Lancement de la bataille navale")
                elif(boutons[3].isCursorInRange()):
                    print("Lancement du poker")
                elif(boutons[4].isCursorInRange()):
                    print("Lancement des options")
                elif(boutons[5].isCursorInRange()):
                    print("Lancement du profil")
            elif (data.etat == 1):
                print("OPTIONS")
            elif (data.etat == 2):
                if (boutons[0].isCursorInRange()):
                    data.partie.charger_grille()
                elif (boutons[1].isCursorInRange()):
                    data.partie.choixniveau_gui(frame, boutons)
            elif (data.etat == 3):
                if (boutons[0].isCursorInRange()):
                    data.partie.creerGrille(1)
                elif (boutons[1].isCursorInRange()):
                    data.partie.creerGrille(2)
                elif (boutons[2].isCursorInRange()):
                    data.partie.creerGrille(3)

                data.setEtat(4);

                # L'état de la partie passe à "En cours"
                data.partie.etat_partie = 1;
                data.partie.draw(frame)
            elif (data.etat == 4):
                pos = pygame.mouse.get_pos()
                data.partie.grille_jeu.selectCase(pos[0], pos[1])
                data.partie.draw(frame)
        elif (event.type == MOUSEMOTION):
            if (data.etat == 4):
                pos = pygame.mouse.get_pos()
                data.partie.grille_jeu.hoverCase(pos[0], pos[1])
                data.partie.draw(frame)

pygame.quit()
