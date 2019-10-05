from tkinter import *
import pygame
from pygame.locals import *
import Sudoku
import UiPygame as ui
import os

pygame.init()
frame = pygame.display.set_mode((640,480))

fond = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "background_menu.jpg")).convert()
frame.blit(fond, (0,0))

#cette variable représente les différents états dans lequel le jeu peux se trouver.
#
# 0 - Menu principal
# 1 - options
# 2 - demande si on reprend la grille du Sudoku
# 3 - Sudoku
# 4 -
#
etat = 0;

police = pygame.font.SysFont('Impact',25)
boutons = [];

def createBoutons(tab):
    tab[:] = []
    tab.append(ui.Bouton(30,30,150,50,(180,180,180)))
    tab.append(ui.Bouton(30,100,150,50,(180,180,180)))
    tab.append(ui.Bouton(30,160,150,50,(180,180,180)))
    tab.append(ui.Bouton(30,220,150,50,(180,180,180)))

    tab.append(ui.Bouton(300,160,150,50,(180,180,180)))
    tab.append(ui.Bouton(300,220,150,50,(180,180,180)))



def drawBoutons(frame, police):
    boutons[0].draw(frame,"Sudoku",(255,255,255),police)
    boutons[1].draw(frame,"Loto",(255,255,255),police)
    boutons[2].draw(frame,"Bataille navale",(255,255,255),police)
    boutons[3].draw(frame,"Poker",(255,255,255),police)
    boutons[4].draw(frame,"Options",(255,255,255),police)
    boutons[5].draw(frame,"Profil",(255,255,255),police)

createBoutons(boutons)
drawBoutons(frame, police)
pygame.display.flip()

fin = False
while(not(fin)):
    for event in pygame.event.get():
        if(event.type == QUIT):
            fin = True
        if(event.type == MOUSEBUTTONDOWN):
            if (etat == 0):
                if(boutons[0].isCursorInRange()):
                    Sudoku.PartieG()
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
            elif (etat == 1):
                if (boutons[0].isCursorInRange()):
                    print("YOLO")
                elif (boutons[1].isCursorInRange()):
                    print("YOLO 2")

pygame.quit()
