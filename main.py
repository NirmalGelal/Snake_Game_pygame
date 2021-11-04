import pygame
import time
import random

# initializing pygame
x = pygame.init()

screen_width = 900
screen_height = 600

# setting the size of game window
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#setting the title of the window
pygame.display.set_caption('Snake Game - Nirmal')
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
lightgreen = (153, 255, 51)

# game specific variables
exit_game = False
game_over = False
velocity_x = 0
velocity_y = 0
snake_x = 45
snake_y = 55
snake_size = 10
fps =  30
food_x = random.randint(20,screen_width/2)
food_y = random.randint(20,screen_height/2)
score = 0
clock = pygame.time.Clock()

#Gameover function
def gameover():
    gameWindow.fill(white)
    image1 = pygame.image.load('game-over.png')
    pygame.Surface.blit(gameWindow, image1,(10,10))
    pygame.display.update()
    time.sleep(2)
    # exit_game = False
    # pygame.quit()
    # quit()
    

# creating a game loop 
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_game = True
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0

            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = -10
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    if snake_x<=15 or snake_x>=880:
        velocity_x = 0
        velocity_y = 0
        gameover()
        break
    elif snake_y<=15 or snake_y>=580:
        velocity_y = 0
        velocity_x = 0
        gameover()
        break
    
    if abs(food_y-snake_y)<9 and abs(food_x-snake_x)<9:
        score+=1
        print('score: ',score)
        food_x = random.randint(20,screen_width/2)
        food_y = random.randint(20,screen_height/2)
        

    gameWindow.fill(lightgreen)
    pygame.draw.circle(gameWindow, red, (food_x,food_y), 7)
    pygame.draw.rect(gameWindow, black, [snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
