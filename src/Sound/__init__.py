import pygame
from pygame.mixer import Sound
import os
# Classe réalisée pour l'algorithmique et développement - L3
# Réalisation par BendoTV - 2019

# Classe gérant l'ensemble des sons de l'application
class SoundManager():
# un "sound" : son durant moins de 10s
# une "music" : son durant au moins 10s

    def __init__(self,data):
        self.data = data
        self.mx = pygame.mixer.init(48000,16,8)
        self.sound_link = {"rire": Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "rires.wav")),
                           "byebye": Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "Au revoir.wav"))}
        self.music_link = {"triste": Sound(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../assets", "tristitude.wav"))}

    # Joue un son avec sound, un élement de sound_link
    def playSound(self,sound):
        if(self.data.sound_active):
            son = self.sound_link[sound]
            son.set_volume(1)
            son.play()
    # Arrête un son avec sound, un élement de sound_link
    def stopSound(self,sound):
        if(self.data.sound_active):
            son = self.sound_link[sound]
            son.stop()
    # Joue une musique avec music, un élement de music_link
    def playMusic(self,music):
        if(self.data.music_active):
            son = self.music_link[music]
            son.set_volume(1)
            son.play()
    # Arrête une musique avec music, un élement de music_link
    def stopMusic(self,music):
        if(self.data.music_active):
            son = self.music_link[music]
            son.stop()
