import sys
import pygame 
from pygame.locals import *
from path import *
from game import*
from setting import*

run = True

while run:
    # fpsClock.tick(FPS)    
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    updateBg()

pygame.quit()