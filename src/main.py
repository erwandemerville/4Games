from tkinter import *
import pygame
from pygame.locals import *
import Sudoku
import UiPygame as ui
       
pygame.init()
frame = pygame.display.set_mode((640,480))

fond = pygame.image.load("assets/background_menu.jpg").convert()
frame.blit(fond, (0,0))

police = pygame.font.SysFont('Impact',25)
b_s = ui.Bouton(frame,30,30,150,50,(180,180,180),"Sudoku",(255,255,255),police)
b_l = ui.Bouton(frame,30,100,150,50,(180,180,180),"Loto",(255,255,255),police)
b_bn = ui.Bouton(frame,30,160,150,50,(180,180,180),"Bataille navale",(255,255,255),police)
b_p = ui.Bouton(frame,30,220,150,50,(180,180,180),"Poker",(255,255,255),police)

b_o = ui.Bouton(frame,300,160,150,50,(180,180,180),"Options",(255,255,255),police)
b_p = ui.Bouton(frame,300,220,150,50,(180,180,180),"Profil",(255,255,255),police)

pygame.display.flip()

fin = False
while(not(fin)):
    for event in pygame.event.get():
        if(event.type == QUIT):
            fin = True
        if(event.type == MOUSEBUTTONDOWN):
            if(b_s.isCursorInRange()):
                Sudoku.Partie()
            elif(b_l.isCursorInRange()):
                print("Lancement du loto")
            elif(b_bn.isCursorInRange()):
                print("Lancement de la bataille navale")
            elif(b_p.isCursorInRange()):
                print("Lancement du poker")
            elif(b_o.isCursorInRange()):
                print("Lancement des options")
            elif(b_p.isCursorInRange()):
                print("Lancement du profil")
            
pygame.quit()
