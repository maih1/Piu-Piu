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
    
        self.hitbox = (self.x + 1.5, self.y + 12, 90, 57)
        self.health = 10
        self.visible = True

    def draw(self):
        self.move()

        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            
            if self.value > 0:
                DISPLAYSURF.blit(walkRightEnemy[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                DISPLAYSURF.blit(walkLeftEnemy[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            
            pygame.draw.rect(DISPLAYSURF, RED, (self.hitbox[0] + 20, self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(DISPLAYSURF, GREEN2, (self.hitbox[0] + 20, self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 1.5, self.y + 12, 90, 57) #  12 57
            pygame.draw.rect(DISPLAYSURF, (255,0,0), self.hitbox,2)

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

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
