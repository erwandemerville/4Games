import os
from random import randint

import pygame

import LTO
import UiPygame as ui
import SubMenu
from Grille import Grille, Loto_Case
from UiPygame import Title


class Menu_LotoChoose(SubMenu.Menu_G):
    "Menu pause du Loto"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, frame.get_height()-120, frame.get_width()/2 - 40, 50, 2, (45, 45, 45),
                                    "Jouer avec ces grilles", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(frame.get_width()/2 + 20, frame.get_height()-120, frame.get_width() /2- 40, 50, 2, (45, 45, 45),
                                    "Changer de grilles", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(10, frame.get_height()-60, frame.get_width()/2 - 40, 50, 2, (45, 45, 45),
                                    "Ajouter une grille", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(frame.get_width()/2 + 20, frame.get_height()-60, frame.get_width()/2 - 40, 50, 2, (45, 45, 45),
                                    "Retirer une grille", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton((frame.get_width()/2)-150, frame.get_height()-185, 40, 40, 2, (45, 45, 45),
                                    "<", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton((frame.get_width()/2)+150, frame.get_height()-185, 40, 40, 2, (45, 45, 45),
                                    ">", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)
        self.pageGridToDraw = 0
        self.grillesToDraw = []
        self.addGrille();self.addGrille()
        for grille in self.grillesToDraw:
            LTO.Loto_Party.generateRandomContenuGrille(grille)

    @staticmethod
    def existInList(cont,value):
        for j in cont:
            if(j == value):
                return True
        return False

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            # Cas où il appuie sur "Lancer la partie"
            self.data.setEtat("Loto_Play")
            self.data.partie.start()
            self.data.partie.addGrillesToMainPlayer(self.grillesToDraw)
            self.data.nbInBoule = 0
        elif self.boutons[1].isCursorInRange():
            # Cas où il appuie sur "Changer de grilles"
            for grille in self.grillesToDraw:
                LTO.Loto_Party.generateRandomContenuGrille(grille)
        elif self.boutons[2].isCursorInRange():
            # Cas où on ajoute une grille
            self.addGrille()
        elif self.boutons[3].isCursorInRange():
            # Cas où en retire une grille
            self.removeLastGrilleAdded()
        elif self.boutons[4].isCursorInRange():
            # Cas où il appuie sur <
            self.pageGridToDraw = (self.pageGridToDraw-1)%(round(len(self.grillesToDraw)/2))
        elif self.boutons[5].isCursorInRange():
            # Cas où il appuie sur >
            self.pageGridToDraw = (self.pageGridToDraw+1)%(round(len(self.grillesToDraw)/2))
    def addGrille(self):
        if len(self.grillesToDraw) < 6:
            grille = Grille.Grille(9, 3, 0, 0, 300, 90, Loto_Case)
            LTO.Loto_Party.generateRandomContenuGrille(grille)
            self.grillesToDraw.append(grille)
        else:
            print("[ERROR] Cannot add another grille")
    def removeGrille(self,last):
        self.grillesToDraw.remove(last)
    def removeLastGrilleAdded(self):
        if len(self.grillesToDraw) > 2:
            self.grillesToDraw.pop(len(self.grillesToDraw)-1)
            if (len(self.grillesToDraw) % 2 == 0) and (len(self.grillesToDraw) < (self.pageGridToDraw+1)*2):
                self.pageGridToDraw = self.pageGridToDraw - 1
    def drawGrille(self,grille,frame,coord):
        surface = pygame.Surface((grille.x2,grille.y2))
        surface.fill((255,255,255))
        grille.draw(surface, (255, 0, 0))
        frame.blit(surface,coord)

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (0, 0, 0), (0, 0, frame.get_width(), frame.get_height()))
        #pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)
        self.boutons[2].draw(frame)
        self.boutons[3].draw(frame)
        if len(self.grillesToDraw) > 2:
            self.boutons[4].draw(frame)
            self.boutons[5].draw(frame)
        nb = 0
        buffer = [self.grillesToDraw[self.pageGridToDraw*2]]
        if(len(self.grillesToDraw) >= (self.pageGridToDraw+1)*2):
            buffer.append(self.grillesToDraw[self.pageGridToDraw*2+1])
        for grille in buffer:
            LTO.Loto_Party.removeAllJetonsS(grille)
            self.drawGrille(grille,frame,((frame.get_width()/2)-130,45+nb*130))
            nb = nb + 1

class Menu_LotoPlay(SubMenu.Menu_G):
    "Menu jeu du Loto"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, frame.get_height()-60, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Abandonner", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(10, frame.get_height()-120, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Bingo !", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(50, frame.get_height()-185, 40, 40, 2, (45, 45, 45),
                                    "<", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(280, frame.get_height()-185, 40, 40, 2, (45, 45, 45),
                                    ">", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)
        self.police19 = pygame.font.SysFont("Impact",19)
        self.police14 = pygame.font.SysFont("Impact",14)
        self.sizeBoule = round(frame.get_height() / 14)
        self.colorBackground = (0,0,0)
        self.titre = Title(20,5,frame.get_width()-40,45,2,"Lancement de la partie ...",(12, 12, 251),self.police25,(255,255,255))
        self.nbInBoule = 0
        self.frame = frame
        self.pageGridToDraw = 0
        self.linkImg = [(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets/loto/", "1.jpg")),
                        (os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets/loto/", "2.jpg")),
                        (os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets/loto/", "3.jpg")),
                        (os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets/loto/", "4.jpg"))]
        self.img = []
        for img in self.linkImg:
            self.img.append(pygame.image.load(img))
    def isCursorInRangeGrilles(self,grille,x,y):
        pos = pygame.mouse.get_pos();footX = 33;footY = 30
        for i in range(0,9):
            for j in range(0,3):
                if(x+grille.x+i*footX <= pos[0] <= x+grille.x+footX+i*footX):
                    if(y+grille.y+j*footY <= pos[1] <= y+grille.y+footY+j*footY):
                        return j*9+i
        return -1
    def click(self, frame):
        nb = 0
        buffer = [self.data.partie.grilles_mainplayer[self.pageGridToDraw*2]]
        if(len(self.data.partie.grilles_mainplayer) >= (self.pageGridToDraw+1)*2):
            buffer.append(self.data.partie.grilles_mainplayer[self.pageGridToDraw*2+1])
        for grille in buffer:
            value = self.isCursorInRangeGrilles(grille,40,90+110*nb)
            if(not(value==-1)):
                case = grille.getCase(value)
                if not(case==None):
                    if case.number > 0:
                        self.data.soundSystem.playSound("Jeton")
                        if case.jetonIn:
                            case.jetonIn = False
                        else:
                            case.jetonIn = True
            nb = nb + 1
        if self.boutons[0].isCursorInRange():
            # Cas où il apuuie sur "Abandon"
            self.data.setEtat("Loto_End")
            self.data.partie.stop()
            self.nbInBoule = 0
            self.data.soundSystem.playMusic("triste")
            self.data.partie.classements(False)
            del self.data.partie
            self.data.partie = None
        elif self.boutons[1].isCursorInRange():
            # Cas où il appuie sur bingo
            self.data.setEtat("Loto_End")
            self.data.soundSystem.playSound("Bingo")
            self.data.menus[10].asWin = self.data.partie.isMainPlayerWinner()
            if(not(self.data.getCurrentMenu().asWin)):
                self.data.soundSystem.playMusic("triste")
                self.data.partie.classements(False)
            else:
                self.data.partie.classements(True)
            self.nbInBoule = 0
            del self.data.partie
            self.data.partie = None
        elif self.boutons[2].isCursorInRange():
            # Cas où il appuie sur <
            self.pageGridToDraw = (self.pageGridToDraw-1)%(round(len(self.data.partie.grilles_mainplayer)/2))
        elif self.boutons[3].isCursorInRange():
            # Cas où il appuie sur >
            self.pageGridToDraw = (self.pageGridToDraw+1)%(round(len(self.data.partie.grilles_mainplayer)/2))

    def drawIA(self,frame,ia,x,y):
        surface = pygame.Surface((102,122))
        surface.fill((255,0,0))
        if ia.isWinner():
            text_on = self.police14.render("Bingo !",True,(12,255,12))
        else:
            text_on = self.police14.render(ia.nom,True,(255,255,255))
        surface.blit(self.img[ia.id], (1, 1, 100, 100))
        pygame.draw.rect(surface,(12,12,45),(1,101,100,120))
        surface.blit(text_on,(50 - text_on.get_width()/2 ,101))
        frame.blit(surface,(x,y))

    def drawBouleSortie(self,frame,value):
        surface = pygame.Surface((self.sizeBoule*2,self.sizeBoule*2))
        surface.fill(self.colorBackground)
        pygame.draw.circle(surface,(255,255,255),(self.sizeBoule,self.sizeBoule),self.sizeBoule)
        pygame.draw.circle(surface,(15,255,15),(self.sizeBoule,self.sizeBoule),self.sizeBoule-4)
        text_on = self.police.render(value,True,(255,255,255))
        surface.blit(text_on,(self.sizeBoule - text_on.get_width()/2,self.sizeBoule - text_on.get_height()/2))
        frame.blit(surface,(frame.get_width()-130,frame.get_height()-300))

    def drawGrille(self,grille,frame,coord):
        surface = pygame.Surface((grille.x2,grille.y2))
        surface.fill((255,255,255))
        grille.draw(surface, (255, 0, 0))
        frame.blit(surface,coord)

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, self.colorBackground, (0, 0, frame.get_width(), frame.get_height()))
        if(self.nbInBoule>0):
            self.drawBouleSortie(frame,str(self.nbInBoule))
        self.drawGrille(self.data.partie.grilles_mainplayer[self.pageGridToDraw*2],frame,(40,90))
        if(len(self.data.partie.grilles_mainplayer) >= (self.pageGridToDraw+1)*2):
            self.drawGrille(self.data.partie.grilles_mainplayer[self.pageGridToDraw*2+1],frame,(40,200))

        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)
        frame.blit(self.police14.render("Vos grilles", True, (255,255,255)),
                   (160,65))
        if len(self.data.partie.grilles_mainplayer) > 2:
            self.boutons[2].draw(frame)
            self.boutons[3].draw(frame)
        frame.blit(self.police14.render("Adversaires", True, (255,255,255)),
                   (386,65))
        self.drawIA(frame,self.data.partie.tab_IA[0],370,90)
        self.drawIA(frame,self.data.partie.tab_IA[1],370,220)
        self.titre.draw(frame)


class Menu_LotoEnd(SubMenu.Menu_G):
    "Menu de fin du Loto"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, frame.get_height()-100, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Retour au menu", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(10, frame.get_height()-160, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Rejouer", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)
        self.policeTitle = pygame.font.SysFont("Impact",80)
        self.titre = Title(20,20,frame.get_width()-40,50,2,"Fin de partie",(12, 12, 251),self.police,(255,255,255))
        self.asWin = False

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            # Cas où il appuie sur "Go to main"
            self.data.soundSystem.stopMusic("triste")
            self.data.setEtat("main")
        elif self.boutons[1].isCursorInRange():
            # Cas où il apupuie sur "Rejouer"
            self.data.partie = LTO.Loto_Party(frame, self.data)
            self.data.soundSystem.stopMusic("triste")
            self.data.setEtat("Loto_Choose")
            self.data.menus[9].nbInBoule = 0

    def draw(self, frame):
        frame.blit(self.data.fond,(0,0))
        pygame.draw.rect(frame, (70, 70, 70), (0, 0, frame.get_width(), frame.get_height()))
        #pygame.draw.rect(frame, (90, 90, 90), (470, 0, 170, 480))
        if(not(self.asWin)):
            self.titre.rgb = (0, 0, 0)
            self.titre.text = "Perdu !"
            frame.blit(self.policeTitle.render("Perdu !", True, (255,12,12)),
                       ((frame.get_width()/2)-self.policeTitle.size("Perdu !")[0]/2,frame.get_height()*0.3))
        else:
            self.titre.rgb = (12, 12, 251)
            self.titre.text = "Gagné !"
            frame.blit(self.policeTitle.render("Gagné !", True, (255,255,255)),
                       ((frame.get_width()/2)-self.policeTitle.size("Gagné !")[0]/2,frame.get_height()*0.3))
        self.titre.draw(frame)
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)
