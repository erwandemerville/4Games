import pygame
from pygame.mixer import Sound


class SoundManager():

    def __init__(self,data):
        self.data = data
        self.mx = pygame.mixer.init(48000,16,8)
        self.sound_link = {"rire": Sound("assets/rires.wav"),
                           "byebye": Sound("assets/Au revoir.wav")}
        self.music_link = {"triste": Sound("assets/tristitude.wav")}

    def playSound(self,sound):
        if(self.data.sound_active):
            son = self.sound_link[sound]
            son.set_volume(1)
            son.play()
    def stopSound(self,sound):
        if(self.data.sound_active):
            son = self.sound_link[sound]
            son.stop()

    def playMusic(self,music):
        if(self.data.music_active):
            son = self.music_link[music]
            son.set_volume(1)
            son.play()
    def stopMusic(self,music):
        if(self.data.music_active):
            son = self.music_link[music]
            son.stop()