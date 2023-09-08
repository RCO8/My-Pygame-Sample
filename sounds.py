import pygame

filepathS = 'C:/Users/Lenovo/Documents/pygame/sound/'

class SoundEffect():
    def __init__(self, filename):
        self.sound = pygame.mixer.music.load(filepathS+filename)
    def play(self, count=1):
        pygame.mixer.music.play(self.sound,count)

class BackgoundMusic(SoundEffect):
    def __init__(self, filename):
        super().__init__(filename)
        self.play(-1)