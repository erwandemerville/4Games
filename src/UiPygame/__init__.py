import pygame
from pygame.locals import *

class Bouton(object):
    def __init__(self,x,y,width,height,border = 0,rgb_when_change = (0,0,0),text = "",rgb=(255,255,255),police = None,rgb_text = (0,0,0)):
        #Constructeur
        self.btn = pygame.Surface((width,height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        self.rgb_when_change = rgb_when_change
        self.text = text
        self.rgb = rgb
        self.rgb_text = rgb_text
        if(police != None):
            self.police = police
        else:
            self.police = pygame.font.SysFont('Impact',14)

    #Permet de dessiner le bouton dans une fenetre donnée
    def draw(self,frame):
        if(self.isCursorInRange() and self.rgb_when_change != None):
            self.btn.fill(self.rgb_when_change)
        else:
            self.btn.fill(self.rgb)
        if(self.border > 0):
            pygame.draw.rect(self.btn,(0,0,0),[0,0,self.width,self.height],self.border)
        text_on = self.police.render(self.text,True,self.rgb_text)
        self.btn.blit(text_on,(self.width/2 - text_on.get_width()/2,self.height/2 - text_on.get_height()/2))
        frame.blit(self.btn,(self.x,self.y))

    #Détermine si la souris est dans la surface du bouton
    def isCursorInRange(self):
        pos = pygame.mouse.get_pos()
        if((self.x+self.width > pos[0] > self.x)and(self.y+self.height > pos[1] > self.y)):
            return True
        return False

    def setText(self,text):
        self.text = text

    def getText(self):
        return self.text

    def update(self,frame):
        self.draw(frame)
        pygame.display.flip()

class Title():
    def __init__(self,x,y,width,height,border = 0,text = "",rgb=(255,255,255),police = None,rgb_text = (0,0,0)):
        #Constructeur
        self.btn = pygame.Surface((width,height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        self.text = text
        self.rgb = rgb
        self.rgb_text = rgb_text
        if(police != None):
            self.police = police
        else:
            self.police = pygame.font.SysFont('Impact',14)

    #Permet de dessiner le titre dans une fenetre donnée
    def draw(self,frame):
        if self.rgb != None:
            self.btn.fill(self.rgb)
        if(self.border > 0):
            pygame.draw.rect(self.btn,(0,0,0),[0,0,self.width,self.height],self.border)
        text_on = self.police.render(self.text,True,self.rgb_text)

        if self.rgb != None:
            self.btn.blit(text_on,(self.width/2 - text_on.get_width()/2,self.height/2 - text_on.get_height()/2))
            frame.blit(self.btn,(self.x,self.y))
        else:
            frame.blit(text_on,(self.x + self.width/2 - text_on.get_width()/2,self.y + self.height/2 - text_on.get_height()/2))

    def setText(self,text):
        self.text = text

    def getText(self):
        return self.text

class TextBox:
    "Classe permettant de gérer une boite ou écrire du texte"
    def __init__(self,x,y,width,height,border = 0,placeholder = "",rgb=(15,15,15), rgb_selected=(40,40,40),police = None,rgb_text = (255,255,255), rgb_placeholder = (128,128,128), rgb_border = (140,140,140), rgb_border_selected = (220,220,220), hideChar = None):
        #Constructeur
        self.selected = False
        self.btn = pygame.Surface((width,height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        self.rgb_border = rgb_border
        self.rgb_border_selected = rgb_border_selected
        self.placeholder = placeholder
        self.rgb_placeholder = rgb_placeholder
        self.text = ""
        self.hideChar = hideChar
        self.rgb = rgb
        self.rgb_selected = rgb_selected
        self.rgb_text = rgb_text
        self.button_pressed = False
        if(police != None):
            self.police = police
        else:
            self.police = pygame.font.SysFont('Impact',14)

    #Détermine si la souris est dans la surface du TextBox
    def isCursorInRange(self):
        pos = pygame.mouse.get_pos()
        return (self.x+self.width > pos[0] > self.x)and(self.y+self.height > pos[1] > self.y)

    #Actions a performer quand on clique
    def click(self):
        self.selected = self.isCursorInRange()

    #Actions a performer quand un bouton est pressé
    def keyDown(self, keys):
        if not self.button_pressed:
            if self.selected:
                shifted = keys[-3] == 1 or keys[-2] == 1 # On test si une des touches SHIFT est pressée
                if keys[-1] == 1: #Si la touche pressée est la touche pour effacer (BACKSPACE)
                    self.text = self.text[:-1]
                elif keys[-4] == 1: #Si la touche "M" est pressée

                    # Comme pygame est codé pour accepter les clavier QWERTY seulement,
                    # quelques conversions sont requises
                    self.text = self.text + 'm'
                else: # Sinon, on determine la touche via des boucles parcourant le tableau
                    isLetter = False
                    char = -1
                    for i in range(0, 26):
                        if (keys[i] == 1):
                            char = i
                            isLetter = True
                            break
                    if char == -1:
                        for i in range(26, 36):
                            if (keys[i] == 1):
                                char = i
                                break
                        for i in range(36, 46):
                            if (keys[i] == 1):
                                char = i
                                break

                    if char < 0:
                        return False

                    if isLetter: #Si une lettre est entrée
                        if shifted: # Si une touche SHIFT est pressée

                            # On converti la lettre entrée de minuscule vers majuscule.
                            # les chaines de caractère de Python 3.X sont encodées en UTF-8
                            # En UTF-8, les majuscules se trouvent 32 caractères avant les minuscules et dans le même ordre
                            # Ce qui fait que pour convertir une minuscule en majuscule, il suffit d'une soustraction
                            # Marche aussi avec l'encodage ASCII utilisé par python 2.X
                            char = char - 32
                        char = chr(ord('a')+char) # On determine la lettre entrée
                    else:
                        char = char - 26 # Un chiffre est entré, donc on peut passer les index des lettres
                        if char > 9: # Si le chiffre est tapé via le pad numérique
                            char = char - 10 # On le traite comme un chiffre normal
                        char = str(char) # Conversion du chiffre en String

                    # Comme pygame est codé pour accepter les clavier QWERTY seulement,
                    # quelques conversions sont requises
                    if char == 'a':
                        char = 'q'
                    elif char == 'w':
                        char = 'z'
                    elif char == 'z':
                        char = 'w'
                    elif char == 'q':
                        char = 'a'
                    elif char == 'm':
                        return False

                    self.text = self.text + char
            self.button_pressed = True
            return True

    #Actions a performer quand un bouton est relaché
    def keyUp(self):
        self.button_pressed = False

    #Fonction retournant le text contenu dans la TextBox
    def getText(self):
        return self.text

    #Permet de dessiner la TextBox dans une fenetre donnée
    def draw(self, frame):
        if self.rgb != None:
            if self.selected:
                self.btn.fill(self.rgb_selected)
            else:
                self.btn.fill(self.rgb)
        if(self.border > 0):
            if self.selected:
                pygame.draw.rect(self.btn,self.rgb_border_selected,[0,0,self.width,self.height],self.border)
            else:
                pygame.draw.rect(self.btn,self.rgb_border,[0,0,self.width,self.height],self.border)
        if self.text != "":
            if self.hideChar == None:
                text_on = self.police.render(self.text,True,self.rgb_text)
            else:
                hiddenText = ""
                for i in self.text:
                    hiddenText = hiddenText + self.hideChar
                text_on = self.police.render(hiddenText,True,self.rgb_text)
        else:
            text_on = self.police.render(self.placeholder,True,self.rgb_placeholder)
        self.btn.blit(text_on,(8,self.height/2 - text_on.get_height()/2))
        frame.blit(self.btn,(self.x,self.y))
