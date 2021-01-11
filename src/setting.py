import sys
import pygame 
from pygame.locals import *
from path import *
from player import *
from enemy import *
from projectile import *
from bg import *

ninja = Ninja(0, 410, 100, 100)
bullets = []
obstacles = []

def endGame():
    global score

    obstacles = []

    runs = True
    while runs:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runs = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                runs = False

                ninja.left = False
                ninja.right = False
                ninja.isJump = False
                ninja.isProp = False
                ninja.standing = True
        
        largeFont = pygame.font.SysFont('comicsans', 80, True)
        currentScore = largeFont.render('Score: '+ str(score),1,RED)
        DISPLAYSURF.blit(currentScore, (WINDOWWIDTH/2 - currentScore.get_width()/2, 240))
        pygame.display.update()
    
    score = 0

def bull():
    global score

    for bullet in bullets:
        for obstacle in obstacles:
            if obstacle.visible:
                if bullet.hitbox[1] < obstacle.hitbox[1] + obstacle.hitbox[3] and bullet.hitbox[1] + bullet.hitbox[3] >  obstacle.hitbox[1]:
                    if bullet.hitbox[0] + bullet.hitbox[2] > obstacle.hitbox[0] and bullet.hitbox[0]< obstacle.hitbox[0] + obstacle.hitbox[2]:
                        hitSound.play()
                        obstacle.hit()
                        score += 1

                        if len(bullets) and obstacle:
                            bullets.pop(bullets.index(bullet))

        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.value
        else:
            bullets.pop(bullets.index(bullet))

def scores():
    fontScore = pygame.font.SysFont('comicsans', 30, True)
    textScore = fontScore.render("Score: " + str(score), 1, BLACK)
    
    fontHealth = pygame.font.SysFont('comicsans', 30, True)
    textHealth = fontHealth.render("Health: ", 1, YEALLOW)

    DISPLAYSURF.blit(textScore, (600, 10))
    DISPLAYSURF.blit(textHealth, (0, 10))

    pygame.display.update()

def redrawGameWindow(bgX, bgX2):    
    drawWindow(bgX, bgX2)
    
    ninja.draw()
    scores()

    for bullet in bullets:
        bullet.draw()

    for obstacle in obstacles:
        obstacle.draw()

    pygame.display.update()

def update(keys):

    global shootLoop, score

    for obstacle in obstacles:
        if obstacle.visible == True:
            if ((ninja.hitbox2[1] < obstacle.hitbox[1] + obstacle.hitbox[3] and ninja.hitbox2[1] + ninja.hitbox2[3] >  obstacle.hitbox[1])
                or 
                (ninja.hitbox3[1] < obstacle.hitbox[1] + obstacle.hitbox[3] and ninja.hitbox3[1] + ninja.hitbox3[3] >  obstacle.hitbox[1])
            ):
                if ((ninja.hitbox2[0] + ninja.hitbox2[2] > obstacle.hitbox[0] and ninja.hitbox2[0]< obstacle.hitbox[0] + obstacle.hitbox[2])
                    or 
                    (ninja.hitbox3[0] + ninja.hitbox3[2] > obstacle.hitbox[0] and ninja.hitbox3[0]< obstacle.hitbox[0] + obstacle.hitbox[2])
                ):
                    hitSound.play()
                    obstacle.hit()
                    score += 1

            if ninja.hitbox1[1] < obstacle.hitbox[1] + obstacle.hitbox[3] and ninja.hitbox1[1] + ninja.hitbox1[3] > obstacle.hitbox[1]:
                if ninja.hitbox1[0] + ninja.hitbox1[2] > obstacle.hitbox[0] and ninja.hitbox1[0] < obstacle.hitbox[0] + obstacle.hitbox[2]:
                    ninja.hit()
                    ninja.hitbox2 = (0, 0, 0, 0)
                    ninja.hitbox3 = (0, 0, 0, 0)
                    # score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 10:
        shootLoop = 0

    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()

        ninja.isProp = True
        ninja.standing = False

        if ninja.left:
            facing = -1
        else:
            facing = 1
        
        if len(bullets) < 20:
            bullets.append(projectile(
                round(ninja.x + 50), 
                round(ninja.y + 50),
                facing
            )) 

        shootLoop = 1 
    
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
        jumpSound.play()
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
    
    if ninja.visible == False:
            endGame()
