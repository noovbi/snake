import pygame
from pygame import mixer
from settings import *

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}

    def load_music(self, path):
        pygame.mixer.music.load(path)

    def play_music(self, loops=-1):
        pygame.mixer.music.play(loops)
        
    def play(self, sound_name, loops=0):
        if sound_name in self.sounds:
            self.sounds[sound_name].play(loops=loops)
            
    def stop(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].stop()

    def play_sound(self, name):
        self.sounds[name].play()