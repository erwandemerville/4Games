import pygame
from pygame.locals import *
import SubMenu as sb
import UiPygame as ui
import os

class Data:

        menus = []
    
        def __init__(self, frame):
            # Cette variable représente les différents états dans lequel le jeu peut se trouver.
            #
            # 0 - Menu principal
            # 1 - options
            # 2 - demande si on reprend la grille du Sudoku
            # 3 - choix du niveau de difficulté au Sudoku (peut être généralisé si tout les mini-jeux possèdent exactement 3 niveaux de difficulté)
            # 4 - En partie de Sudoku
            # 5 - Gain de la partie du Sudoku
            # 6 - Partie de Sudoku en Pause
            #
            self.etat = 0

            # Cette variable représente la partie au cas ou on en aurait besoin.
            self.partie = None;

            # Ces variables permettent d'activer et désactiver le son/musique
            self.sound_active = True;
            self.music_active = True;
            self.fin = False
            self.fond = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "background_menu.jpg")).convert()
            frame.blit(self.fond, (0,0))

        @staticmethod
        def init(frame, data):
            police20 = pygame.font.SysFont('Impact',20)
            police = pygame.font.SysFont('Impact',25)
            color_boutons = (180,180,180)
            color_boutons_change = (45,45,45)
            color_f = (255,255,255);width_b = 400;x_btn = (frame.get_width()/2) - (width_b/2);y_btn_start = 160
            Data.menus.append(sb.Main_Menu(data, [ui.Bouton(x_btn,y_btn_start,width_b,50,2,color_boutons_change,"Sudoku",color_boutons,police,color_f),
                        ui.Bouton(x_btn,y_btn_start+60,width_b,50,2,color_boutons_change,"Loto",color_boutons,police,color_f),
                        ui.Bouton(x_btn,y_btn_start+120,width_b,50,2,color_boutons_change,"Bataille navale",color_boutons,police,color_f),
                        ui.Bouton(x_btn,y_btn_start+180,width_b,50,2,color_boutons_change,"Poker",color_boutons,police,color_f),
                        ui.Bouton(50,frame.get_height()-60,150,50,2,color_boutons_change,"Options",color_boutons,police,color_f),
                        ui.Bouton((frame.get_width()/2)-(150/2),frame.get_height()-60,150,50,2,color_boutons_change,"Profil",color_boutons,police,color_f),
                        ui.Bouton(frame.get_width()-200,frame.get_height()-60,150,50,2,color_boutons_change,"Quitter",color_boutons,police,color_f)]))
           
            Data.menus.append(sb.Menu_Optn(data,
                                           [ui.Bouton(x_btn,y_btn_start+60,width_b,50,2,color_boutons_change,"Loto",color_boutons,police,color_f)] ,
                                           [ui.Title(50,50,(frame.get_width()-100),60,3,"OPTIONS")]

                                           ))

            Data.menus.append(sb.Menu_SavedGrille(data, [ui.Bouton(245, 220, 150, 50,0,(45,45,45),"Oui",(180,180,180),police,(255,255,255)), ui.Bouton(245, 320, 150, 50,0,(45,45,45), "Non",(180,180,180),police,(255,255,255))],
                                                    [ui.Title(75, 100, 500, 100, 2, "Une partie a été sauvegardée, voulez-vous la charger?", (0,0,0,0), police20, (255,255,255))]))

            Data.menus.append(sb.Menu_Diff(data, [ui.Bouton(245, 150, 150, 50,2,(2,235,2),"Facile",color_boutons,police,(255,255,255)),ui.Bouton(245, 250, 150, 50,2,(220,220,2),"Normal",color_boutons,police,(255,255,255)),ui.Bouton(245, 350, 150, 50,2,(235,2,2),"Difficile",color_boutons,police,(255,255,255))], [ui.Title(75, 80, 500, 50, 2, "Choisir la difficulté", (0,0,0,0), police, (255,255,255))]))

            Data.menus.append(sb.Menu_Sudoku(data, [ui.Bouton(480,420,150,50,2,color_boutons_change,"Pause",(152,152,152),police,(255,255,255))]))

            Data.menus.append(sb.Menu_SudokuEnd(data, [ui.Bouton(245, 200, 150, 50,2,(2,235,2),"Recommencer",color_boutons,police20,(255,255,255)), ui.Bouton(245, 300, 150, 50,2,(220,220,2),"Retourner au menu",color_boutons,pygame.font.SysFont('Impact',18),(255,255,255))]))

            Data.menus.append(sb.Menu_SudokuP(data, [ui.Bouton(245,165,150,50,2,(120,120,120),"Reprendre",(152,152,152),police,(255,255,255)), ui.Bouton(245,240,150,50,2,(120,120,120),"Quitter et Sauvegarder",(152,152,152),police,(255,255,255)), ui.Bouton(245,315,150,50,2,(120,120,120),"Quitter sans Sauvegarder",(152,152,152),police,(255,255,255))]))

            pass

        # Fonction setEtat(e)
        #
        # e : le nouvel état du jeu
        #
        def setEtat(self, e):
            self.etat = e

        # Fonction setSound(e)
        #
        # e : boolean pour activer ou non les sons
        #
        def setSound(self,e):
            self.sound_active = e

        # Fonction setSound(e)
        #
        # e : boolean pour activer ou non les sons
        #
        def setMusic(self,e):
            self.music_active = e
