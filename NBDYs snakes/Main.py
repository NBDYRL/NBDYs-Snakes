import pygame
import time
import random

snake_speed = 15

# Window size
WINDOW_X = 720
WINDOW_Y = 480

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

def RGB():
    '''Randomizes color input for snake body'''
    random_color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return random_color


# Initialising pygame
pygame.init()

#Initialise game window
pygame.display.set_caption('NBDYs Snakes')
game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

# FPS Controller
fps = pygame.time.Clock()

# Default position of snake
snake_position = [100, 50]

# body of snake, first four blocks
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]
# Position of fruit
fruit_position = [random.randrange(1, (WINDOW_X//10)) * 10,
                  random.randrange(1, (WINDOW_Y//10)) * 10]
fruit_spawn = True

# Snake spawn facing right
direction = 'RIGHT'
change_to = direction

# Starting score
score = 0

# Display for the score function
def show_score(choice, color, font, size):

    # Score font and size
    score_font = pygame.font.SysFont(font, size)

    # The display surface where the score will be shown
    score_surface = score_font.render('score : ' + str(score), True, color)

    # Creates a rectangular object for display surface
    score_rect = score_surface.get_rect()

    # Displays the text inside the rectangular surface
    game_window.blit(score_surface, score_rect)

# Game over function
def game_over():

    # Creating font for display screen
    my_font = pygame.font.SysFont('times new roman', 50)

    # Creates the surface on which the text will be displayed
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    # Creates a rectangular box for the text
    game_over_rect = game_over_surface.get_rect()

    # Display position on the screen
    game_over_rect.midtop = (WINDOW_X/2, WINDOW_Y/4)

    # Using blit to display to draw text on the screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Waits 2 seconds before closing the game
    time.sleep(2)

    # Closes the pygame library
    pygame.quit()

    # quits the program
    quit()


# Main function
while True:

    # Movement keys to change direction of snake
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Makes sure the snake can't hit itself if two opposite keys are pressed
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Snake movement
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism, if snake collides with fruit then score will be incremented by 10
    # Snake will also grow when collecting fruits
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        snake_speed += .8
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (WINDOW_X//10)) * 10,
                          random.randrange(1, (WINDOW_Y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, RGB(), pygame.Rect(
          pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(game_window, white, pygame.Rect(
      fruit_position[0], fruit_position[1], 10, 10))
 
    # Calls the game_over function if the snake hits the wall
    if snake_position[0] < 0 or snake_position[0] > WINDOW_X-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > WINDOW_Y-10:
        game_over()
     
    # Calls the game_over function when the snake hits itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
     
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20)
     
    # Refresh game screen
    pygame.display.update()
 
    # Game FPS
    fps.tick(snake_speed)
