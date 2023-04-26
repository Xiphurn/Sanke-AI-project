import pygame
import random
from statistics import mean


class SnakeGame:

    pygame.init()

    #We define colors and font
    red = (255, 0,0 )
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 128, 0)
    myfont = pygame.font.Font(None, 36)

    #Main loop (à changer)
    pygame.key.set_repeat(145,100)

    def __init__(self, s) -> None:

        #Define game window
        self.s = s 
        self.size = (self.s, self.s)
        self.facteur = int((self.s/500))
        

        #Initial snake position and speed (ordre a vérifier)
        self.x = 240 * self.facteur
        self.y = 240 * self.facteur
        self.x_speed = 0
        self.y_speed = 0  

        #Snake characteristics
        self.segment_width = 18 * self.facteur
        self.segment_height = (18 * self.facteur)
        self.segment_margin = (2 * self.facteur)
        self.segments = []
        self.segments.append([self.x, self.y])

        #Initial apple
        self.apple_x = random.randrange(0, self.size[0]-self.segment_width, (self.segment_width + self.segment_margin) )
        self.apple_y = random.randrange(0, self.size[1]-self.segment_height, (self.segment_height + self.segment_margin))
      
        #Initial score
        self.score = 0  

        #Main loop configuration
        self.done = False 
        self.manger = False
        

        self.clock = pygame.time.Clock()
        #self.reset()

        self.screen = pygame.display.set_mode(self.size)
        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Snake")

        print("init effectué")



    def stat_game(self):
        
        #print("lancement game")

        while not self.done:
            #Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                elif event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_LEFT:
                            self.x_speed = -self.segment_width - self.segment_margin
                            self.y_speed = 0

                    if event.key == pygame.K_RIGHT:
                            self.x_speed = self.segment_width + self.segment_margin
                            self.y_speed = 0

                    if event.key == pygame.K_DOWN:   
                            self.x_speed = 0
                            self.y_speed = self.segment_height + self.segment_margin

                    if event.key == pygame.K_UP:
                            self.x_speed = 0
                            self.y_speed = -self.segment_height - self.segment_margin
                            
                    #Snake head displacement
                    self.x += self.x_speed
                    self.y += self.y_speed

                    #Body displacement
                    self.segments.append([self.x, self.y])

                    #Delete last segment after displacement
                    if len(self.segments) > self.score + 1:
                        del self.segments[0]

                    #Eat apple
                    if self.x == self.apple_x and self.y == self.apple_y:
                        self.apple_x = random.randrange(0, self.size[0]-self.segment_width, (self.segment_width + self.segment_margin))
                        self.apple_y = random.randrange(0, self.size[1]-self.segment_height, (self.segment_height + self.segment_margin))
                        self.score += 1
                        self.manger = True
                        #yield [score]
                    else : 
                        self.manger = False
                        #yield [0, score, 1]

                    #Management of collision with window edges
                    if self.x < 0 or self.x > self.size[0]-self.segment_width or self.y < 0 or self.y > self.size[1] - self.segment_height:
                        self.done = True

                    #Management of the collision with the snake's body
                    for segment in self.segments[:-1]:
                        if segment == [self.x, self.y]:
                            self.done = True

                #Display of the game grid
                # for y_pos in range(0, size[1], segment_height + segment_margin):
                #     for x_pos in range(0, size[0], segment_width + segment_margin):
                #         pygame.draw.rect(screen, white, [x_pos, y_pos, segment_width, segment_height])

                    #Information about food location
                    if self.x < self.apple_x:
                        self.horizontal = "Right"
                        self.horizontal1 = 1 #Right"

                    elif self.x > self.apple_x: 
                        self.horizontal = "Left"
                        self.horizontal1 = 2 #"Left"

                    else:
                        self.horizontal = ""
                        self.horizontal1 = 3 #""


                    if self.y < self.apple_y:
                        self.vertical = "Down"
                        self.vertical1 = 4 #"Down"

                    elif self.y > self.apple_y:
                        self.vertical = "Up"
                        self.vertical1 = 5 #"Up"
                    else:
                        self.vertical = ""
                        self.vertical1 = 6 #""
                    
                    self.distance1 = (((self.apple_x - self.x)**2) + ((self.apple_y - self.y)**2))**(1/2)


                    #Wallpaper display
                    self.screen.fill(self.black) 

                    self.food_direction = self.myfont.render(f"Food : = {self.vertical} {self.horizontal}", True, (0,0,255))
                    self.screen.blit(self.food_direction, (1, 50)) 
                    
                    self.distance = self.myfont.render(f"Distance : = {self.distance1} pxs", True, (0,0,255))
                    self.screen.blit(self.distance, (1, 85)) 

                    if self.manger:
                        return [self.distance1, 1, self.horizontal1, self.vertical1]
                    else:
                        return [self.distance1, 0, self.horizontal1, self.vertical1]
                
                # moyenne = myfont.render(f"Moyenne score : = {moyenne_score} pts", True, (0,0,255))
                # screen.blit(moyenne, (1, 120)) 

                # maxi = myfont.render(f"Score max : = {max(score_list[0:])} pts", True, (0,0,255))
                # screen.blit(maxi, (1, 155)) 

                # game_num = myfont.render(f"Game # : {nb_game}", True, (0,0,255))
                # screen.blit(game_num, (1, 190)) 
                
                #Screen refresh speed
                self.clock.tick(60)

                #Display score
                self.scoretext = self.myfont.render(f"Score = {self.score}", True, (0,0,255))
                self.screen.blit(self.scoretext, (1, 15)) 
                
                #Display Apple 
                pygame.draw.rect(self.screen, self.red, [self.apple_x, self.apple_y, self.segment_width, self.segment_height])
                    
                #Snake segments display
                for i, segment in enumerate(self.segments):
                    if i == len(self.segments) - 1:
                        self.color = self.green
                    else:
                        self.color = self.white
                        
                    pygame.draw.rect(self.screen, self.color, [segment[0], segment[1], self.segment_width, self.segment_height ])            


                #Display update
                pygame.display.update()



                

        #Window close
        pygame.quit()
