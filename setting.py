import sys
import random
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

def game():
    global bgX,bgX2, obstacles
    gameExit = False

    # vòng lặp game
    speed = 30

    while not gameExit:

        if not ninja.visible:
            obstacles.clear()
            endGame()

        
        #di chuyển nền cuộn 
        bgX -= 2
        bgX2 -= 2
        
        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()
        
        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()

        # tắt game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # bắt sự kiện
                gameExit = True
                pygame.quit()
                quit()
            
            if event.type == USEREVENT + 1:
                speed += 1
            
            if len(obstacles) == 0:
                obstacles.append(Enemy1(500, 425, 90, 76, 700))

            if event.type == USEREVENT + 2:
                ran = random.randrange(0,3)

                if ran == 0:
                    botSound1.play()
                    obstacles.append(Enemy1(500, 415, 90, 76, 700))
                elif ran == 1:
                    botSound2.play()
                    obstacles.append(Enemy2(100, 360, 90, 76, 700))
                elif ran == 2:
                    botSound3.play()
                    obstacles.append(Enemy3(600, 425, 90, 76, 700))        

        bull()

        keys = pygame.key.get_pressed()
        update(keys)

        redrawGameWindow(bgX, bgX2)

        fpsClock.tick(speed)

def endGame():    
    global score, speed

    speed = 30
    ninja.visible = True
    
    run = True

    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN: # if the user hits the mouse button
                run = False
                ninja.x = 0
                ninja.y = 410
                ninja.left = False
                ninja.right = False
                ninja.isJump = False
                ninja.isProp = False
                ninja.standing = True
                ninja.health = 20
                score = 0 

        # DISPLAYSURF.blit(bg, (0,0))    
        fontScore = pygame.font.SysFont('comicsans', 80, True)
        textScore = fontScore.render("Score: " + str(score), 1, RED)
        
        fontScoreBest = pygame.font.SysFont('comicsans', 80, True)
        textScoreBest = fontScoreBest.render("Best Score: " + str(updateFile()), 1, GREEN)

        DISPLAYSURF.blit(textScore, (WINDOWWIDTH/2 - textScore.get_width()/2, 240))
        DISPLAYSURF.blit(textScoreBest, (WINDOWWIDTH/2 - textScoreBest.get_width()/2,150))

        game_button("RERDY",321,300,150,83,GOLD,BLUE, game, )

        pygame.display.update()

def updateFile():
    f = open('scores.txt','r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score): 
        f.close() 
        file = open('scores.txt', 'w')
        file.write(str(score))
        file.close() 

        return score
               
    return last

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
                    dieSound.play()
                    ninja.hit()
                    ninja.hitbox2 = (0, 0, 0, 0)
                    ninja.hitbox3 = (0, 0, 0, 0)

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