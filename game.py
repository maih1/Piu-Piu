import sys
import pygame 
from pygame.locals import *
from path import *
from player import *
from enemy import *
from projectile import *
from bg import *
from setting import *

def updateBg():

    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSur, TextRect = text_obj("PIU PIU", largeText,ORANGE)
    TextRect.center = ((WINDOWWIDTH/2),(WINDOWHEIGHT * 0.3))
    DISPLAYSURF.blit(TextSur, TextRect)

    drawSetting()
    drawVolume()

    #button

    image_button("data\images\volume.png",680,420,64,64)
    game_button("Start",321,300,150,83,GOLD,ORANGE, game, )

    pygame.display.update()

    
    DISPLAYSURF.fill(WHITE)
    