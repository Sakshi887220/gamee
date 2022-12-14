import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('')



clock = pygame.time.Clock()

block_size = 20
FPS = 15

direction = "right"

font = pygame.font.SysFont(None, 25)


def snake(block_size, snakelist):
    


def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color):
    textSurf, textRect = text_objects(msg, color)
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    textRect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    

    while not gameExit:

        while gameOver == True:
            

            for event in pygame.event.get():
                

                if event.type == pygame.KEYDOWN:
                    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        
        

        if len(snakeList) > snakeLength:
            del snakeList[0]

        

        snake(block_size, snakeList)

        pygame.display.update()

        ##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
        ##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
        ##                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
        ##                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
        ##                snakeLength += 1

        

        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()















