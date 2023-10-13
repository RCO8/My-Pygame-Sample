#필수 초기화
import pygame
import random
import bg_colors
from resources import ImageResources
from resources import BackgoundMusic

pygame.init()

#화면 크기
screen = pygame.display.set_mode((304,512))

#아이콘 설정
icon = ImageResources('enemy.png')
#pygame.display.set_icon(icon.sprite)

#FPS
clock = pygame.time.Clock()

#화면 타이틀
pygame.display.set_caption("피하기 게임")

#게임 폰트
game_font = pygame.font.Font(None, 40)

#게임 배경 및 이미지
background = ImageResources('astro.png')

player = ImageResources('agent.png')
player.setPosition(screen.get_width()/2-(player.sprite_width),screen.get_height() - player.sprite_height - 10)

enemy = ImageResources('rocket.png')
enemy.setPosition(random.randint(0,screen.get_width() - enemy.sprite_width),10)

bgSound = BackgoundMusic('Deltarune - MEGALOVANIA.mp3')

total_time = 10

def limit(left,top,x1,x2,y1,y2):
    if left < x1:
        left = x1
    elif left > x2:
        left = x2
    if top < y1:
        top = y1
    elif top > y2:
        top = y2
def level(start, div, speed, index):
    for i in index:
        if start > div * 1:
            speed = index[i]

xpos = 0
ypos = 0
avoidCount = 0
falling = 3

#이미지 그리기
def drawImage():
    screen.fill(bg_colors.bg_azure)
    screen.blit(background.sprite, (0,0))
    screen.blit(player.sprite, player.getPosition())
    screen.blit(enemy.sprite, enemy.getPosition())
pygame.joystick.init()

#게임 진행 루프
running = True
bgSound.play()
while running:
    #초당 지정된 프레임 횟수동안 동작
    dt = clock.tick(60)

    set_speed = 3
    #키보드 이벤트
    for event in pygame.event.get():
        #화면 창을 닫을 때
        if event.type == pygame.QUIT:
            pygame.time.delay(2000)
            running = False
        #키를 누르고 있을 때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xpos -= set_speed
            elif event.key == pygame.K_RIGHT:
                xpos += set_speed
            if event.key == pygame.K_UP:
                ypos -= set_speed
            elif event.key == pygame.K_DOWN:
                ypos += set_speed
        #키를 떼었을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xpos = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ypos = 0
            

    #게임 데이터 업데이트
    
    player.sprite_xpos += xpos
    player.sprite_ypos += ypos

    #화면 밖으로 못나가게 방지
    if player.sprite_xpos < 0:
        player.sprite_xpos = 0
    elif player.sprite_xpos > screen.get_width()-player.sprite_width:
        player.sprite_xpos = screen.get_width()-player.sprite_width
    if player.sprite_ypos < 0:
        player.sprite_ypos = 0
    elif player.sprite_ypos > screen.get_height()-player.sprite_height:
        player.sprite_ypos = screen.get_height()-player.sprite_height

    if enemy.sprite_ypos > screen.get_height():
        enemy.sprite_xpos = random.randint(0,screen.get_width() - enemy.sprite_width)
        enemy.sprite_ypos = 0 - enemy.sprite_height
        avoidCount += 1

    enemy.sprite_ypos += falling

    #충돌 설정
    player_rect = player.sprite.get_rect()
    player_rect.left = player.sprite_xpos
    player_rect.top = player.sprite_ypos

    enemy_rect = enemy.sprite.get_rect()
    enemy_rect.left = enemy.sprite_xpos
    enemy_rect.top = enemy.sprite_ypos

    drawImage()

    #카운터
    elapsed_time = (pygame.time.get_ticks()) / 1000
    timer = game_font.render("time : "+str(int(elapsed_time)),True,bg_colors.bg_white)
    screen.blit(timer,(screen.get_width()-timer.get_width()-10,10))
    
    if elapsed_time > 50:
        falling = 7
    elif elapsed_time > 25:
        falling = 5
    elif elapsed_time > 10:
        falling = 4

    #텍스트
    totalScore = game_font.render("score : "+str(avoidCount),True,bg_colors.bg_azure)
    screen.blit(totalScore,(10,10))
    
    #충돌 체크
    if player_rect.colliderect(enemy_rect):
        game_over = game_font.render("GAME OVER!!",True,bg_colors.bg_red)
        screen.blit(game_over,((screen.get_width() / 2) - (game_over.get_width() / 2),(screen.get_height()/2) - (game_over.get_height() / 2)))
        running = False
        pygame.time.delay(2000)

    #갱신
    pygame.display.update()

pygame.quit()