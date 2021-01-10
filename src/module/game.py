import sys
import pygame 
from pygame.locals import *
from path import *
from player import *
from enemy import *
from projectile import *
from bg import *
from setting import *

bullets = []


def game():
    global bgX,bgX2
    gameExit = False

    # vòng lặp game
    speed = 30
    while not gameExit:
        redrawGameWindow(bullets)
        
        #di chuyển nền cuộn 
        bgX -= 2
        bgX2 -= 2

        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()
        
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()

        # tắt game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # bắt sự kiện
                gameExit = True
                pygame.quit()
                quit()
            if event.type == USEREVENT +1:
                speed += 1
        

        bull(bullets)

        keys = pygame.key.get_pressed()

        update(keys, bullets)

        fpsClock.tick(speed)

def updateBg():

    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSur, TextRect = text_obj("PIU PIU", largeText,ORANGE)
    TextRect.center = ((WINDOWWIDTH/2),(WINDOWHEIGHT * 0.3))
    DISPLAYSURF.blit(TextSur, TextRect)

    drawSetting()
    drawVolume()

    #button
    game_button("Start",321,300,150,83,GOLD,ORANGE, game, )

    image_button("data\images\volume.png",680,420,64,64)
    
    pygame.display.update()

    
    DISPLAYSURF.fill(WHITE)
    