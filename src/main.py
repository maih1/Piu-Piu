import pygame 
from pygame.locals import *
import sys

WINDOWWIDTH = 800 # Chiều dài cửa sổ
WINDOWHEIGHT = 600 # Chiều cao cửa sổ

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

pygame.init()

### Xác định FPS ###
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Ninja piu piu')

# self.surface = pygame.image.load('./data/img1/NINJA03GIF-0000.png')
paht_img = './data/img1/'

char = pygame.image.load(paht_img + 'NINJA03GIF-0000.png')

walkRight = [
    pygame.image.load(paht_img + 'NINJA03GIF-0007.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0008.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0009.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0010.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0011.png'), 
    pygame.image.load(paht_img + 'NINJA03GIF-0012.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0013.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0014.png'), 
    pygame.image.load(paht_img + 'NINJA03GIF-0015.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0016.png')
]

walkLeft = [
    pygame.image.load(paht_img + '0007.png'),
    pygame.image.load(paht_img + '0008.png'),
    pygame.image.load(paht_img + '0009.png'),
    pygame.image.load(paht_img + '0010.png'),
    pygame.image.load(paht_img + '0011.png'), 
    pygame.image.load(paht_img + '0012.png'),
    pygame.image.load(paht_img + '0013.png'),
    pygame.image.load(paht_img + '0014.png'), 
    pygame.image.load(paht_img + '0015.png'),
    pygame.image.load(paht_img + '0016.png')
]

jump = [
    pygame.image.load(paht_img + '0031.png'),
    pygame.image.load(paht_img + '0032.png'),
    pygame.image.load(paht_img + '0039.png'),
    pygame.image.load(paht_img + '0040.png'),
    pygame.image.load(paht_img + '0047.png'), 
    pygame.image.load(paht_img + '0048.png'),
]

class Ninja():
    def __init__(self):
        self.x = 0 # Vị trí 
        self.y = 400
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.moveJump = False
        self.jumpCount = 10
        self.walkCount = 0
        self.standing = True
        ## Tạo surface và thêm hình vào ##
        # 7 - 16 đi
        # 23 chem
        #  29 phi tieu
        # 54 nhay
        # 61 ngã
        # self.surface = pygame.image.load(paht_img + 'NINJA03GIF-0007.png')
    
    def draw(self): # Hàm dùng để vẽ
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if not (self.standing):
            if self.moveLeft:
                DISPLAYSURF.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.moveRight:
                DISPLAYSURF.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.moveJump:
                print(self.walkCount)
                DISPLAYSURF.blit(jump[self.walkCount // 5], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.moveLeft:
                DISPLAYSURF.blit(walkLeft[0], (self.x, self.y))
            if self.moveRight:
                DISPLAYSURF.blit(walkRight[0], (self.x, self.y))
        # DISPLAYSURF.blit(self.surface, (self.x, self.y))

    def update(self): # Hàm dùng để thay đổi vị trí

        if self.moveLeft:
            self.x -= 2
        if self.moveRight:
            self.x += 2

        if not self.moveJump:
            # if self.moveUp:
            #     self.y -= 2
            if self.moveDown:
                self.y += 2
        else:
            if self.jumpCount >= - 10:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else: 
                self.jumpCount = 10
                self.moveJump = False
                        
        if self.x + 100 > WINDOWWIDTH:
            self.x = WINDOWWIDTH - 100
        if self.x < 0:
            self.x = 0
        
        if self.y + 100 > WINDOWHEIGHT:
            self.y = WINDOWHEIGHT - 100
        if self.y < 0:
            self.y = 0

ninja = Ninja()

def redrawGameWindow():
    ninja.draw()
    ninja.update()

    pygame.display.update()

while True:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ninja.moveLeft = True
                ninja.standing = False
            if event.key == pygame.K_RIGHT:
                ninja.moveRight = True
                ninja.standing = False
            # if event.key == pygame.K_UP:
            #     ninja.moveUp = True
            if event.key == pygame.K_DOWN:
                ninja.standing = False
                ninja.moveDown = True
            if event.key == pygame.K_SPACE:
                ninja.standing = False
                ninja.moveJump = True
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ninja.standing = True
                ninja.moveLeft = False
            if event.key == pygame.K_RIGHT:
                ninja.standing = True
                ninja.moveRight = False  
            # if event.key == pygame.K_UP:
            #     ninja.moveUp = False
            if event.key == pygame.K_DOWN:
                ninja.standing = True
                ninja.moveDown = False 
            
    DISPLAYSURF.fill(WHITE)
    
    redrawGameWindow()

    fpsClock.tick(FPS)

