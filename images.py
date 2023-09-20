import pygame

filepath = 'sprite/'

class ImageResources:
    sprite_xpos = 0
    sprite_ypos = 0
    def __init__(self,filename):
        self.sprite = pygame.image.load(filepath+filename)
        self.sprite_size = self.sprite.get_rect().size
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()
        
    #def addonSprite(self):
        
    def setPosition(self,x,y):
        self.sprite_xpos = x
        self.sprite_ypos = y
        
    def jumpPosition(self,x,y):
        self.sprite_xpos += x
        self.sprite_ypos += y
        
    def getPosition(self):
        return (self.sprite_xpos,self.sprite_ypos)
        