__author__="Antigoni-k"
__description__="Simple snake game using pygame. Please install pygame (pip install pygame on Command Prompt) to play the game."

import pygame
import time
import os
import random
import sys


pygame.init()

#Screen resolution
screenwidth,screenheight=500, 500
screen=pygame.display.set_mode((screenwidth,screenheight))
#Window caption and font style
pygame.display.set_caption("Snake Game")
font_style=pygame.font.SysFont("bahnschrift", 25)


#Clock initialization
clock=pygame.time.Clock()
#Initialization of snake's and food's single segment size
block=10
#Initialization of lives
lives=3



def Snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, "green", [x[0], x[1], block, block])

def Message(msg):
    mesg=font_style.render(msg, True, "black")
    screen.blit(mesg, [10, 220])

def Score(score):
    scorevalue=font_style.render("Score: "+ str(score), True, "black")
    screen.blit(scorevalue, [0,0])

def Lives(lives):
    livesvalue=font_style.render("Lives: "+ str(lives), True, "black")
    screen.blit(livesvalue, [screenwidth-90,0])
    if lives==0:
        return False



#Main Game  
def gameloop():
    global lives, lengthofsnake
    snake_speed=15
    loss=False
    running=True

    #Snake's initial position
    x2=screenwidth/2
    y=screenheight/2
    #Snake's movements / coordinations
    xchange=0
    ychange=0
    
    snake_list=[]
    lengthofsnake=1

    foodx=round(random.randrange(0, screenwidth-block)/10.0)*10.0
    foody=round(random.randrange(0, screenheight-block)/10.0)*10.0
    blockx=round(random.randrange(0, screenwidth-block)/10.0)*10.0
    blocky=round(random.randrange(0, screenheight-block)/10.0)*10.0

    while not loss and lives>0:
        #Loss and Game Over
        while running==False:
            screen.fill("pink")
            if Lives(lives - 1)==False:
                Message("Game Over! Press ESC to quit.")
            else:
                Message("Press 'C' to play again or press ESC to quit.")
            Score(lengthofsnake - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        loss=True
                        running=True
                    if event.key==pygame.K_c:
                        lives-=1
                        gameloop()

        #Key Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loss = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xchange = -block
                    ychange = 0
                elif event.key == pygame.K_RIGHT:
                    xchange = block
                    ychange = 0
                elif event.key == pygame.K_UP:
                    ychange = -block
                    xchange = 0
                elif event.key == pygame.K_DOWN:
                    ychange = block
                    xchange = 0

        #Screen limits            
        if x2>=screenwidth or x2<0 or y>=screenheight or y<0:
            running=False
        x2+=xchange
        y+=ychange

        #Background color
        screen.fill("pink")
        #Food segment
        pygame.draw.rect(screen, "red", [foodx, foody, block, block])

        #Snake's body
        snakehead=[]
        snakehead.append(x2)
        snakehead.append(y)
        snake_list.append(snakehead)

        if len(snake_list)>lengthofsnake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snakehead:
                running=False
                
        Snake(block, snake_list)
        Score(lengthofsnake-1)
        Lives(lives)
        pygame.display.update()

        #Food spawning
        if x2==foodx and y==foody:
                foodx = round(random.randrange(0, screenwidth - block) / 10.0) * 10.0
                foody = round(random.randrange(0, screenheight - block) / 10.0) * 10.0
                lengthofsnake += 1
        
        if x2==blockx and y==blocky:
            running=False
            
        clock.tick(snake_speed)
    pygame.quit()
    sys.exit()


gameloop()
