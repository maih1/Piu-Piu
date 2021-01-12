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

        self.hitbox = (self.x + 1.5, self.y + 12, 90, 57)
        
    def draw(self):
        prop = pygame.image.load(paht_img1 + 'prop.png')

        # if ninja.isProp:
        #     DISPLAYSURF.blit(props[ninja.walkCount // 5], (ninja.x, ninja.y))
        #     ninja.walkCount += 1

        DISPLAYSURF.blit(prop, (self.x, self.y))
        
        self.hitbox = (self.x + 1.5, self.y + 2, 21, 21)
        
        # pygame.draw.rect(DISPLAYSURF, (255,0,0), self.hitbox,2)