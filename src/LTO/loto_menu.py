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
                         [ui.Bouton(10, frame.get_height()-60, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Jouer avec ces grilles", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(50, frame.get_height()-140, frame.get_width() - 120, 50, 2, (45, 45, 45),
                                    "Changer de grilles", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)
        self.grilleToDraw1 = Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)
        self.grilleToDraw2 = Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)
        self.generateRandomContenuGrille(self.grilleToDraw1)
        self.generateRandomContenuGrille(self.grilleToDraw2)

    @staticmethod
    def existInList(cont,value):
        for j in cont:
            if(j == value):
                return True
        return False
    @staticmethod
    def generateRandomContenuGrille(grille):
        cont = [randint(1, 90)]
        for i in range(14):
            val = randint(1,90)
            while Menu_LotoChoose.existInList(cont, val):
                val = randint(1,90)
            cont.append(val)
        grille.fillByListNumeros(cont)

    def click(self, frame):
        if self.boutons[0].isCursorInRange():
            # Cas où il appuie sur "Lancer la partie"
            self.data.grilleToDraw1 = self.grilleToDraw1
            self.data.grilleToDraw2 = self.grilleToDraw2
            self.data.partie.addGrilleToMainPlayer(self.grilleToDraw1,self.grilleToDraw2)
            self.data.setEtat("Loto_Play")
            self.data.partie.start()
            self.data.nbInBoule = 0
        elif self.boutons[1].isCursorInRange():
            # Cas où il appuie sur "Changer de grilles"
            self.generateRandomContenuGrille(self.grilleToDraw1)
            self.generateRandomContenuGrille(self.grilleToDraw2)

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
        self.drawGrille(self.grilleToDraw1,frame,((frame.get_width()/2)-(self.grilleToDraw1.x2/2),50))
        self.drawGrille(self.grilleToDraw2,frame,((frame.get_width()/2)-(self.grilleToDraw2.x2/2),200))
        #self.grilleToDraw1.draw(frame, (255, 0, 0))

class Menu_LotoPlay(SubMenu.Menu_G):
    "Menu jeu du Loto"

    def __init__(self,data, frame):
        # Constructeur prenant la classe Data définie dans le main.py
        super().__init__(data,
                         [ui.Bouton(10, frame.get_height()-60, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Abandonner", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255)),
                          ui.Bouton(10, frame.get_height()-130, frame.get_width() - 20, 50, 2, (45, 45, 45),
                                    "Bingo !", (170, 170, 170), pygame.font.SysFont("Impact",27),(255,255,255))])
        self.police25 = pygame.font.SysFont('Impact',25)
        self.police = pygame.font.SysFont("Impact",27)
        self.police19 = pygame.font.SysFont("Impact",19)
        self.sizeBoule = round(frame.get_height() / 14)
        self.colorBackground = (0,0,0)
        self.grilleToDraw1 = Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)
        self.grilleToDraw2 = Grille.Grille(5, 3, 0, 0, 300, 90, Loto_Case)
        self.titre = Title(20,20,frame.get_width()-40,50,2,"Lancement de la partie ...",(12, 12, 251),self.police,(255,255,255))
        self.nbInBoule = 0
        self.frame = frame
    def isCursorInRangeGrilles(self,grille,x,y):
        pos = pygame.mouse.get_pos();footX = 60;footY = 30
        for i in range(0,5):
            for j in range(0,3):
                if(x+grille.x+i*footX <= pos[0] <= x+grille.x+footX+i*footX):
                    if(y+grille.y+j*footY <= pos[1] <= y+grille.y+footY+j*footY):
                        return j*5+i
        return -1
    def click(self, frame):
        value = self.isCursorInRangeGrilles(self.grilleToDraw1,40,90)
        if(not(value==-1)):
            case = self.grilleToDraw1.getCase(value)
            if not(case==None):
                if case.jetonIn:
                    case.jetonIn = False
                else:
                    case.jetonIn = True
        value2 = self.isCursorInRangeGrilles(self.grilleToDraw2,40,200)
        case2 = self.grilleToDraw2.getCase(value2)
        if(not(value2==-1)):
            if not(case2==None):
                if case2.jetonIn:
                    case2.jetonIn = False
                else:
                    case2.jetonIn = True

        if self.boutons[0].isCursorInRange():
            # Cas où il apuuie sur "Abandon"
            self.data.setEtat("Loto_End")
            self.data.partie.stop()
            self.nbInBoule = 0
            #self.data.soundSystem.playSound("rire")
            self.data.soundSystem.playMusic("triste")
        elif self.boutons[1].isCursorInRange():
            # Cas où il appuie sur bingo
            self.data.setEtat("Loto_End")
            self.data.menus[10].asWin = self.data.partie.isMainPlayerWinner()
            del self.data.partie
            self.data.partie = None
            if(not(self.data.getCurrentMenu().asWin)):
                self.data.soundSystem.playMusic("triste")
            self.nbInBoule = 0

    def drawIA(self,frame,ia,x,y):
        surface = pygame.Surface((100,100))
        surface.fill(self.colorBackground)
        if(ia.isWinner()):
            text_on = self.police19.render("Bingo!",True,(255,255,255))
        else:
            text_on = self.police19.render(ia.nom,True,(255,255,255))
        pygame.draw.circle(surface,(100,100,100),(50,20),20)
        pygame.draw.rect(surface,(12,12,45),(0,70,100,100))
        surface.blit(text_on,(50 - text_on.get_width()/2,80))
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
        self.drawGrille(self.grilleToDraw1,frame,(40,90))
        self.drawGrille(self.grilleToDraw2,frame,(40,200))
        self.boutons[0].draw(frame)
        self.boutons[1].draw(frame)
        self.drawIA(frame,self.data.partie.tab_IA[0],370,200)
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
