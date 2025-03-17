import pygame
from pygame import mixer
from settings import *

class SoundManager:
    def __init__(self):
        mixer.init()
        self.sounds = {
            'eat': mixer.Sound('sounds/eat.wav'),
            'game_over': mixer.Sound('sounds/game_over.wav'),
            'background': mixer.Sound('sounds/background.wav')
        }
        self.set_volumes()
        
    def set_volumes(self):
        self.sounds['eat'].set_volume(0.7)
        self.sounds['game_over'].set_volume(0.8)
        self.sounds['background'].set_volume(0.2)
        
    def play(self, sound_name, loops=0):
        if sound_name in self.sounds:
            self.sounds[sound_name].play(loops=loops)
            
    def stop(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].stop()