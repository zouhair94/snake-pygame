#snake game

import pygame
import sys
import random
import time



try:
    
    check_error = pygame.init()

    if check_error[1] > 0 :
        print('there is an error in {0} .....!'.format(check_error[0]))
        sys.exit(-1)
    else:
        print('pygame initialized')




    #play surface
    play_surface = pygame.display.set_mode((720,460))
    #game caption 'title'
    pygame.display.set_caption('snake game')

    #color 

    red = pygame.Color(255,0,0)

    green = pygame.Color(0,255,0)

    black = pygame.Color(0,0,0)

    blue = pygame.Color(0,0,255)

    brown = pygame.Color(164,64,64)

    white = pygame.Color(255,255,255)

    #fps controller

    fps_controller = pygame.time.Clock()

    #game variables

    snake_pos = [100,50]
    snake_body = [[100,50],[90,50],[80,50]]

    food_pos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    food_spwan = True 

    change_to = 'RIGHT'
    direction = change_to

    score = 0 
    #game over function


    def gameOver():
        myFont = pygame.font.SysFont('monaco',72)
        GoSurface = myFont.render('Game over',True,red)
        goRect = GoSurface.get_rect()
        goRect.midtop = (360,15)
        play_surface.blit(GoSurface,goRect)
        pygame.display.flip()
        time.sleep(4)
        pygame.quit()
        sys.exit()


    
    #mail logic of game 

    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT or event.key == ord('d') :
                    change_to = 'RIGHT'
                if event.key == pygame.K_LEFT or event.key == ord('a') :
                    change_to = 'LEFT'
                if event.key == pygame.K_UP or event.key == ord('w') :
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == ord('s') :
                    change_to = 'DOWN'          
                if event.key == pygame.K_ESCAPE :
                    pygame.event.post(pygame.event.Event(QUIT))

            # positions
            if change_to == 'RIGHT' and not direction == 'LEFT':
                direction = 'RIGHT'
            if change_to == 'LEFT' and not direction == 'RIGHT':
                direction = 'LEFT'
            if change_to == 'UP' and not direction == 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and not direction == 'UP':
                direction = 'DOWN'
            
            #update snake position 

            if direction == 'RIGHT':
                snake_pos[0] += 10                          
            if direction == 'LEFT':
                snake_pos[0] -= 10 
            if direction == 'UP':
                snake_pos[1] -= 10 
            if direction == 'DOWN':
                snake_pos[1] += 10       

            #move snakes

            snake_body.insert(0,list(snake_pos))    
            if snake_pos[0] == food_pos[0] and   snake_pos[1] == food_pos[1] :
                score += 1
                food_spwan = False
            else:
                snake_body.pop()    

            if food_spwan == False:
                food_pos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
                food_spwan = True
            play_surface.fill(white)
            for pos in snake_body :
                
                pygame.draw.rect(play_surface,green,
                pygame.Rect(pos[0],pos[1],10,10))  
            pygame.draw.rect(play_surface,brown,
                pygame.Rect(food_pos[0],food_pos[1],10,10))    
            if snake_pos[0] > 720 or snake_pos[0] < 0 or  snake_pos[1] > 460 or snake_pos[1] < 0 :
                gameOver()
            for block in snake_body[1:]:
                if snake_pos[0] == block[0] and snake_pos[1] == block[1] :
                    gameOver()


            pygame.display.flip()
            fps_controller.tick(25)
            
        pygame.display.flip()     






except expression as identifier:
    print(expression)