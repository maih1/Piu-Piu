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

backgroud = pygame.image.load(paht_img + 'bg.png')
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
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.value = 5
        
        self.left = False
        self.right = False
        self.isJump = False

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
                # print(self.walkCount)

            elif self.right:
                DISPLAYSURF.blit(walkRight[self.walkCount // 3], (self.x,self.y))
                self.walkCount +=1
            elif self.isJump:
                DISPLAYSURF.blit(jump[self.walkCount // 5], (self.x, self.y))
                self.walkCount += 1
                print(self.walkCount)

        else:
            if self.right:
                DISPLAYSURF.blit(walkRight[0], (self.x, self.y))
            else:
                DISPLAYSURF.blit(walkLeft[0], (self.x, self.y))

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.value = 8 * facing

    def draw(self):
        pygame.draw.circle(DISPLAYSURF, self.color, (self.x,self.y), self.radius)

def redrawGameWindow():
    ninja.draw()
    pygame.display.update()

def update(key):
    if keys[pygame.K_LEFT] and ninja.x > ninja.value:
        ninja.x -= ninja.value
        ninja.left = True
        ninja.right = False
        ninja.standing = False
    elif keys[pygame.K_RIGHT] and ninja.x < 500 - ninja.width - ninja.value:
        ninja.x += ninja.value
        ninja.right = True
        ninja.left = False
        ninja.standing = False
    elif keys[pygame.K_SPACE]:
        ninja.standing = False
    else:
        ninja.standing = True
        ninja.walkCount = 0
        
    if not(ninja.isJump):
        if keys[pygame.K_SPACE]:
            ninja.isJump = True
            ninja.right = False
            ninja.left = False
    else:
        if ninja.jumpCount >= -10:
            ninja.y -= (ninja.jumpCount * abs(ninja.jumpCount)) * 0.5
            ninja.jumpCount -= 1
        else:
            ninja.isJump = False
            ninja.jumpCount = 10

ninja = Ninja(0, 400, 64, 64)
run = True

while run:
    fpsClock.tick(FPS)
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    update(keys)
    DISPLAYSURF.fill(WHITE)
    redrawGameWindow()

pygame.quit()
