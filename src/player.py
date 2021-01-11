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

        self.hitbox1 = (self.x + 19, self.y + 28, 70, 50)
        self.hitbox2 = (0,0,0,0)
        self.hitbox3 = (0,0,0,0)
        self.health = 20
        self.visible = True

    def draw(self):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                DISPLAYSURF.blit(walkLeft[self.walkCount // 3], (self.x,self.y))
                self.hitbox3 = (self.x + 10, self.y + 35, 25, 30)
                self.hitbox2 = (0, 0, 0, 0)
                # pygame.draw.rect(DISPLAYSURF, BROWN, self.hitbox3, 2)
                self.walkCount += 1
            elif self.right:
                DISPLAYSURF.blit(walkRight[self.walkCount // 3], (self.x,self.y))
                self.hitbox2 = (self.x + 64, self.y + 35, 29, 30)
                self.hitbox3 = (0, 0, 0, 0)
                # pygame.draw.rect(DISPLAYSURF, GREEN2, self.hitbox2, 2)
                self.walkCount +=1
            elif self.isJump:
                DISPLAYSURF.blit(jump[self.walkCount // 5], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                DISPLAYSURF.blit(walkLeft[0], (self.x, self.y))
                # self.hitbox3 = (self.x + 10, self.y + 35, 25, 30)
                # pygame.draw.rect(DISPLAYSURF, BROWN, self.hitbox3, 2)
            elif self.right:
                DISPLAYSURF.blit(walkRight[0], (self.x, self.y))
                # self.hitbox2 = (self.x + 64, self.y + 35, 29, 30)
                # pygame.draw.rect(DISPLAYSURF, GREEN2, self.hitbox2, 2)
            else:
                DISPLAYSURF.blit(jump[0], (self.x, self.y))

        
        pygame.draw.rect(DISPLAYSURF, RED, (self.x - self.x + 100, self.y - self.y + 10, 100, 20))
        pygame.draw.rect(DISPLAYSURF, GREEN2, (self.x - self.x + 100, self.y - self.y + 10, 100 - (5 * (20 - self.health)), 20))

        self.hitbox1 = (self.x + 19, self.y + 28, 50, 50)
        # self.hitbox2 = (self.x + 64, self.y + 35, 29, 30)
        # self.hitbox3 = (self.x + 10, self.y + 35, 25, 30)

        # pygame.draw.rect(DISPLAYSURF, RED, self.hitbox1, 2)
        # pygame.draw.rect(DISPLAYSURF, GREEN2, self.hitbox2, 2)
        # pygame.draw.rect(DISPLAYSURF, BROWN, self.hitbox3, 2)

    def hit(self):
        if self.health > 0:
            self.health -= 1

            self.isJump = False
            self.jumpCount = 10
            self.x = 0
            self.y = 400
            self.walkCount = 0

            i = 0
            
            while i < 21:
                # pygame.time.delay(5)

                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 201
                        pygame.quit()
        else:
            self.visible = False

    def die():
        DISPLAYSURF.blit(die, (self.x, self.y))