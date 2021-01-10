import sys
import pygame 
from pygame.locals import *
from path import *

class projectile(object):
    def __init__(self,x,y,facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.value = 8 * facing

    def draw(self):
        prop = pygame.image.load(paht_img1 + 'prop.png')

        # if ninja.isProp:
        #     DISPLAYSURF.blit(props[ninja.walkCount // 5], (ninja.x, ninja.y))
        #     ninja.walkCount += 1

        DISPLAYSURF.blit(prop, (self.x, self.y))