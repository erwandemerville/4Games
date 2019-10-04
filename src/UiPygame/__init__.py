import pygame
from pygame.locals import *

class Bouton(object):
    def __init__(self,frame,x,y,width,height,rgb,text,rgb_text,police):
        #Constructeur
        self.btn = pygame.Surface((width,height))
        self.btn.fill(rgb)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        pygame.draw.rect(self.btn,rgb,self.btn.get_rect(),1)
        text = police.render(text,True,rgb_text)
        self.btn.blit(text,(width/2 - text.get_width()/2,height/2 - text.get_height()/2))
        frame.blit(self.btn,(x,y))


    def isCursorInRange(self):
        pos = pygame.mouse.get_pos()
        if((self.x+self.width > pos[0] > self.x)and(self.y+self.height > pos[1] > self.y)):
            return True
        return False
    
