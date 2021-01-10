import pygame
from pygame.locals import *
import sys

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255,165,0)
gold = (255,215,0)
brown = (139,69,19)
unmellowyellow = (255,255,102)

pygame.mixer.music.load("data/sounds/intro_Theme.wav")
pygame.mixer.music.play()

gameDisplay = pygame.display.set_mode((display_width, display_height))  # screen 
pygame.display.set_caption("Flash Piu")  # title game

clock = pygame.time.Clock()

bg = pygame.image.load("data/images/bg.png").convert()
bgX = 0
bgX2 = bg.get_width()

def drawWindow():
    gameDisplay.blit(bg,(bgX,0))
    gameDisplay.blit(bg,(bgX2,0))
    pygame.display.update()


imgSetting = pygame.image.load("data\images\settings (2).png")
def setting():
    gameDisplay.blit(imgSetting, (display_width * 0.85, display_height * 0.85))  # vẽ hình setting lên screen


imgVolume = pygame.image.load(r"data\images\volume.png")
def volume():

    gameDisplay.blit(imgVolume, (display_width * 0.85, display_height * 0.7))


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
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSur, TextRect)
    
    pygame.display.update()
    time.sleep(2)
    # game_intro()

#button cho hình khối
def game_button(te,x,y,c,d,bef,aft,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if(x + c) > mouse[0] > x and y + d > mouse[1] > y:
        pygame.draw.rect(gameDisplay,aft,(x,y,c,d))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,bef,(x,y,c,d))

    #vẽ chữ vào nút
    smallText = pygame.font.Font("freesansbold.ttf",30)
    textSur, textRect = text_obj(te, smallText,brown)
    textRect.center = ( (x+(c/2)), (y+(d/2)) )
    gameDisplay.blit(textSur, textRect)

#mở đầu của game
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        gameDisplay.fill(unmellowyellow)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSur, TextRect = text_obj("PIU PIU", largeText,orange)
        TextRect.center = ((display_width/2),(display_height * 0.3))
        gameDisplay.blit(TextSur, TextRect)

        setting()
        volume()

        #button
        game_button("Start",321,300,150,83,gold,orange,game_loop)

        image_button("data\images\volume.png",680,420,64,64)
        
        pygame.display.update()
       
        clock.tick(60)

        
def crash():
    message_display("Game Over!")


# loop game
def game_loop():
    
    
    global bgX,bgX2
    gameExit = False

    # x_change = 0
    # y_change = 0

    # vòng lặp game
    speed = 30
    while not gameExit:
        drawWindow()
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
            if event.type == USEREVENT +1:
                speed += 1
            #di chuyển sự kiện 
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         x_change = -5
            #     elif event.key == pygame.K_RIGHT:
            #         x_change = 5
            #     elif event.key == pygame.K_UP:
            #         y_change = -5
            #     elif event.key == pygame.K_DOWN:
            #         y_change = 5

            # #khi thả di chuyển sự kiện
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         x_change = 0

        # x += x_change
        # y += y_change

        # gameDisplay.fill(unmellowyellow)
    

        #xử lý khi va chạm vào thành của khung trò chơi
        # if x > display_width - cat_width or x < 0:
        #     crash()
        # if y > display_height - cat_height or y < 0:
        #     crash()

        # pygame.display.update()
        
        clock.tick(speed)
        

game_intro()
game_loop()
pygame.quit()
