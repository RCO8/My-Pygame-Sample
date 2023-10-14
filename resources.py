import pygame

class ImageResources:
    sprite_xpos = 0
    sprite_ypos = 0
    def __init__(self,filename):
        self.sprite = pygame.image.load('sprite/'+filename)
        self.sprite_size = self.sprite.get_rect().size
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()
        
    #스프라이트 이미지 추가
    #스프라이트 회전처리
    
    # 스프라이트를 해당 좌표로 이동
    def setPosition(self,x,y):
        self.sprite_xpos = x
        self.sprite_ypos = y
    # 스프라이트를 좌표만큼 이동
    def jumpPosition(self,x,y):
        self.sprite_xpos += x
        self.sprite_ypos += y
    # 현재 좌표 반환
    def getPosition(self):
        return (self.sprite_xpos,self.sprite_ypos)
        
class SoundResources():
    def __init__(self, filename):
        self.sound = pygame.mixer.music.load('sound/'+filename)
        self.nowVolume = pygame.mixer.music.get_volume()
    def play(self,cnt = 1):
        pygame.mixer.music.play(cnt)
    def stop(self,mode = 0):
        if mode == 0:
            pygame.mixer.music.pause()
        elif mode == 1:
            pygame.mixer.music.stop()
    def setVolume(self,fade):
        self.nowVolume += fade
        pygame.mixer.music.set_volume(self.nowVolume)

class BackgoundMusic(SoundResources):
    def __init__(self, filename):
        super().__init__(filename)
        self.play()