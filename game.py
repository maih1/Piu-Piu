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
    TextRect.center = ((WINDOWWIDTH/2),(WINDOWHEIGHT * 0.15))
    DISPLAYSURF.blit(TextSur, TextRect)

    drawController()
    drawVolume()

    #button

    image_button("data\images\volume.png",680,510,80,80)
    
    game_button("Start",312,160,150,83,GOLD,ORANGE, game, )

    
    # image_buttonH("data\images\bg_desert.png",680,510,64,64)
    pygame.display.update()
    DISPLAYSURF.fill(DARKYELLOW)
    
    
    
    