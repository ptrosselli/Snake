import pygame
import sys
import random

pygame.init()

# Screen dimensions
width, height = 600, 300
cols, rows = 30, 15
cell_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

# Game logic variables
pts = []
apples = []
snake = []
apple = True

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Grid display
for x in range(cols):
    for y in range(rows):
        if x in range(10, 16) and y == 9:
            snake.append((x, y))
        else:
            pts.append((x, y))


def draw_snake():
    for spot in snake:
        s = pygame.Rect(spot[0] * cell_size, spot[1] * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, GREEN, s)

def clear_snake():
    for spot in snake:
        s = pygame.Rect(spot[0] * cell_size, spot[1] * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, BLACK, s)

def move_snake(direction):
    global apple
    spot = snake[-1]

    if direction == 'd':
        spot = (spot[0] + 1, spot[1])
    elif direction == 's':
        spot = (spot[0], spot[1] + 1)
    elif direction == 'w':
        spot = (spot[0], spot[1] - 1)
    elif direction == 'a':
        spot = (spot[0] - 1, spot[1])
    
    clear_snake()

    if spot in apples:
        apples.remove(spot)
        snake.append(spot)
        apple = True
    elif spot in snake:
        draw_snake()
        return
    elif spot not in pts:
        draw_snake()
        return
    else:
        pts.remove(spot)
        snake.append(spot)
        el = snake.pop(0)
        pts.append(el)

    draw_snake()

def generate_apple():
    spot = random.choice(pts)
    pts.remove(spot)
    apples.append(spot)
    r = pygame.Rect(spot[0] * cell_size, spot[1] * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, RED, r)

# Main loop
running = True
clock = pygame.time.Clock()
draw_snake()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_snake('w')
            elif event.key == pygame.K_a:
                move_snake('a')
            elif event.key == pygame.K_s: 
                move_snake('s') 
            elif event.key == pygame.K_d:
                move_snake('d')
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    
    if apple:
        generate_apple()
        apple = False
    
    clock.tick(100)
 

    # Update the display
    pygame.display.flip()