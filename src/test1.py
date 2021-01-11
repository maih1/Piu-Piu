import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 400))

def collision(surface1, pos1, surface2, pos2):
    mask1 = pygame.mask.from_surface(surface1)
    mask2 = pygame.mask.from_surface(surface2)

    # print(type(mask1), mask2)
    x = pos2[0] - pos1[0]
    y = pos2[1] - pos1[1]
    if mask1.overlap(mask2, (x, y)) != None:
        return True
    return False

star1 = pygame.image.load('./data/img1/NINJA03GIF-0000.png') # Sao di chuyển
star1_pos = [0, 0] # Vị trí sao di chuyển
star2 = pygame.image.load('./data/imgEnemy/enemy1/1r.png') # Sao đứng yên
star2_pos = [50, 50] # Vị trí sao đứng yên

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill((0, 0, 0))

    star1_pos = pygame.mouse.get_pos() # Lấy vị trí của chuột

    DISPLAYSURF.blit(star2, star2_pos)
    DISPLAYSURF.blit(star1, star1_pos)
    if collision(star1, star1_pos, star2, star2_pos) == True:
        pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (50, 350, 300, 40))

    pygame.display.update()
    fpsClock.tick(FPS)