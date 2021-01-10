import sys
import pygame 
from pygame.locals import *
from path import *

class Ninja():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.value = 5
        
        self.left = False
        self.right = False
        self.isJump = False
        self.isProp = False

        self.walkCount = 0
        self.jumpCount = 10

        self.standing = True

    def draw(self):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not(self.standing):
            if self.left:
                DISPLAYSURF.blit(walkLeft[self.walkCount // 3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                DISPLAYSURF.blit(walkRight[self.walkCount // 3], (self.x,self.y))
                self.walkCount +=1
            elif self.isJump:
                DISPLAYSURF.blit(jump[self.walkCount // 5], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                DISPLAYSURF.blit(walkLeft[0], (self.x, self.y))
            elif self.right:
                DISPLAYSURF.blit(walkRight[0], (self.x, self.y))
            else:
                DISPLAYSURF.blit(jump[0], (self.x, self.y))
