import pygame
from pygame.locals import *
import Data as da
import os,sys,time

#Corriger bug du bouton Quitter

pygame.init()
FPS = 60.0
mustRedraw = True
frame = pygame.display.set_mode((640,480))

data = da.Data(frame)
da.Data.init(frame, data)

da.Data.menus[0].draw(frame)

pygame.display.flip()

t = time.time()
currentTime = time.time()
lastFrameTime = currentTime

while(not(data.fin)):
    for event in pygame.event.get():
        if(event.type == QUIT):
            # En cas d'appui sur la croix
            data.fin = True
        elif(event.type == MOUSEBUTTONDOWN):
            # Quand un clic est effectué
            data.getCurrentMenu().click(frame)
            data.getCurrentMenu().draw(frame)
            mustRedraw = False
        elif (event.type == MOUSEMOTION):
            # Quand la souris est en mouvement
            if data.etat == 4:
                pos = pygame.mouse.get_pos()
                data.partie.grille_jeu.hoverCase(pos[0], pos[1])
                data.partie.draw(frame, da.Data.menus[data.etat])
            elif data.etat == 11 or data.etat == 12:
                pos = pygame.mouse.get_pos()
                if data.etat == 11 or (data.etat == 12 and data.partie.currentPlayData[0] == 1):
                    data.partie.getGrille().hoverCase(pos[0], pos[1])
                data.partie.draw(frame, data.getCurrentMenu())
            else:
                data.getCurrentMenu().draw(frame)
            mustRedraw = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if (data.etat == 4):
                if(keys[K_LSHIFT]==1 and keys[K_g]==1):
                    data.setEtat("Sudoku_Win")
                    data.partie.effacer_sauvegarde()
                    data.partie.victoire(data)
                    data.getCurrentMenu().draw(frame)
                data.partie.keyPressed(keys[K_1:K_COLON]+keys[K_KP1:K_KP_PERIOD]+(keys[K_BACKSPACE],0), data)
                data.partie.draw(frame, da.Data.menus[data.etat])
                mustRedraw = False
            elif(data.etat == 12):
                if(keys[K_LSHIFT]==1 and keys[K_g]==1):
                    data.setEtat("BN_End")
                    data.partie.victoire(data)
                    data.getCurrentMenu().draw(frame)
                elif(keys[K_LSHIFT]==1 and keys[K_p]==1):
                        data.partie.winner = 2
                        data.partie.defaite(data)
                        data.soundSystem.playMusic("triste")
                        data.setEtat("BN_End")
                        data.getCurrentMenu().draw(frame)
            elif data.getCurrentMenu().haveTextBox():
                data.getCurrentMenu().keyDown(keys)
                data.getCurrentMenu().draw(frame)
                mustRedraw = False
            else:
                da.Data.menus[data.etat].draw(frame)
                mustRedraw = False
        elif event.type == pygame.KEYUP:
            if data.getCurrentMenu().haveTextBox():
                data.getCurrentMenu().keyUp()
    if mustRedraw and data.particules.mustDraw():
        data.getCurrentMenu().draw(frame)
    elif mustRedraw and data.mustDraw():
        data.partie.draw(frame, data.getCurrentMenu())
    if time.time()-t > 1:
        if data.partie != None:
            if data.haveTimerTick():
                data.partie.draw(frame, da.Data.menus[data.etat])
        t = t+1
    data.particules.tick()
    data.particules.draw(frame)
    currentTime = time.time()
    sleepTime = 1./FPS - (currentTime - lastFrameTime)
    lastFrameTime = currentTime + sleepTime
    pygame.display.flip()
    if sleepTime > 0:
        time.sleep(sleepTime)
    mustRedraw = True

pygame.quit()
