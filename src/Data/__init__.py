import pygame
import SubMenu as sb
from BatailleNavale import BN_Menu
import UiPygame as ui
from LTO import loto_menu as lm
import Sound
import os
from Particules import ParticleSystem
from Classements import Classements

class Data:

        # Sert a contenir tous les menus du jeu
        menus = []
        # Tous les états possibles se trouvent dans ce tableau, utilisé car plus de lisibilité.
        etatsStr = {"main": 0,
                    "options": 1,
                    "Sudoku_Saved": 2,
                    "Sudoku_Diff": 3,
                    "Sudoku_Game": 4,
                    "Sudoku_Win": 5,
                    "Sudoku_Pause": 6,
                    "Classements":7,
                    "Loto_Choose":8,
                    "Loto_Play":9,
                    "Loto_End":10,
                    "BN_Place":11,
                    "BN_Play":12,
                    "BN_End":13,
                    "BN_Pause":14,
                    "profil":15}

        # Constructeur de la classe Data
        #
        # self : instance crée par le constructeur, ne doit pas être mis en argument.
        # frame : instance de la fenêtre
        #
        def __init__(self, frame):
            # Cette variable représente les différents états dans lequel le jeu peut se trouver.
            self.etat = 0
            # Cette variable représente la partie au cas ou on en aurait besoin.
            self.partie = None
            # Cette variable représente le joueur au cas ou on en aurait besoin.
            self.joueur = None

            # Ces variables permettent d'activer et désactiver le son/musique
            self.sound_active = True
            self.music_active = True
            self.soundSystem = Sound.SoundManager(self)
            self.fin = False
            self.fond = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "background_menu.jpg")).convert()
            frame.blit(self.fond, (0,0))
            self.particules = ParticleSystem.ParticleSystem()
            self.classements = [Classements.Classement(["Profil", "Temps", "Erreurs"], [0.5, 0.75]), None,
                                Classements.Classement(["Profil", "Gagné/Perdu","Taux réussite"], [0.3,0.7]), None]
            self.classements[0].load("Classements_Sudoku.yolo")
            self.classements[2].load("Classements_Loto.yolo")

        # Fonction init
        #
        # frame : instance de la fenêtre
        # data : instance de la classe Data
        #
        # Fonction servant a initialiser les menus et a lire la configuration des options
        #
        @staticmethod
        def init(frame, data):
            police20 = pygame.font.SysFont('Impact',20)
            police = pygame.font.SysFont('Impact',25)
            color_boutons = (170,170,170);color_boutons_change = (45,45,45);color_f = (255,255,255);
            width_b = 400;x_btn = (frame.get_width()/2) - (width_b/2);y_btn_start = 160
            # Initialisation des menus
            Data.menus.append(sb.Main_Menu(data, [ui.Bouton(x_btn,y_btn_start-50,width_b,50,2,color_boutons_change,"Sudoku",color_boutons,police,color_f),
                        ui.Bouton(x_btn,y_btn_start+10,width_b,50,2,color_boutons_change,"Loto",color_boutons,police,color_f),
                        ui.Bouton(x_btn,y_btn_start+70,width_b,50,2,color_boutons_change,"Bataille navale",color_boutons,police,color_f),
                        ui.Bouton(x_btn,y_btn_start+130,width_b,50,2,color_boutons_change,"Poker",color_boutons,police,color_f),
                        ui.Bouton(30,frame.get_height()-130,280,50,2,color_boutons_change,"Options",color_boutons,police,color_f),
                        ui.Bouton((frame.get_width()/2)+10,frame.get_height()-130,280,50,2,color_boutons_change,"Profil",color_boutons,police,color_f),
                        ui.Bouton(30,frame.get_height()-60,280,50,2,color_boutons_change,"Classements",color_boutons,police,color_f),
                        ui.Bouton((frame.get_width()/2)+10,frame.get_height()-60,280,50,2,color_boutons_change,"Quitter",color_boutons,police,color_f)]))

            Data.menus.append(sb.Menu_Optn(data,
                                           [ui.Bouton(50,frame.get_height()-60,200,50,2,color_boutons_change,"Sauvegarder",color_boutons,police,color_f),
                                            ui.Bouton(frame.get_width()-50-200,frame.get_height()-60,200,50,2,color_boutons_change,"Retour",color_boutons,police,color_f),
                                            ui.Bouton(75,200,frame.get_width()-150,50,2,color_boutons_change,"Désactiver la musique",color_boutons,police,color_f),
                                            ui.Bouton(75,300,frame.get_width()-150,50,2,color_boutons_change,"Activer les bruitages",color_boutons,police,color_f)
                                            ],
                                           [ui.Title(50,50,(frame.get_width()-100),60,3,"OPTIONS",(152,152,152),police,(255,255,255))]

                                           ))

            Data.menus.append(sb.Menu_SavedGrille(data, [ui.Bouton(245, 220, 150, 50,0,(45,45,45),"Oui",(180,180,180),police,(255,255,255)), ui.Bouton(245, 320, 150, 50,0,(45,45,45), "Non",(180,180,180),police,(255,255,255))],
                                                    [ui.Title(75, 100, 500, 100, 2, "Une partie a été sauvegardée, voulez-vous la charger?", (0,0,0,0), police20, (255,255,255))]))

            Data.menus.append(sb.Menu_Diff(data, [ui.Bouton(245, 150, 150, 50,2,(2,235,2),"Facile",color_boutons,police,(255,255,255)),ui.Bouton(245, 250, 150, 50,2,(220,220,2),"Normal",color_boutons,police,(255,255,255)),ui.Bouton(245, 350, 150, 50,2,(235,2,2),"Difficile",color_boutons,police,(255,255,255))], [ui.Title(75, 80, 500, 50, 2, "Choisir la difficulté", (0,0,0,0), police, (255,255,255))]))

            Data.menus.append(sb.Menu_Sudoku(data, [ui.Bouton(480,420,150,50,2,color_boutons_change,"Pause",(152,152,152),police,(255,255,255))]))

            Data.menus.append(sb.Menu_SudokuEnd(data, [ui.Bouton(245, 200, 150, 50,2,(2,235,2),"Recommencer",color_boutons,police20,(255,255,255)), ui.Bouton(245, 300, 150, 50,2,(220,220,2),"Retourner au menu",color_boutons,pygame.font.SysFont('Impact',18),(255,255,255))]))

            Data.menus.append(sb.Menu_SudokuP(data, [ui.Bouton(180,165,frame.get_width()-300-60,50,2,(120,120,120),"Reprendre",(152,152,152),police,(255,255,255)),
                                                     ui.Bouton(180,240,frame.get_width()-300-60,50,2,(120,120,120),"Sauvegarder et quitter",(152,152,152),police,(255,255,255)),
                                                     ui.Bouton(180,315,frame.get_width()-300-60,50,2,(120,120,120),"Quitter sans sauvegarder",(152,152,152),police,(255,255,255))]))

            Data.menus.append(sb.Menu_Classements(data, [ui.Bouton(10, 10, frame.get_width()/4 - 20, 50, 2, (45, 45, 45), "Sudoku", (170, 170, 170), police,(255,255,255)),
                                                         ui.Bouton(frame.get_width()/4+10, 10, frame.get_width()/4 - 20, 50, 2, (45, 45, 45), "Poker", (170, 170, 170), police,(255,255,255)),
                                                         ui.Bouton(frame.get_width()/2+10, 10, frame.get_width()/4 - 20, 50, 2, (45, 45, 45), "Loto", (170, 170, 170), police,(255,255,255)),
                                                         ui.Bouton(3*frame.get_width()/4+10, 10, frame.get_width()/4 - 20, 50, 2, (45, 45, 45), "Bataille Navale", (170, 170, 170), police20,(255,255,255)),
                                                         ui.Bouton(frame.get_width()/2 - 75, frame.get_height()-60, 150, 50, 2, (45,45,45), "Retour au menu", (170,170,170), police20,(255,255,255))]))


            Data.menus.append(lm.Menu_LotoChoose(data,frame))#Loto choose
            Data.menus.append(lm.Menu_LotoPlay(data,frame))#Loto Play
            Data.menus.append(lm.Menu_LotoEnd(data,frame))#Loto End
            Data.menus.append(BN_Menu.BN_Place_Boats(data, [ui.Bouton(frame.get_width()/2 - frame.get_width()/3, 20, frame.get_width()/4, 50, 2, (45, 45, 45), "Valider", (170, 170, 170), police, (255, 255, 255)),
                                                            ui.Bouton(frame.get_width()/2 + frame.get_width()/3 - frame.get_width()/4, 20, frame.get_width()/4, 50, 2, (45, 45, 45), "Retour au menu", (170, 170, 170), police20, (255, 255, 255))]))#BN Place
            Data.menus.append(BN_Menu.BN_Jouer(data, [ui.Bouton(500, 110, 150, 50, 2, (45, 45, 45), "voir la grille de l'adversaire", (170, 170, 170), pygame.font.SysFont('Impact',12), (255, 255, 255)),
                                                      ui.Bouton(500, 210, 150, 50, 2, (185, 75, 75), "Tirer", (170, 170, 170), police, (255, 255, 255)),
                                                      ui.Bouton(500, 410, 150, 50, 2, (45, 45, 45), "Pause", (170, 170, 170), police, (255, 255, 255))]))#BN Play
            Data.menus.append(BN_Menu.BN_GGAGNER(data, [ui.Bouton(160, 290, 320, 50, 2, (45, 45, 45), "Rejouer", (170, 170, 170), police, (255, 255, 255)),
                                                        ui.Bouton(160, 390, 320, 50, 2, (45, 45, 45), "Retour au menu", (170, 170, 170), police, (255, 255, 255))]))#BN End
            Data.menus.append(BN_Menu.BN_Pause(data, [ui.Bouton(245,165,150,50,2,(120,120,120),"Reprendre",(152,152,152),police,(255,255,255)),
                                                      ui.Bouton(245,235,150,50,2,(120,120,120),"Quitter",(152,152,152),police,(255,255,255))]))#BN Pause
            Data.menus.append(None)#Profil
            Data.menus[1].readCfg() # Lecture des options depuis le fichier de config
            pass

        # Fonction getCurrentMenu
        #
        # Fonction servant a récupérer le menu actuel
        #
        def getCurrentMenu(self):
            return Data.menus[self.etat]

        # Fonction setEtat(e)
        #
        # e : le nouvel état du jeu
        #
        def setEtat(self, e):
            if isinstance(e, int):
                self.etat = e
            elif isinstance(e, str):
                self.etat = Data.etatsStr[e]
            else:
                raise TypeError("setEtat from Data object takes an int or a string as argument.")

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

        # Fonction getParticleSystem(self)
        #
        # retourne le system de particules
        #
        def getParticleSystem(self):
            return self.particules

        # Fonction haveTimerTick
        #
        # Permet de déterminer si la partie contenue dans cette instance de la classe utilise la boucle
        # du chronomètre du main
        #
        def haveTimerTick(self):
            if self.partie == None:
                return False
            else:
                try:
                    d = self.partie.timerTick()
                    if isinstance(d, list):
                        for i in d:
                            if self.etat == d:
                                return True
                        return False
                    elif d == None:
                        return True
                    else:
                        return self.etat == d
                except:
                    return False

        # Fonction mustDraw
        #
        # Permet de déterminer si la partie contenue dans cette instance de la classe doit être redéssinée a chaque
        # itération de la boucle principale
        #
        def mustDraw(self):
            if self.partie == None:
                return False
            else:
                try:
                    return self.partie.mustDraw()
                except:
                    return False
