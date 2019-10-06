import pygame
from pygame.locals import *

class Bouton(object):
    def __init__(self,x,y,width,height):
        #Constructeur
        self.btn = pygame.Surface((width,height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def draw(self,frame,rgb,text,rgb_text,police):
        #pygame.draw.rect(self.btn,rgb,self.btn.get_rect(),1)
        self.btn.fill(rgb)
        text = police.render(text,True,rgb_text)
        self.btn.blit(text,(self.width/2 - text.get_width()/2,self.height/2 - text.get_height()/2))
        frame.blit(self.btn,(self.x,self.y))

    def isCursorInRange(self):
        pos = pygame.mouse.get_pos()
        if((self.x+self.width > pos[0] > self.x)and(self.y+self.height > pos[1] > self.y)):
            return True
        return False
