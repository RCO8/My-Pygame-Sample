from pygame import transform, image
from pygame import mixer
from pygame import Rect
class ImageResources:
    sprite_xpos = 0
    sprite_ypos = 0
    sprite_count = 0
    def __init__(self,filename):
        self.sprite = image.load('sprite/'+filename)
        self.sprite_size = self.sprite.get_rect().size
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()
        self.sprite_clip = Rect(0,0,self.sprite_width,self.sprite_height)
        self.sprite_direction = 0.0
    # 스프라이트를 해당 좌표로 이동
    def setPosition(self,x,y):
        self.sprite_xpos = x
        self.sprite_ypos = y
    # 스프라이트를 좌표만큼 이동
    def jumpPosition(self,x,y):
        self.sprite_xpos += x
        self.sprite_ypos += y
    # 스프라이트 회전
    def setRotation(self,dir):
        self.sprite_direction = dir
        self.sprite = transform.rotate(self.sprite, self.sprite_direction)
    def jumpRotation(self,dir):
        self.sprite_direction += dir
        self.sprite = transform.rotate(self.sprite, self.sprite_direction)
    # 스프라이트 확대축소
    def setScale(self,x,y):
        self.sprite = transform.scale(self.sprite,(self.sprite_width*x,self.sprite_height*y))
        #증감된 크기를 갱신
        self.sprite_width *= x
        self.sprite_height *= y
    def setScale(self,x):
        self.sprite = transform.scale(self.sprite,(self.sprite_width*x,self.sprite_height*x))
        self.sprite_width *= x
        self.sprite_height *= x

    #스프라이트 일부 출력
    def setClipping(self,x,y,w,h):
        self.sprite_clip = Rect(x,y,w,h)
        
    # 현재 좌표 반환
    def getPosition(self):
        return (self.sprite_xpos,self.sprite_ypos)
    # 현재 이미지 크기 반환
    def getSize(self):
        return (self.sprite_width,self.sprite_height)
        
class SoundResources():
    def __init__(self, filename):
        self.sound = mixer.music.load('sound/'+filename)
        self.nowVolume = mixer.music.get_volume()
    def play(self,cnt = 1):
        mixer.music.play(cnt)
    def stop(self,mode = 0):
        if mode == 0:
            mixer.music.pause()
        elif mode == 1:
            mixer.music.stop()
    def setVolume(self,fade):
        self.nowVolume += fade
        mixer.music.set_volume(self.nowVolume)

class BackgoundMusic(SoundResources):
    def __init__(self, filename):
        super().__init__(filename)
    # 여기서 필요한 메서드
    # 시간대 옮기기
    # 배속 증감
    
    # 점점 사라지게
    def fadeout(self):
        mixer.music.fadeout()