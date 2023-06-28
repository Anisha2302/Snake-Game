import pygame,time,random

pygame.init()

xlim = 1400
ylim = 700
color1 = (245, 237, 10)
color2 = (66, 22, 140)
red =  (255,0,0)
black = (0,0,0)
update_value=15
block=20                     # square dimension

clock = pygame.time.Clock()


gameWindow = pygame.display.set_mode((xlim,ylim))      # creates the window of size(800,600)
pygame.display.set_caption('snake game')               # title for the game
pygame.display.update()                                # updates all the logics written after

font = pygame.font.SysFont(None,50)                    # font is defined.

def message_to_screen(message,color):                  # function that prints message after game ends
    screen_text = font.render(message,True,color)
    gameWindow.blit(screen_text,(xlim/4,ylim/3))       # prints the message

def snake(block,snakelist):                            # for snake length increase.
    for XnY in snakelist:
        pygame.draw.rect(gameWindow,color2,(XnY[0],XnY[1],block,block))
            

def loop():

    update_x = 0
    update_y = 0
    start_x = float(xlim/2)
    start_y = float(ylim/2)
    gameclose = False
    gameover = False
    rAppleX = random.randrange(0,xlim-2*block)         # for creating random points for apple
    rAppleY = random.randrange(0,ylim-2*block)
    
    snakelist=[]
    snakelength=1
    
    while not gameclose:
        while gameover==True:
            gameWindow.fill(black)

            # quiting message   
            message_to_screen("You Lose!!!,Press r to replay or press q to quit.",red)
            pygame.display.update()
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_q:
                        gameclose=True
                        gameover=False
                    if event.key == pygame.K_r:
                        loop()

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                gameclose = True    

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    update_x = -update_value
                    update_y = 0
            
                if event.key == pygame.K_RIGHT:
                    update_x = update_value
                    update_y = 0
            
                if event.key == pygame.K_UP:
                    update_y = -update_value
                    update_x = 0
            
                if event.key == pygame.K_DOWN:
                    update_y = +update_value
                    update_x = 0                        
        
        # #boundary detect
        # if start_x>=xlim or start_x<0:               # if snake moves out of the window in left or right direction,then game exits
        #     gameover = True
        # if start_y>=ylim or start_y<0:               # if snake moves out of the window in up or down direction,then game exits
        #     gameover = True    
        
        if start_x>=xlim:
            start_x=0
        if start_x<0:
            start_x=xlim

        if start_y>=ylim:
            start_y=0
        if start_y<0:
            start_y=ylim    

        start_x = start_x +update_x
        start_y = start_y +update_y
        
        gameWindow.fill(color1)
        pygame.draw.rect(gameWindow,color2,(start_x,start_y,block,block))            # snake      
        pygame.draw.rect(gameWindow,red,(rAppleX,rAppleY,block,block))               # apple
        
        # for snake length increase:
        snakehead = []
        snakehead.append(start_x)
        snakehead.append(start_y)
        snakelist.append(snakehead)

        if len(snakelist)>snakelength:
            del (snakelist[0])

        for eachSegment in snakelist[:-1]:
            if eachSegment==snakehead:
                gameover=True
             
        snake(block,snakelist)

        pygame.display.update()                        
        
        if((start_x in range(rAppleX,rAppleX+block) and start_y in range(rAppleY,rAppleY+block)) or
           ((start_x+block) in range(rAppleX,rAppleX+block) and (start_y+block) in range(rAppleY,rAppleY+block))):    # snakes passes through apple 
           rAppleX = random.randrange(0,xlim-2*block)                                                                 # for creating new random points for apple
           rAppleY = random.randrange(0,ylim-2*block)

           snakelength = snakelength +1

        clock.tick(15)

    pygame.quit()
    quit()          


loop()    
