import sys
import pygame 
from pygame.locals import *
from path import *

class Enemy ():
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.path = [x, end]

        self.value = 3

        self.walkCount = 0
    
    def draw(self):
        self.move()

        if self.walkCount + 1 >= 30:
            self.walkCount = 0
        
        if self.value > 0:
            DISPLAYSURF.blit(walkRightEnemy[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            DISPLAYSURF.blit(walkLeftEnemy[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if self.value > 0:
            if self.x < self.path[1] + self.value:
                self.x += self.value
            else:
                self.value = self.value * -1
                self.x += self.value
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.value:
                self.x += self.value
            else:
                self.value = self.value * -1
                self.x += self.value
                self.walkCount = 0
