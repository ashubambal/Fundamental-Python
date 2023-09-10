import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SNAKE_SPEED = 10

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction
score = 0

# Food variables
food_pos = [random.randrange(1, GRID_WIDTH) * GRID_SIZE,
            random.randrange(1, GRID_HEIGHT) * GRID_SIZE]
food_spawn = True

# Game Over flag
game_over = False

# Game over function
def game_over_screen():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Your Score is: ' + str(score), True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH/2, HEIGHT/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.quit()
    sys.exit()

# Main game loop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Change direction according to user input
    if change_to == 'UP' and not snake_direction == 'DOWN':
        snake_direction = 'UP'
    if change_to == 'DOWN' and not snake_direction == 'UP':
        snake_direction = 'DOWN'
    if change_to == 'LEFT' and not snake_direction == 'RIGHT':
        snake_direction = 'LEFT'
    if change_to == 'RIGHT' and not snake_direction == 'LEFT':
        snake_direction = 'RIGHT'

    # Move the snake
    if snake_direction == 'UP':
        snake_pos[1] -= GRID_SIZE
    if snake_direction == 'DOWN':
        snake_pos[1] += GRID_SIZE
    if snake_direction == 'LEFT':
        snake_pos[0] -= GRID_SIZE
    if snake_direction == 'RIGHT':
        snake_pos[0] += GRID_SIZE

    # Snake body growing mechanism
    # If food and snake collide, scores incremented by 10
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()
    
    if not food_spawn:
        food_pos = [random.randrange(1, GRID_WIDTH) * GRID_SIZE,
                    random.randrange(1, GRID_HEIGHT) * GRID_SIZE]
        food_spawn = True
    
    snake_body.insert(0, list(snake_pos))

    # Game Over conditions
    if (snake_pos[0] >= WIDTH or snake_pos[0] <= 0 or
        snake_pos[1] >= HEIGHT or snake_pos[1] <= 0):
        game_over = True

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    # Display the game screen
    screen.fill(WHITE)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], GRID_SIZE, GRID_SIZE))
    
    if game_over:
        game_over_screen()
    
    pygame.display.flip()

    # Control game speed
    pygame.time.Clock().tick(SNAKE_SPEED)

# Quit the game and close the window
pygame.quit()
sys.exit()
