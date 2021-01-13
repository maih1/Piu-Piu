import sys
import pygame 
from pygame.locals import *
from path import *
from player import *
from enemy import *
from projectile import *

# draw backgroud

def drawWindow(bgX, bgX2):
    DISPLAYSURF.blit(bg,(bgX,0))
    DISPLAYSURF.blit(bg,(bgX2,0))

#draw icon setting
# bghowTG = pygame.image.load("data/images/bg_desert.png")
# bghowTG = pygame.transform.scale(bghowTG,(WINDOWWIDTH,WINDOWHEIGHT))

def drawController():
    imgController = pygame.image.load("data\images\controller.png")
    imgController = pygame.transform.scale(imgController,(400,250))

    DISPLAYSURF.blit(imgController, (WINDOWWIDTH * 0.25, WINDOWHEIGHT /2 ))  # vẽ hình setting lên screen

# draw icon volume
def drawVolume():
    imgVolume = pygame.image.load("data\images\olume.png")
    imgVolume = pygame.transform.scale(imgVolume,(80,80))
    DISPLAYSURF.blit(imgVolume, (WINDOWWIDTH * 0.86, WINDOWHEIGHT * 0.85))

#button là ảnh
def image_button(img,x,y,c,d):
    pause = False
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if(x + c) > mouse[0] > x and y + d > mouse[1] > y:
        if click[0] == 1:
            if pause == False:
                pygame.mixer.music.pause()
                pause == True
            if pause == True:
                pygame.mixer.music.unpause()
                pause == False
    

#đối tượng chữ
def text_obj(text,font,color):
    textSur = font.render(text,True,color)
    return textSur,textSur.get_rect()

#hiển thị chữ
def message_display(text,color):
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSur, TextRect = text_obj(text, largeText,color)
    TextRect.center = ((WINDOWWIDTH /2),(WINDOWHEIGHT /2))
    DISPLAYSURF.blit(TextSur, TextRect)
    
    pygame.display.update()
    time.sleep(2)
    # game_intro()
    
#button cho hình khối
def game_button(te,x,y,c,d,bef,aft,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if(x + c) > mouse[0] > x and y + d > mouse[1] > y:
        pygame.draw.rect(DISPLAYSURF,aft,(x,y,c,d))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(DISPLAYSURF,bef,(x,y,c,d))

    #vẽ chữ vào nút
    smallText = pygame.font.Font("freesansbold.ttf",30)
    textSur, textRect = text_obj(te, smallText,BROWN)
    textRect.center = ( (x+(c/2)), (y+(d/2)) )
    DISPLAYSURF.blit(textSur, textRect)
