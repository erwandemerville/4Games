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

    def update(self,frame):
        self.draw(frame)
        pygame.display.flip()

#A ne pas utiliser, en construction xD
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

    #Permet de dessiner le bouton dans une fenetre donnée
    def draw(self,frame):
        self.btn.fill(self.rgb)
        if(self.border > 0):
            pygame.draw.rect(self.btn,(0,0,0),[0,0,self.width,self.height],self.border)
        text_on = self.police.render(self.text,True,self.rgb_text)
        self.btn.blit(text_on,(self.width/2 - text_on.get_width()/2,self.height/2 - text_on.get_height()/2))
        frame.blit(self.btn,(self.x,self.y))



    
