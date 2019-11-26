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

    def __init__(self, data):
        self.data = data
        self.grille_J1 = Grille.Grille(10, 10, 145, 100, 495, 450, Bataille_Navale_Case)
        self.grille_J2 = Grille.Grille(10, 10, 145, -450, 495, -100, Bataille_Navale_Case)
        self.grille_J2.unshowShip()
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
        self.placeData = [(10, 150), (52, 150), (10, 330), (52, 330), (94, 280), 1, -1, ["Verticale", "Verticale", "Verticale", "Verticale", "Verticale"]]
        self.currentPlayData = [1, 1]
        self.tirTexture = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Bataille Navale/tir.png")).convert_alpha(), (35, 35))
        self.tirData = [-1, -1]
        self.tirTimer = 0;
        self.winner = 0
        self.IA = None

    def createIA(self):
        self.IA = IA.BN_IA(self.grille_J2, self)
        self.IA.generateGrille()

    def mustDraw(self):
        return self.tirTimer >= 0 or (self.currentPlayData[0] == 2 and self.IA != None)

    def timerTick(self):
        if self.currentPlayData[0] == 2 and self.IA != None:
            self.IA.timerTick()
        return 12

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

    def peutAjouterBateau(self, grille, direction, position, type):
        l = len(self.bateauStr[type])
        if direction == 'Horizontale':
            for i in range(l):
                if not grille.getCaseByCoords(position[0]+i-1, position[1]-1).estVide():
                    print("2 bateaux se superposent : ", end="")
                    return False
        elif direction == 'Verticale':
            for i in range(l):
                if not grille.getCaseByCoords(position[0]-1, position[1]+i-1).estVide():
                    print("2 bateaux se superposent : ", end="")
                    return False
            pass
        return True

    def tir(self, grille, position):
        if position[0] > 10 or position[0] < 1 or position[1] > 10 or position[1] < 1:
            print("Position invalide")
            return None
        else:
            grille.getCaseByCoords(position[0]-1, position[1]-1).shoot()
            return not grille.getCaseByCoords(position[0]-1, position[1]-1).estVide()

    def checkVictory(self, grille):
        i = 0
        for y in range(grille.hauteur):
            for x in range(grille.largeur):
                if not grille.getCaseByCoords(x, y).estVide() and grille.getCaseByCoords(x, y).isShot():
                    i = i+1
        return i == 17

    def cmd(self):
        self.ajouter_Bateau(self.grille_J1, "Horizontale", (1, 1), "Porte-Avion")
        self.ajouter_Bateau(self.grille_J1, "Horizontale", (1, 2), "Croiseur")
        self.ajouter_Bateau(self.grille_J1, "Horizontale", (1, 3), "Contre-Torpilleur")
        self.ajouter_Bateau(self.grille_J1, "Horizontale", (1, 4), "Sous-marin")
        self.ajouter_Bateau(self.grille_J1, "Horizontale", (1, 5), "Torpilleur")

        self.tir(self.grille_J1, (1, 1))
        self.tir(self.grille_J1, (2, 1))
        self.tir(self.grille_J1, (3, 1))
        self.tir(self.grille_J1, (4, 1))
        self.tir(self.grille_J1, (5, 1))

        self.tir(self.grille_J1, (1, 2))
        self.tir(self.grille_J1, (2, 2))
        self.tir(self.grille_J1, (3, 2))
        self.tir(self.grille_J1, (4, 2))

        self.tir(self.grille_J1, (1, 3))
        self.tir(self.grille_J1, (2, 3))
        self.tir(self.grille_J1, (3, 3))

        self.tir(self.grille_J1, (1, 4))
        self.tir(self.grille_J1, (2, 4))
        self.tir(self.grille_J1, (3, 4))

        self.tir(self.grille_J1, (1, 5))
        self.tir(self.grille_J1, (2, 5))

        """direction = input("Veuillez entrer la direction du porte-avion : ")
        caseX = int(input("Veuillez selectionner la case(X) sur laquelle placer le porte-avion : "))
        caseY = int(input("Veuillez selectionner la case(Y) sur laquelle placer le porte-avion : "))
        self.ajouter_Bateau(self.grille_J1, direction, (caseX, caseY), "Porte-Avion")"""

    def selectBateau(self):
        pos = pygame.mouse.get_pos()
        l = len(list(self.bateauStr.keys()))
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

        if grille.getCaseByClick(pos[0], pos[1]) != None:
            cx = int(math.floor((pos[0] - grille.x) / ((abs(grille.x2 - grille.x) / grille.largeur))))
            cy = int(math.floor((pos[1] - grille.y) / ((abs(grille.y2 - grille.y) / grille.hauteur))))
            case = grille.getCaseByCoords(cx, cy)
            if case.getcontenu() != None:
                l = list(self.bateauStr.values())
                for i in range(len(l)):
                    for j in range(len(l[i])):
                        if case.contient(l[i][j]):
                            self.placeData[6] = i
                            cy = cy-j
                            for k in range(len(list(l[i]))):
                                grille.getCaseByCoords(cx, cy+k).setContenu(None)
                            break

                l = list(self.bateauStr_H.values())
                for i in range(len(l)):
                    for j in range(len(l[i])):
                        if case.contient(l[i][j]):
                            self.placeData[6] = i
                            cx = cx-j
                            for k in range(len(list(l[i]))):
                                grille.getCaseByCoords(cx+k, cy).setContenu(None)
                            break

    def placeBateau(self):
        pos = pygame.mouse.get_pos()
        grille = self.getGrille()
        if grille.getCaseByClick(pos[0], pos[1]) != None:
            cx = int(math.floor((pos[0] - grille.x) / ((abs(grille.x2 - grille.x) / grille.largeur))))
            cy = int(math.floor((pos[1] - grille.y) / ((abs(grille.y2 - grille.y) / grille.hauteur))))
            if self.ajouter_Bateau(grille, self.placeData[7][self.placeData[6]], (cx+1, cy+1), list(self.bateauStr.keys())[self.placeData[6]]):
                self.placeData[self.placeData[6]] = (-self.placeData[self.placeData[6]][0], -self.placeData[self.placeData[6]][1])
                self.placeData[6] = -1
        else:
            self.placeData[6] = -1

    def TournerBateau(self):
        if self.placeData[6] > -1:
            if self.placeData[7][self.placeData[6]] == "Verticale":
                self.placeData[7][self.placeData[6]] = "Horizontale"
            else:
                self.placeData[7][self.placeData[6]] = "Verticale"

    def getGrille(self):
        if self.data.etat == 11:
            return self.grille_J1 if self.placeData[5] == 1 else self.grille_J2
        elif self.data.etat == 12:
            return self.grille_J1 if self.currentPlayData[1] == 1 else self.grille_J2

    def playTir(self, case=(-1, -1)):
        grille = self.getGrille()
        caseT = grille.getSelectedCase()
        if caseT[0] == None and not(self.currentPlayData[0] == 2 and self.IA != None):
            return None
        self.tirTimer = 60
        self.tirData = [caseT[1]%grille.largeur, math.floor(caseT[1]/grille.largeur)] if case[0] < 0 or case[1] < 0 else [case[0], case[1]]
        if self.currentPlayData[0] == 1 and self.IA != None:
            self.currentPlayData[0] = 2

    def allBoatsPlaced(self):
        for i in range(5):
            if self.placeData[i][0] > 0 or self.placeData[i][1] > 0:
                return False
        return True

    def victoire(self,data):
        rayon = 4
        data.particules.addEmitter(FireWorkParticule.FireworkEmitter(data.particules, [Particule.Particule((100,100), 60, (230, 60, 60))], [(0, 235, 0), (0, 100, 0)], rayon, 60, (320, 480), (0, -4) , 0, 2))

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
                    self.data.setEtat("BN_End")
                    self.victoire(self.data)
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
            frame.blit(self.tirTexture, (grille.x + self.tirData[0] * case_Largeur, grille.y + self.tirData[1] * case_Hauteur))
            self.tirTimer = self.tirTimer-1
        else:
            self.tirTimer = self.tirTimer-1

        if menu != None:
            menu.draw(frame)
        pass
