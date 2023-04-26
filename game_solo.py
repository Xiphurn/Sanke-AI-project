import pygame
import random
from statistics import mean


def start_game():

    nb_game = 1
    moyenne_score  = 0
    score_list = [0]
    
    pygame.init()
    
    #We define colors and font
    red = (255, 0,0 )
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 128, 0)
    myfont = pygame.font.Font(None, 36)

    #Define game window
    s = 1000
    size = (s, s)
    facteur = int((s/500))
    screen = pygame.display.set_mode(size)

    #Title
    pygame.display.set_caption("Snake")

    #Main loop configuration
    done = False
    clock = pygame.time.Clock()

    #Initial snake position and speed
    x = 240 * facteur
    y = 240 * facteur
    x_speed = 0
    y_speed = 0

    #Snake characteristics
    segment_width = 18 * facteur
    segment_height = (18 * facteur)
    segment_margin = (2 * facteur)
    segments = []
    segments.append([x, y])

    #Initial score
    score = 0
    
    #Initial apple
    apple_x = random.randrange(0, size[0]-(segment_width), (segment_width + segment_margin) )
    apple_y = random.randrange(0, size[1]-(segment_height ), (segment_height + segment_margin))

    #Main loop
    pygame.key.set_repeat(145,100)

    while not done:

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                        x_speed = -segment_width - segment_margin
                        y_speed = 0

                if event.key == pygame.K_RIGHT:
                        x_speed = segment_width + segment_margin
                        y_speed = 0

                if event.key == pygame.K_DOWN:   
                        x_speed = 0
                        y_speed = segment_height + segment_margin

                if event.key == pygame.K_UP:
                        x_speed = 0
                        y_speed = -segment_height - segment_margin
                        
                #Snake head displacement
                x += x_speed
                y += y_speed

                #Body displacement
                segments.append([x, y])

                #Delete last segment after displacement
                if len(segments) > score + 1:
                    del segments[0]

                #Eat apple
                if x == apple_x and y == apple_y:
                    apple_x = random.randrange(0, size[0]-segment_width, (segment_width + segment_margin))
                    apple_y = random.randrange(0, size[1]-segment_height, (segment_height + segment_margin))
                    score += 1
                    manger = True
                    #yield [score]
                else : 
                     manger = False
                     #yield [0, score, 1]

                #Management of collision with window edges
                if x < 0 or x > size[0]-segment_width or y < 0 or y > size[1] - segment_height:
                    done = True

                #Management of the collision with the snake's body
                for segment in segments[:-1]:
                    if segment == [x, y]:
                        done = True

                #Display of the game grid
                # for y_pos in range(0, size[1], segment_height + segment_margin):
                #     for x_pos in range(0, size[0], segment_width + segment_margin):
                #         pygame.draw.rect(screen, white, [x_pos, y_pos, segment_width, segment_height])

                #Information about food location
                if x < apple_x:
                    horizontal = "Right"
                    horizontal1 = 1 #Right"

                elif x > apple_x: 
                    horizontal = "Left"
                    horizontal1 = 2 #"Left"
                else:
                    horizontal = ""
                    horizontal1 = 3 #""

                if y < apple_y:
                    vertical = "Down"
                    vertical1 = 4 #"Down"
                elif y > apple_y:
                    vertical = "Up"
                    vertical1 = 5 #"Up"
                else:
                    vertical = ""
                    vertical1 = 6 #""
                
                distance1 = (((apple_x - x)**2) + ((apple_y - y)**2))**(1/2)
                
                #Wallpaper display
                screen.fill(black) 

                food_direction = myfont.render(f"Food : = {vertical} {horizontal}", True, (0,0,255))
                screen.blit(food_direction, (1, 50)) 
                
                distance = myfont.render(f"Distance : = {distance1} pxs", True, (0,0,255))
                screen.blit(distance, (1, 85)) 
                
                # moyenne = myfont.render(f"Moyenne score : = {moyenne_score} pts", True, (0,0,255))
                # screen.blit(moyenne, (1, 120)) 

                # maxi = myfont.render(f"Score max : = {max(score_list[0:])} pts", True, (0,0,255))
                # screen.blit(maxi, (1, 155)) 

                # game_num = myfont.render(f"Game # : {nb_game}", True, (0,0,255))
                # screen.blit(game_num, (1, 190)) 
               
                #Screen refresh speed
                clock.tick(20)

                if manger:
                     yield [distance1, 1, horizontal1, vertical1]
                else:
                     yield [distance1, 0, horizontal1, vertical1]
            
            #Display score
            scoretext = myfont.render(f"Score = {score}", True, (0,0,255))
            screen.blit(scoretext, (1, 15)) 
            
            #Display Apple 
            pygame.draw.rect(screen, red, [apple_x, apple_y, segment_width, segment_height])
                
            #Snake segments display
            for i, segment in enumerate(segments):
                if i == len(segments) - 1:
                    color = green
                else:
                    color = white
                    
                pygame.draw.rect(screen, color, [segment[0], segment[1], segment_width, segment_height ])            
            
            #Display update
            pygame.display.update()
      
    #Statistics on games played 
    score_list.append(score)
    moyenne_score = mean(score_list[1:])
        
    #Window close
    pygame.quit()
    return score_list


    