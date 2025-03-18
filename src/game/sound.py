import pygame
from settings import *

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            'eat': None,
            'game_over': None,
        }

    def load_sound(self, name, path):
        try:
            self.sounds[name] = pygame.mixer.Sound(path)
        except Exception as e:
            print(f"Error cargando sonido {name}: {str(e)}")
            self.sounds[name] = None

    def play_sound(self, name):
        if self.sounds.get(name):
            self.sounds[name].play()
        else:
            print(f"Sonido {name} no encontrado!")

    @staticmethod
    def load_music(path):
        pygame.mixer.music.load(path)

    @staticmethod
    def play_music(loops=-1):
        pygame.mixer.music.play(loops)

    def play(self, sound_name, loops=0):
        if sound_name in self.sounds:
            self.sounds[sound_name].play(loops=loops)

    def stop(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].stop()

    def play_sound(self, name):
        self.sounds[name].play()
