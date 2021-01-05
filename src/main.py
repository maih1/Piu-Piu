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
        self.x = 0 # Vị trí của xe
        self.y = 210

        ## Tạo surface và thêm hình chiếc xe vào ##
        self.surface = pygame.image.load('./data/img/ninja2.png')
    
    def draw(self): # Hàm dùng để vẽ xe
        DISPLAYSURF.blit(self.surface, (self.x, self.y))

    def update(self, moveLeft, moveRight, moveUp, moveDown, moveJump): # Hàm dùng để thay đổi vị trí xe
        if moveLeft == True:
            self.x -= 2
        if moveRight == True:
            self.x += 2
        if moveUp == True:
            self.y -= 2
        if moveDown == True:
            self.y += 2
        if moveJump == True:
            self.y -= 5
            self.x += 5
        
        if self.x + 50 > WINDOWWIDTH:
            self.x = WINDOWWIDTH - 50
        if self.x < 0:
            self.x = 0
        
        if self.y + 50 > WINDOWHEIGHT:
            self.y = WINDOWHEIGHT - 50
        if self.y < 0:
            self.y = 0

        # print (moveUp, moveDown)

Ninja = Ninja()

moveLeft = False
moveRight = False
moveUp = False
moveDown = False
moveJump = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
            elif event.key == pygame.K_RIGHT:
                moveRight = True
            elif event.key == pygame.K_UP:
                moveUp = True
            elif event.key == pygame.K_DOWN:
                moveDown = True
            elif event.key == pygame.K_SPACE:
                moveJump = True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
            elif event.key == pygame.K_RIGHT:
                moveRight = False  
            elif event.key == pygame.K_UP:
                moveUp = False
            elif event.key == pygame.K_DOWN:
                moveDown = False 
            elif event.key == pygame.K_SPACE:
                moveJump = False
              
    DISPLAYSURF.fill(WHITE)
    
    Ninja.draw()
    Ninja.update(moveLeft, moveRight, moveUp, moveDown, moveJump)

    pygame.display.update()
    fpsClock.tick(FPS)