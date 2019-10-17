import pygame
from pygame.locals import *
import Sudoku
import Data as da
import UiPygame as ui
import SubMenu as sb
import os,sys

try:
    pygame.init()
    frame = pygame.display.set_mode((640,480))

    fond = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "background_menu.jpg")).convert()
    frame.blit(fond, (0,0))

    data = da.Data(frame)
    police = pygame.font.SysFont('Impact',20)
    color_boutons = (180,180,180)
    color_boutons_change = (45,45,45)
    
    boutons = []
    color_f = (255,255,255);width_b = 400;x_btn = (frame.get_width()/2) - (width_b/2);y_btn_start = 160
    boutons.append(ui.Bouton(x_btn,y_btn_start,width_b,50,2,color_boutons_change,"Sudoku",color_boutons,police,color_f))
    boutons.append(ui.Bouton(x_btn,y_btn_start+60,width_b,50,2,color_boutons_change,"Loto",color_boutons,police,color_f))
    boutons.append(ui.Bouton(x_btn,y_btn_start+120,width_b,50,2,color_boutons_change,"Bataille navale",color_boutons,police,color_f))
    boutons.append(ui.Bouton(x_btn,y_btn_start+180,width_b,50,2,color_boutons_change,"Poker",color_boutons,police,color_f))

    boutons.append(ui.Bouton(50,frame.get_height()-60,150,50,2,color_boutons_change,"Options",color_boutons,police,color_f))
    boutons.append(ui.Bouton((frame.get_width()/2)-(150/2),frame.get_height()-60,150,50,2,color_boutons_change,"Profil",color_boutons,police,color_f))
    boutons.append(ui.Bouton(frame.get_width()-200,frame.get_height()-60,150,50,2,color_boutons_change,"Quitter",color_boutons,police,color_f))

    for i in boutons:
        i.draw(frame)

    pygame.display.flip()

    fin = False
    while(not(fin)):
        for event in pygame.event.get():
            if(event.type == QUIT):
                # En cas d'appui sur la croix
                fin = True
            elif(event.type == MOUSEBUTTONDOWN):
                # Quand un clic est effectué
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
                    elif(boutons[6].isCursorInRange()):
                        fin = True
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

                    if(boutons[0].isCursorInRange() or boutons[1].isCursorInRange() or boutons[2].isCursorInRange()):
                        data.setEtat(4);
                
                        # L'état de la partie passe à "En cours"
                        data.partie.etat_partie = 1;
                        data.partie.draw(frame)
                elif (data.etat == 4):
                    pos = pygame.mouse.get_pos()
                    data.partie.grille_jeu.selectCase(pos[0], pos[1])
                    data.partie.draw(frame)
            elif (event.type == MOUSEMOTION):
                # Quand la souris est en mouvement
                if (data.etat == 4):
                    pos = pygame.mouse.get_pos()
                    data.partie.grille_jeu.hoverCase(pos[0], pos[1])
                    data.partie.draw(frame)

                else:
                    for b in boutons:
                        b.update(frame)
                    
except Exception as e:
    pygame.quit()
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print("Type : ",exc_type," dans ",fname," ligne : ",exc_tb.tb_lineno)
    print(e)
pygame.quit()
