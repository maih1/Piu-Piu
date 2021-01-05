import pygame 
from pygame.locals import *
import sys

WINDOWWIDTH = 400 # Chiều dài cửa sổ
WINDOWHEIGHT = 300 # Chiều cao cửa sổ

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

pygame.init()

### Xác định FPS ###
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Ninja piu piu')

class Ninja():
    def __init__(self):
        self.x = 0 # Vị trí 
        self.y = 210
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.moveJump = False
        self.jumpCount = 6

        ## Tạo surface và thêm hình vào ##
        self.surface = pygame.image.load('./data/img/ninja2.png')
    
    def draw(self): # Hàm dùng để vẽ
        DISPLAYSURF.blit(self.surface, (self.x, self.y))

    def update(self): # Hàm dùng để thay đổi vị trí

        if self.moveLeft:
            self.x -= 2
        if self.moveRight:
            self.x += 2

        if not self.moveJump:
            if self.moveUp:
                self.y -= 2
            if self.moveDown:
                self.y += 2
        else:
            if self.jumpCount >= - 6:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else: 
                self.jumpCount = 6
                self.moveJump = False
                        
        if self.x + 50 > WINDOWWIDTH:
            self.x = WINDOWWIDTH - 50
        if self.x < 0:
            self.x = 0
        
        if self.y + 50 > WINDOWHEIGHT:
            self.y = WINDOWHEIGHT - 50
        if self.y < 0:
            self.y = 0

Ninja = Ninja()

while True:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Ninja.moveLeft = True
            if event.key == pygame.K_RIGHT:
                Ninja.moveRight = True
            if event.key == pygame.K_UP:
                Ninja.moveUp = True
            if event.key == pygame.K_DOWN:
                Ninja.moveDown = True
            if event.key == pygame.K_SPACE:
                Ninja.moveJump = True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Ninja.moveLeft = False
            if event.key == pygame.K_RIGHT:
                Ninja.moveRight = False  
            if event.key == pygame.K_UP:
                Ninja.moveUp = False
            if event.key == pygame.K_DOWN:
                Ninja.moveDown = False 
            
    DISPLAYSURF.fill(WHITE)
    
    Ninja.draw()
    Ninja.update()

    pygame.display.update()
    fpsClock.tick(FPS)