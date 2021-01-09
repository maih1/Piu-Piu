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
paht_img1 = './data/img/'
path_imgEnemy1 = './data/imgEnemy/enemy1/'
path_imgEnemy2 = './data/imgEnemy/enemy2/'


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
    pygame.image.load(paht_img + 'NINJA03GIF-0031.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0032.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0039.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0040.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0047.png'), 
    pygame.image.load(paht_img + 'NINJA03GIF-0048.png'),
]

props = [
    pygame.image.load(paht_img + 'NINJA03GIF-0024.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0025.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0026.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0027.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0028.png'),
]

walkRightEnemy = [
    pygame.image.load(path_imgEnemy1 + '1r.png'),
    pygame.image.load(path_imgEnemy1 + '2r.png'),
    pygame.image.load(path_imgEnemy1 + '3r.png'),
    pygame.image.load(path_imgEnemy1 + '4r.png'),
    pygame.image.load(path_imgEnemy1 + '5r.png'), 
    pygame.image.load(path_imgEnemy1 + '6r.png'),
    pygame.image.load(path_imgEnemy1 + '7r.png'),
    pygame.image.load(path_imgEnemy1 + '8r.png'), 
    pygame.image.load(path_imgEnemy1 + '9r.png'),
    pygame.image.load(path_imgEnemy1 + '10r.png')
]

walkLeftEnemy = [
    pygame.image.load(path_imgEnemy1 + '1.png'),
    pygame.image.load(path_imgEnemy1 + '2.png'),
    pygame.image.load(path_imgEnemy1 + '3.png'),
    pygame.image.load(path_imgEnemy1 + '4.png'),
    pygame.image.load(path_imgEnemy1 + '5.png'), 
    pygame.image.load(path_imgEnemy1 + '6.png'),
    pygame.image.load(path_imgEnemy1 + '7.png'),
    pygame.image.load(path_imgEnemy1 + '8.png'), 
    pygame.image.load(path_imgEnemy1 + '9.png'),
    pygame.image.load(path_imgEnemy1 + '10.png')
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

def bull(bullets):
    for bullet in bullets:
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.value
        else:
            bullets.pop(bullets.index(bullet))

def redrawGameWindow():
    ninja.draw()
    enemy.draw()

    for bullet in bullets:
        bullet.draw()
    
    pygame.display.update()

def update(keys, bullets):

    if keys[pygame.K_SPACE]:
        ninja.isProp = True
        ninja.standing = False

        if ninja.left:
            facing = -1
        else:
            facing = 1
        
        if len(bullets) < 100:
            bullets.append(projectile(
                round(ninja.x + 50), 
                round(ninja.y + 50),
                facing
            ))        

    if keys[pygame.K_LEFT] and ninja.x > ninja.value:
        ninja.x -= ninja.value
        ninja.left = True
        ninja.right = False
        ninja.isProp = False
        ninja.standing = False
    elif keys[pygame.K_RIGHT] and ninja.x < 800 - ninja.width - 50  - ninja.value:
        ninja.x += ninja.value
        ninja.right = True
        ninja.left = False
        ninja.isProp = False
        ninja.standing = False
    elif keys[pygame.K_UP]:
        ninja.standing = False
    else:
        ninja.standing = True
        ninja.walkCount = 0
        
    if not(ninja.isJump):
        if keys[pygame.K_UP]:
            ninja.isJump = True
            ninja.right = False
            ninja.left = False
            ninja.isProp = False    
    else:
        if ninja.jumpCount >= -10:
            ninja.y -= (ninja.jumpCount * abs(ninja.jumpCount)) * 0.5
            ninja.jumpCount -= 1
        else:
            ninja.isJump = False
            ninja.jumpCount = 10

ninja = Ninja(0, 400, 64, 64)
enemy = Enemy(0, 400, 64, 64, 700)
bullets = []

run = True

while run:
    fpsClock.tick(FPS)
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    bull(bullets)

    keys = pygame.key.get_pressed()

    update(keys, bullets)
    DISPLAYSURF.fill(WHITE)
    redrawGameWindow()

pygame.quit()
