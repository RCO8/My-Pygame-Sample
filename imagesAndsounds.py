import pygame

filepath = 'C:/Users/Lenovo/Documents/pygame/sprite/'

class ImageResources:
    sprite_xpos = 0
    sprite_ypos = 0
    def __init__(self,filename):
        self.sprite = pygame.image.load(filename)
        self.sprite_size = self.sprite.get_rect().size
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()
    def setPosition(self,x,y):
        self.sprite_xpos = x
        self.sprite_ypos = y
    def getPosition(self):
        return (self.sprite_xpos,self.sprite_ypos)
        
filepathS = 'C:/Users/Lenovo/Documents/pygame/sound/'

class SoundEffect():
    def __init__(self, filename):
        self.sound = pygame.mixer.music.load(filepathS+filename)
    def play(self, count=1):
        pygame.mixer.music.play(self.sound,count)
    def stop():
        pygame.mixer.music.stop(self.sound.count)

class BackgoundMusic(SoundEffect):
    def __init__(self, filename):
        super().__init__(filename)
        self.play(-1)