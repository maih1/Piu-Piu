import pygame
import sys
import time

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255,128,0)
unmellowyellow = (255,255,102)

gameDisplay = pygame.display.set_mode((display_width, display_height))  # screen : r 700px,d 800 px
pygame.display.set_caption("Flash Piu")  # title game
clock = pygame.time.Clock()

imgSetting = pygame.image.load("Image\settings (2).png")
def setting():
    gameDisplay.blit(imgSetting, (display_width * 0.85, display_height * 0.85))  # vẽ hình setting lên screen


imgVolume = pygame.image.load(r"Image\volume.png")
def volume():
    gameDisplay.blit(imgVolume, (display_width * 0.85, display_height * 0.7))


imgStart = pygame.image.load(r"Image\START.png")
def st():
    gameDisplay.blit(imgStart,(display_width * 0.35,display_height * 0.5))


imgStart2 = pygame.image.load(r"Image\start2.png")
def st2():
    gameDisplay.blit(imgStart2,(display_width * 0.35,display_height * 0.5))

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
        TextSur, TextRect = text_obj("PIU PIU", largeText)
        TextRect.center = ((display_width/2),(display_height * 0.3))
        gameDisplay.blit(TextSur, TextRect)

        setting()
        volume()

        #button
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if(280 + 191) > mouse[0] > 280 and 300 + 83 > mouse[1] > 300:
            st2()
            if click[0] == 1 and game_loop != None:
                game_loop()
        else:
            st()
        
        pygame.display.update()
        clock.tick(60)
        

#đối tượng chữ
def text_obj(text,font):
    textSur = font.render(text,True,orange)
    return textSur,textSur.get_rect()

#hiển thị chữ
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSur, TextRect = text_obj(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSur, TextRect)
    
    pygame.display.update()
    time.sleep(2)
    game_intro()


def crash():
    message_display("Game Over!")

#đối tượng chơi
#kích thước đối tượng
cat_width = 226
cat_height = 173

imgCat = pygame.image.load(r"Image\cat.png")
def cat(x,y):
    gameDisplay.blit(imgCat,(x,y))
# loop game
def game_loop():

    x = (display_width - cat_width) * 0.5 
    y = display_height - cat_height

    gameExit = False

    x_change = 0
    y_change = 0

    while not gameExit:
        # sự kiện game
        # tắt game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # bắt sự kiện
                pygame.quit()
                sys.quit()

            #di chuyển sự kiện 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            #khi thả di chuyển sự kiện
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        y += y_change

        gameDisplay.fill(unmellowyellow)
    
        cat(x,y)

        #xử lý khi va chạm vào thành của khung trò chơi
        if x > display_width - cat_width or x < 0:
            crash()
        if y > display_height - cat_height or y < 0:
            crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
game_intro()
pygame.quit()
sys.exit()
