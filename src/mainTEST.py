import pygame
from pygame.locals import *
import Data as da
import UiPygame as ui
import SubMenu as sb
import os,sys,time
from BatailleNavale import testJeuCmd

#Corriger bug du bouton Quitter

pygame.init()
frame = pygame.display.set_mode((640,480))

data = da.Data(frame)
da.Data.init(frame, data)

da.Data.menus[0].draw(frame)

pygame.display.flip()

t = time.time()

test = testJeuCmd.testBN()

while(not(data.fin)):
    for event in pygame.event.get():
        if(event.type == QUIT):
                # En cas d'appui sur la croix
            data.fin = True
        elif(event.type == MOUSEBUTTONDOWN):
                # Quand un clic est effectué
            da.Data.menus[data.etat].draw(frame)
            da.Data.menus[data.etat].click(frame)
        elif (event.type == MOUSEMOTION):
                # Quand la souris est en mouvement
            if (data.etat == 4):
                pos = pygame.mouse.get_pos()
                data.partie.grille_jeu.hoverCase(pos[0], pos[1])
                data.partie.draw(frame, da.Data.menus[data.etat])
            else:
                da.Data.menus[data.etat].draw(frame)
        elif event.type == pygame.KEYDOWN:
            if (data.etat == 4):
                keys = pygame.key.get_pressed()
                if(keys[K_LSHIFT]==1 and keys[K_g]==1):
                    data.setEtat(5)
                    data.partie.effacer_sauvegarde()
                    data.partie.victoire(data)
                    da.Data.menus[5].draw(frame)
                data.partie.keyPressed(keys[K_1:K_COLON]+keys[K_KP1:K_KP_PERIOD]+(keys[K_BACKSPACE],0), data)
                data.partie.draw(frame, da.Data.menus[data.etat])
            elif(data.etat == 0):
                keys = pygame.key.get_pressed()
                if(keys[K_LSHIFT]==1 and keys[K_s]==1):
                    print("Sound_active = ",data.sound_active," | Music active = ",data.music_active)
                da.Data.menus[data.etat].draw(frame)
            else:
                da.Data.menus[data.etat].draw(frame)

    if time.time()-t > 1:
        if data.partie != None:
            if (data.etat == 4):
                data.partie.timerTick()
                data.partie.draw(frame, da.Data.menus[4])
        t = t+1
    if(not(data.particules.isEmpty())):
        data.particules.tick()
        data.particules.draw(frame)

    pygame.display.flip()

pygame.quit()
