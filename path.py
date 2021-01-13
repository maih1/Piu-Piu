import pygame 
from pygame.locals import *
import sys

pygame.init()

WINDOWWIDTH = 800 # Chiều dài cửa sổ
WINDOWHEIGHT = 600 # Chiều cao cửa sổ

WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)
RED    = (255,   0,   0)
BLUE   = (  0, 169, 191)
GREEN  = (11, 181, 56)
GREEN2 = (  0, 128,   0)
ORANGE = (255, 165,   0)
GOLD   = (255, 215,   0)
BROWN  = (139,  69,  19)
YEALLOW = (255, 174, 0)
UNMELLOWYELLOW = (255, 255, 102)
DARKYELLOW = (248,219,100)

### Xác định FPS ###
FPS = 60
fpsClock = pygame.time.Clock()

shootLoop = 0
score = 0

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Ninja piu piu')

pygame.time.set_timer(USEREVENT+2, 10000)

bulletSound = pygame.mixer.Sound('data/sounds/prop.wav')
hitSound = pygame.mixer.Sound('data/sounds/hit.wav')
jumpSound = pygame.mixer.Sound('data/sounds/jump.wav')
dieSound = pygame.mixer.Sound('data/sounds/die.wav')
botSound3 = pygame.mixer.Sound('data/sounds/bot3.wav')
botSound2 = pygame.mixer.Sound('data/sounds/bot2.wav')
botSound1 = pygame.mixer.Sound('data/sounds/bot1.wav')

pygame.mixer.music.load("data/sounds/mixkit-deep-urban-623.mp3")
pygame.mixer.music.play(-1)

bg = pygame.image.load("data/images/bg.png")
bgX = 0
bgX2 = bg.get_width()

paht_img = './data/img1/'
paht_img1 = './data/images/'
path_imgEnemy1 = './data/imgEnemy/enemy1/'
path_imgEnemy2 = './data/imgEnemy/enemy2/'
path_imgEnemy3 = './data/imgEnemy/enemy3/'

# char = pygame.image.load(paht_img + 'NINJA03GIF-0000.png')

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

slide = pygame.image.load(paht_img + 'slide.png')

die = pygame.image.load(paht_img + 'd5.png')

props = [
    pygame.image.load(paht_img + 'NINJA03GIF-0024.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0025.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0026.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0027.png'),
    pygame.image.load(paht_img + 'NINJA03GIF-0028.png'),
]

walkRightEnemy1 = [
    pygame.image.load(path_imgEnemy1 + '1r.png'),
    pygame.image.load(path_imgEnemy1 + '2r.png'),
    pygame.image.load(path_imgEnemy1 + '3r.png'),
    pygame.image.load(path_imgEnemy1 + '4r.png'),
    pygame.image.load(path_imgEnemy1 + '5r.png'), 
    pygame.image.load(path_imgEnemy1 + '6r.png'),
    pygame.image.load(path_imgEnemy1 + '7r.png'),
    pygame.image.load(path_imgEnemy1 + '8r.png'), 
    pygame.image.load(path_imgEnemy1 + '9r.png'),
]

walkLeftEnemy1 = [
    pygame.image.load(path_imgEnemy1 + '1.png'),
    pygame.image.load(path_imgEnemy1 + '2.png'),
    pygame.image.load(path_imgEnemy1 + '3.png'),
    pygame.image.load(path_imgEnemy1 + '4.png'),
    pygame.image.load(path_imgEnemy1 + '5.png'), 
    pygame.image.load(path_imgEnemy1 + '6.png'),
    pygame.image.load(path_imgEnemy1 + '7.png'),
    pygame.image.load(path_imgEnemy1 + '8.png'), 
    pygame.image.load(path_imgEnemy1 + '9.png'),
]

walkRightEnemy2 = [
    pygame.image.load(path_imgEnemy2 + '1r.png'),
    pygame.image.load(path_imgEnemy2 + '2r.png'),
    pygame.image.load(path_imgEnemy2 + '3r.png'),
    pygame.image.load(path_imgEnemy2 + '4r.png'),
    pygame.image.load(path_imgEnemy2 + '5r.png'), 
    pygame.image.load(path_imgEnemy2 + '6r.png'),
    pygame.image.load(path_imgEnemy2 + '7r.png'),
    pygame.image.load(path_imgEnemy2 + '8r.png'), 
]

walkLeftEnemy2 = [
    pygame.image.load(path_imgEnemy2 + '1.png'),
    pygame.image.load(path_imgEnemy2 + '2.png'),
    pygame.image.load(path_imgEnemy2 + '3.png'),
    pygame.image.load(path_imgEnemy2 + '4.png'),
    pygame.image.load(path_imgEnemy2 + '5.png'), 
    pygame.image.load(path_imgEnemy2 + '6.png'),
    pygame.image.load(path_imgEnemy2 + '7.png'),
    pygame.image.load(path_imgEnemy2 + '8.png'), 
]

walkRightEnemy3 = [
    pygame.image.load(path_imgEnemy3 + '1r.png'),
    pygame.image.load(path_imgEnemy3 + '2r.png'),
    pygame.image.load(path_imgEnemy3 + '3r.png'),
]

walkLeftEnemy3 = [
    pygame.image.load(path_imgEnemy3 + '1.png'),
    pygame.image.load(path_imgEnemy3 + '2.png'),
    pygame.image.load(path_imgEnemy3 + '3.png'),
]