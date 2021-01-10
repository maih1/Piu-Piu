import sys
sys.path.append('d:/python/Piu-Piu/src/module/')

import pygame 
from pygame.locals import *
from path import *
from player import *
from enemy import *
from projectile import *
from bg import *

ninja = Ninja(0, 400, 64, 64)
enemy = Enemy(0, 415, 64, 64, 700)

def bull(bullets):
    for bullet in bullets:
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.value
        else:
            bullets.pop(bullets.index(bullet))

def redrawGameWindow(bullets):
    
    drawWindow()
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