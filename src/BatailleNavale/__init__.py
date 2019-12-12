import pygame
from pygame.locals import *
import pickle
import os, math, time
import Data as da
from Grille import Grille
from Grille import Bataille_Navale_Case
from BatailleNavale import IA
from Particules import FireWorkParticule, Particule

class GameBN:

    # Constructeur de la classe GameBN
    #
    # self : instance crée par le constructeur, ne doit pas être mis en argument.
    # data : instance de la classe Data
    #
    def __init__(self, data):
        self.data = data
        # Création des grilles
        self.grille_J1 = Grille.Grille(10, 10, 145, 100, 495, 450, Bataille_Navale_Case)
        self.grille_J2 = Grille.Grille(10, 10, 145, -450, 495, -100, Bataille_Navale_Case)
        # On indique que la grille du joueur 2 ne doit pas montrer les bateaux
        self.grille_J2.unshowShip()
        # Ajout des images des bateaux + redimension de ces images
        self.bateauStr = {"Porte-Avion": [pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/Porte-avions_1.png")).convert_alpha(), (35, 35)),
                                          pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/Porte-avions_2.png")).convert_alpha(), (35, 35)),
                                          pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/Porte-avions_3.png")).convert_alpha(), (35, 35)),
                                          pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/Porte-avions_4.png")).convert_alpha(), (35, 35)),
                                          pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/Porte-avions_5.png")).convert_alpha(), (35, 35))],
                     "Croiseur": [pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/croiseur_1.png")).convert_alpha(), (35, 35)),
                                  pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/croiseur_2.png")).convert_alpha(), (35, 35)),
                                  pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/croiseur_3.png")).convert_alpha(), (35, 35)),
                                  pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/croiseur_4.png")).convert_alpha(), (35, 35))],
                     "Contre-Torpilleur": [pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/contre-torpilleur_1.png")).convert_alpha(), (35, 35)),
                                           pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/contre-torpilleur_2.png")).convert_alpha(), (35, 35)),
                                           pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/contre-torpilleur_3.png")).convert_alpha(), (35, 35))],
                     "Sous-marin": [pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/sous-marin_1.png")).convert_alpha(), (35, 35)),
                                    pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/sous-marin_2.png")).convert_alpha(), (35, 35)),
                                    pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/sous-marin_3.png")).convert_alpha(), (35, 35))],
                     "Torpilleur": [pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/torpilleur_1.png")).convert_alpha(), (35, 35)),
                                    pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/torpilleur_2.png")).convert_alpha(), (35, 35))]}

        # Ajout des images des bateaux + redimension de ces images + rotation a 90 degrés des images
        # Sert pour l'affichage des bateau tournés
        self.bateauStr_H = {"Porte-Avion": [pygame.transform.rotate(self.bateauStr["Porte-Avion"][0], 90),
                                          pygame.transform.rotate(self.bateauStr["Porte-Avion"][1], 90),
                                          pygame.transform.rotate(self.bateauStr["Porte-Avion"][2], 90),
                                          pygame.transform.rotate(self.bateauStr["Porte-Avion"][3], 90),
                                          pygame.transform.rotate(self.bateauStr["Porte-Avion"][4], 90)],
                     "Croiseur": [pygame.transform.rotate(self.bateauStr["Croiseur"][0], 90),
                                  pygame.transform.rotate(self.bateauStr["Croiseur"][1], 90),
                                  pygame.transform.rotate(self.bateauStr["Croiseur"][2], 90),
                                  pygame.transform.rotate(self.bateauStr["Croiseur"][3], 90)],
                     "Contre-Torpilleur": [pygame.transform.rotate(self.bateauStr["Contre-Torpilleur"][0], 90),
                                           pygame.transform.rotate(self.bateauStr["Contre-Torpilleur"][1], 90),
                                           pygame.transform.rotate(self.bateauStr["Contre-Torpilleur"][2], 90)],
                     "Sous-marin": [pygame.transform.rotate(self.bateauStr["Sous-marin"][0], 90),
                                    pygame.transform.rotate(self.bateauStr["Sous-marin"][1], 90),
                                    pygame.transform.rotate(self.bateauStr["Sous-marin"][2], 90)],
                     "Torpilleur": [pygame.transform.rotate(self.bateauStr["Torpilleur"][0], 90),
                                    pygame.transform.rotate(self.bateauStr["Torpilleur"][1], 90)]}
        # Données de placements sous forme [(bx1, by1), (bx2, by2), (bx3, by3), (bx4, by4), (bx5, by5), grille du joueur n montrée, ID bateau sélectionné, [dirBateau1, dirBateau2, dirBateau3, dirBateau4, dirBateau5]]
        self.placeData = [(10, 150), (52, 150), (10, 330), (52, 330), (94, 280), 1, -1, ["Verticale", "Verticale", "Verticale", "Verticale", "Verticale"]]
        # Données de jeu sous forme [tour du joueur n, grille du joueur n montrée]
        self.currentPlayData = [1, 1]
        # texture de l'animation de tir
        self.tirTexture = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/tir.png")).convert_alpha(), (35, 35))
        self.tirData = [-1, -1]
        # Timer pour l'animation de tir
        self.tirTimer = 0;
        # Variable indiquant le gagnant de la partie
        self.winner = 0

        # Variables dont ont se sert pour la précision
        self.tirTouche = [0, 0]
        self.tirCoule = [0, 0]
        self.tirs = [0, 0]
        self.time = 0
        # Variable contenant l'IA
        self.IA = None

    # Fonction createIA
    #
    # self : instance de la classe, ne doit pas être mis en argument.
    #
    # Fonction servant a jaouter une IA au jeu
    #
    def createIA(self):
        self.IA = IA.BN_IA(self.grille_J2, self)
        self.IA.generateGrille()

    # Fonction mustDraw
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction indiquant si la parite doit être redessinée ou non
    #
    def mustDraw(self):
        return self.tirTimer >= 0 or (self.currentPlayData[0] == 2 and self.IA != None)

    # Fonction timerTick
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction appellée toute les secondes pour performer des actions
    #
    def timerTick(self):
        if self.currentPlayData[0] == 2 and self.IA != None:
            self.IA.timerTick()
        return 12

    # Fonction invert_Grilles_Pos
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction servant a intervertir les 2 grilles de la partie de place.
    # Appellée au changement de tour ou a l'appui sur le bouton de changement de grille
    #
    def invert_Grilles_Pos(self):
        if self.grille_J1.y < 0:
            self.grille_J1.y = 100
            self.grille_J1.y2 = 450
            self.grille_J2.y = -450
            self.grille_J2.y2 = -100
        else:
            self.grille_J2.y = 100
            self.grille_J2.y2 = 450
            self.grille_J1.y = -450
            self.grille_J1.y2 = -100

    # Fonction ajouter_Bateau
    #
    # self : instance de la partie, ne pas mettre en argument
    # grille : grille dans laquelle ajouter le bateau
    # direction : direction du bateau a ajouter
    # position : position du bateau a ajouter
    # type : type du bateau a ajouter
    #
    # Cette fonction sert a ajouter un bateau dans la grille "grille"
    #
    def ajouter_Bateau(self, grille, direction, position, type):
        l = len(self.bateauStr[type])
        if direction == 'Horizontale':
            if position[0] > self.grille_J1.largeur-l+1 or position[0] < 1 or not self.peutAjouterBateau(grille, direction, position, type):
                print("Position invalide")
                return False
            else:
                for x in range(l):
                    grille.getCaseByCoords(position[0]+x-1, position[1]-1).setContenu(self.bateauStr_H[type][x])
        elif direction == 'Verticale':
            if position[1] > self.grille_J1.hauteur-l+1 or position[1] < 1 or not self.peutAjouterBateau(grille, direction, position, type):
                print("Position invalide")
                return False
            else:
                for x in range(l):
                    grille.getCaseByCoords(position[0]-1, position[1]+x-1).setContenu(self.bateauStr[type][x])
        else:
            print("Direction invalide")
            return False

        return True

    # Fonction peutAjouterBateau
    #
    # self : instance de la partie, ne pas mettre en argument
    # grille : grille ou ajouter le bateau
    # direction : direction du bateau a ajouter
    # position : position du bateau a ajouter
    # type : type du bateau a ajouter
    #
    # Fonction determinant si un bateau peut être placé a la position "position" sur la grille "grille"
    #
    def peutAjouterBateau(self, grille, direction, position, type):
        l = len(self.bateauStr[type])
        if direction == 'Horizontale':
            for i in range(l):
                if not grille.getCaseByCoords(position[0]+i-1, position[1]-1).estVide():
                    print("2 bateaux se superposent : ")
                    return False
        elif direction == 'Verticale':
            for i in range(l):
                if not grille.getCaseByCoords(position[0]-1, position[1]+i-1).estVide():
                    print("2 bateaux se superposent : ")
                    return False
            pass
        return True

    # Fonction tir
    #
    # self : instance de la partie, ne pas mettre en argument
    # grille : grille sur laquelle tirer
    # position : endroit ou l'on tire
    #
    # Fonction permettant de tirer sur la grille "grille"
    #
    def tir(self, grille, position):
        if position[0] > 10 or position[0] < 1 or position[1] > 10 or position[1] < 1:
            print("Position invalide")
            return None
        else:
            case = grille.getCaseByCoords(position[0]-1, position[1]-1)
            case.shoot()
            joueur = 2-self.currentPlayData[1]
            self.tirs[joueur] = self.tirs[joueur] + 1
            if case.estVide():
                self.tirCoule[joueur] = self.tirCoule[joueur]+1
            else:
                self.tirTouche[joueur] = self.tirTouche[joueur]+1
            return not case.estVide()

    # Fonction timerTick
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction appellée toute les secondes pour performer des actions
    #
    def timerTick(self):
        self.time = self.time + 1
        return 12

    # Fonction checkVictory
    #
    # self : instance de la partie, ne pas mettre en argument
    # grille : grille sur laquelle vérifier
    #
    # Fonction servant a vérifier si l'un des joueurs gagne la partie
    #
    def checkVictory(self, grille):
        i = 0
        for y in range(grille.hauteur):
            for x in range(grille.largeur):
                if not grille.getCaseByCoords(x, y).estVide() and grille.getCaseByCoords(x, y).isShot():
                    i = i+1
        return i == 17

    # Fonction precision
    #
    # self : instance de la partie, ne pas mettre en argument
    # joueur : joueur dont on veut la précision
    #
    # Permet de retourner la précision en pourcentage du joueur durant cette partie
    #
    def precision(self, joueur):
        if self.tirs[joueur] == 0:
            return 100
        return (self.tirTouche[joueur]/self.tirs[joueur]) * 100

    # Fonction selectBateau
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction servant a selectionner un bateau
    # Utilisée quand on clique dans la phase de placement des bateau
    #
    def selectBateau(self):
        pos = pygame.mouse.get_pos()
        l = len(list(self.bateauStr.keys())) # On récupère tous les types de bateaux
        for i in range(l):
            if self.placeData[7][i] == "Verticale":
                if pos[0] > self.placeData[i][0] and pos[0] < self.placeData[i][0] + 32 and pos[1] > self.placeData[i][1] and pos[1] < self.placeData[i][1] + l*32:
                    self.placeData[6] = i
                    break
            else:
                if pos[0] > self.placeData[i][0] and pos[0] < self.placeData[i][0] + l*32 and pos[1] > self.placeData[i][1] and pos[1] < self.placeData[i][1] + 32:
                    self.placeData[6] = i
                    break

        grille = self.grille_J2
        if self.placeData[5] == 1:
            grille = self.grille_J1

        if grille.getCaseByClick(pos[0], pos[1]) != None: # Si on clique sur une case de la grille
            # On récupère la case sur laquelle on a cliqué
            cx = int(math.floor((pos[0] - grille.x) / ((abs(grille.x2 - grille.x) / grille.largeur))))
            cy = int(math.floor((pos[1] - grille.y) / ((abs(grille.y2 - grille.y) / grille.hauteur))))
            case = grille.getCaseByCoords(cx, cy)
            if case.getcontenu() != None: # Si la case n'est pas vide
                l = list(self.bateauStr.values()) # on récupère tous les bateaux
                for i in range(len(l)): # on récupère toutes les parties du bateau a placer
                    for j in range(len(l[i])): # on récupère toutes les parties du bateau a placer
                        if case.contient(l[i][j]): # Si la case contient la partie j du bateau i
                            self.placeData[6] = i # On sélectionne le bateau i
                            cy = cy-j
                            for k in range(len(list(l[i]))): # On enlève toutes les parties du bateau i de la grille
                                grille.getCaseByCoords(cx, cy+k).setContenu(None)
                            break

                # On teste la même chose mais avec les bateaux horizontaux
                l = list(self.bateauStr_H.values())
                for i in range(len(l)):
                    for j in range(len(l[i])):
                        if case.contient(l[i][j]):
                            self.placeData[6] = i
                            cx = cx-j
                            for k in range(len(list(l[i]))):
                                grille.getCaseByCoords(cx+k, cy).setContenu(None)
                            break

    # Fonction placeBateau
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction permettant de placer un bateau sur la grille du joueur 1 ou de deselectionner le bateau
    # actuellement selectionné si le clic est effectué en dehors de la grille
    # Appellée quand un clic de souris est effectué pendant la phase de placement des bateau
    #
    def placeBateau(self):
        pos = pygame.mouse.get_pos()
        grille = self.getGrille()
        if grille.getCaseByClick(pos[0], pos[1]) != None: # On vérifie que le joueur a clique sur une case
            # On récupère la case sur laquelle on a cliqué
            cx = int(math.floor((pos[0] - grille.x) / ((abs(grille.x2 - grille.x) / grille.largeur))))
            cy = int(math.floor((pos[1] - grille.y) / ((abs(grille.y2 - grille.y) / grille.hauteur))))
            # Ajout du bateau
            if self.ajouter_Bateau(grille, self.placeData[7][self.placeData[6]], (cx+1, cy+1), list(self.bateauStr.keys())[self.placeData[6]]):
                self.placeData[self.placeData[6]] = (-self.placeData[self.placeData[6]][0], -self.placeData[self.placeData[6]][1])
                self.placeData[6] = -1
        else:
            self.placeData[6] = -1

    # Fonction TournerBateau
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction permettant de tourner un bateau
    # Appellée quand un clic droit de souris est effectué pendant la phase de placement des bateau
    #
    def TournerBateau(self):
        if self.placeData[6] > -1:
            if self.placeData[7][self.placeData[6]] == "Verticale":
                self.placeData[7][self.placeData[6]] = "Horizontale"
            else:
                self.placeData[7][self.placeData[6]] = "Verticale"

    # Fonction getGrille
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction permettant de retourner la grille actuellement montrée a l'écran
    #
    def getGrille(self):
        if self.data.etat == 11:
            return self.grille_J1 if self.placeData[5] == 1 else self.grille_J2
        elif self.data.etat == 12:
            return self.grille_J1 if self.currentPlayData[1] == 1 else self.grille_J2

    # Fonction playTir
    #
    # ARGUMENTS OBLIGATOIRES :
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # ARGUMENTS OPTIONNELS :
    #
    # case : case sur laquelle tirer, si non précisé, effecuera un tir sur la case sélectionnée de la grille
    # actuellement montrée a l'écran
    #
    # Fonction enclenchant l'aimation de tir
    #
    def playTir(self, case=(-1, -1)):
        grille = self.getGrille()
        caseT = grille.getSelectedCase() # On tir sur la case actuellement séléctionnée (pour le joueur)
        if caseT[0] == None and not(self.currentPlayData[0] == 2 and self.IA != None):
            return None
        self.tirTimer = 60 # On attend 60 ticks
        self.tirData = [caseT[1]%grille.largeur, math.floor(caseT[1]/grille.largeur)] if case[0] < 0 or case[1] < 0 else [case[0], case[1]]
        if self.currentPlayData[0] == 1 and self.IA != None:
            self.currentPlayData[0] = 2

    # Fonction allBoatsPlaced
    #
    # self : instance de la partie, ne pas mettre en argument
    #
    # Fonction verifiant si les 5 bateaux sont placés sur la grille
    # Appellée uniquement quand le boutons Valider est pressé pendant la phase de placement des bateaux
    #
    def allBoatsPlaced(self):
        for i in range(5):
            if self.placeData[i][0] > 0 or self.placeData[i][1] > 0:
                return False
        return True

    #Fonction compareFunc
    #
    # self : instance de la partie, ne pas mettre en argument
    # tab :tableau contenant les scores sous la forme : [ratioVD1, ratioVD2, precision1, precision2]
    #
    # Fonction comparant 2 scores et retourne True si le premier score est le meilleur, sinon retourne False
    #
    def compareFunc(self, tab):
        donnees = [tab[0].split("/"), tab[1].split("/")]
        if int(donnees[0][1]) == 0:
            donnees[0][1] = "1"
            return int(donnees[1][1]) > 0
        elif int(donnees[1][1]) == 0:
            donnees[1][1] = "1"
            return False

        pt = tab[2][:3]
        if pt[-1] == ".":
            pt = pt[:-1]
        if pt[-2] == ".":
            pt = pt[:-2]

        pt2 = tab[3][:3]
        if pt2[-1] == ".":
            pt2 = pt2[:-1]
        if pt2[-2] == ".":
            pt2 = pt2[:-2]
        return int(donnees[0][0])/int(donnees[0][1]) + int(pt) > int(donnees[1][0])/int(donnees[1][1]) + int(pt2)

    # Fonction victoire
    #
    # self : instance de la partie, ne pas mettre en argument
    # data : instance de la classe data
    #
    # Fonction activant les feux d'artifices de victoires et ajoutant le score au classement
    #
    def victoire(self,data):
        joueur = data.profilHandler.getcurrentProfil()
        if joueur != None:
            joueur = joueur._getPseudo()
        else:
            joueur = "Anonyme"
        score = data.classements[3].getScore(joueur) # On récupère le score du joueur
        if score == 0: # Si il n'y a aucun score
            Nprec = self.precision(0)
            if len(str(Nprec)) > 5:
                Nprec = str(Nprec)[:5]
            else:
                Nprec = str(Nprec)
            self.data.classements[3].ajouterScore((joueur,"1/0",Nprec+"%")) #On ajoute une score tout neuf
        else:
            self.data.classements[3].removeScore(score)
            donnees = score[1].split("/")
            pt = score[2][:3]
            if pt[-1] == ".":
                pt = pt[:-1]
            if pt[-2] == ".":
                pt = pt[:-2]
            Nprec = (int(pt) * (int(donnees[0])+int(donnees[1])) + self.precision(0)) / (int(donnees[0])+int(donnees[1])+1)
            if len(str(Nprec)) > 5:
                Nprec = str(Nprec)[:5]
            else:
                Nprec = str(Nprec)
            self.data.classements[3].ajouterScore((joueur,str(int(donnees[0])+1)+"/"+str(donnees[1]),Nprec+"%"))
        data.classements[3].sort(self.compareFunc)
        data.classements[3].save("Classements_Bataille_Navale.yolo")
        rayon = 4
        data.particules.addEmitter(FireWorkParticule.FireworkEmitter(data.particules, [Particule.Particule((100,100), 60, (230, 60, 60))], [(0, 235, 0), (0, 100, 0)], rayon, 60, (320, 480), (0, -4) , 0, 2))

    def defaite(self, data):
        joueur = data.profilHandler.getcurrentProfil()
        if joueur != None:
            joueur = joueur._getPseudo()
        else:
            joueur = "Anonyme"
        score = data.classements[3].getScore(joueur) # On récupère le score du joueur
        if score == 0: # Si il n'y a aucun score
            Nprec = self.precision(0)
            if len(str(Nprec)) > 5:
                Nprec = str(Nprec)[:5]
            else:
                Nprec = str(Nprec)
            self.data.classements[3].ajouterScore((joueur,"1/0",Nprec+"%")) #On ajoute une score tout neuf
        else:
            self.data.classements[3].removeScore(score)
            donnees = score[1].split("/")
            pt = score[2][:3]
            if pt[-1] == ".":
                pt = pt[:-1]
            if pt[-2] == ".":
                pt = pt[:-2]
            Nprec = (int(pt) * (int(donnees[0])+int(donnees[1])) + self.precision(0)) / (int(donnees[0])+int(donnees[1])+1)
            if len(str(Nprec)) > 5:
                Nprec = str(Nprec)[:5]
            else:
                Nprec = str(Nprec)
            self.data.classements[3].ajouterScore((joueur,str(int(donnees[0])+1)+"/"+str(donnees[1]),Nprec+"%"))
        data.classements[3].sort(self.compareFunc)
        data.classements[3].save("Classements_Bataille_Navale.yolo")

    # Fonction draw
    #
    # ARGUMENTS OBLIGATOIRES :
    #
    # self : instance de la partie, ne pas mettre en argument
    # frame : instance de la fenêtre
    #
    # ARGUMENTS OPTIONNELS :
    #
    # menu : menu a dessiner par dessus le jeu
    #
    # Fonction permettant de dessiner le jeu (et accesoirement gère l'animation de tir)
    #
    def draw(self, frame, menu=None):
        frame.fill((1, 80, 172))
        if self.currentPlayData[0] != self.currentPlayData[1] or self.tirTimer > 0:
            pygame.draw.rect(frame, (1, 70, 132), (145, 100, 350, 350))
        self.getGrille().draw(frame, (250, 250, 250), (95, 95, 244), (85, 85, 234), (90, 90, 239))

        if self.placeData[6] != -1:
            pos = pygame.mouse.get_pos()
            self.placeData[self.placeData[6]] = (pos[0], pos[1])

        for i in range(len(list(self.bateauStr_H.keys()))):
            if self.placeData[i][0] >= 0 and self.placeData[i][1] >= 0:
                if self.placeData[7][i] == "Horizontale":
                    if self.placeData[i][0] != 0 or self.placeData[i][1] != 0:
                        for j in range(len(self.bateauStr_H[list(self.bateauStr_H.keys())[i]])):
                            frame.blit(self.bateauStr_H[list(self.bateauStr_H.keys())[i]][j], (self.placeData[i][0]+32*j, self.placeData[i][1]))
                else:
                    if self.placeData[i][0] != 0 or self.placeData[i][1] != 0:
                        for j in range(len(self.bateauStr[list(self.bateauStr.keys())[i]])):
                            frame.blit(self.bateauStr[list(self.bateauStr.keys())[i]][j], (self.placeData[i][0], self.placeData[i][1]+32*j))

        if self.tirTimer <= 30 and self.tirTimer > 0:
            grille = self.getGrille()
            largeur = abs(grille.x2 - grille.x)
            hauteur = abs(grille.y2 - grille.y)
            case_Largeur = largeur / grille.largeur
            case_Hauteur = hauteur / grille.hauteur
            if self.tirTimer == 30:
                self.data.soundSystem.playSound("BN_plouf" if self.getGrille().getCaseByCoords(self.tirData[0], self.tirData[1]).estVide() else "BN_boom")
                self.tir(grille, (self.tirData[0]+1, self.tirData[1]+1))
            elif self.tirTimer == 1:
                if self.checkVictory(grille):
                    self.winner = self.currentPlayData[0]
                    da.Data.menus[13].setWin(self.winner)
                    self.currentPlayData[0] = 0
                    if self.winner == 1:
                        self.victoire(self.data)
                    else:
                        self.defaite(self.data)
                        self.data.soundSystem.playMusic("triste")
                    self.data.setEtat("BN_End")
                    self.data.partie = None
                    del self
                    return
                else:
                    if self.currentPlayData[0] == 2 and self.IA != None:
                        if self.IA.played:
                            self.IA.played = False
                            self.currentPlayData[0] = 1 if self.currentPlayData[0] == 2 else 2
                        else:
                            self.IA.play()
                    else:
                        self.currentPlayData[0] = 1 if self.currentPlayData[0] == 2 else 2
                    self.data.getCurrentMenu().boutons[1].rgb_when_change = (185, 75, 75) if self.currentPlayData[1] == self.currentPlayData[0] or self.currentPlayData[0] == 2 else (45, 45, 45)
            frame.blit(self.tirTexture, (grille.x + self.tirData[0] * case_Largeur, grille.y + self.tirData[1] * case_Hauteur))
            self.tirTimer = self.tirTimer-1
        else:
            self.tirTimer = self.tirTimer-1

        if menu != None:
            menu.draw(frame)
        pass
