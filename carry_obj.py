import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Catch the Falling Object")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define the basket
basket_width = 100
basket_height = 20
basket_x = (width - basket_width) // 2
basket_y = height - basket_height - 10
basket_speed = 10

# Define the falling object
object_size = 20
object_x = random.randint(0, width - object_size)
object_y = 0
object_speed = 5

# Game loop control
running = True
score = 0

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < width - basket_width:
        basket_x += basket_speed

    # Move the falling object
    object_y += object_speed

    # Check for collision
    if (object_y + object_size > basket_y and
        object_x + object_size > basket_x and
        object_x < basket_x + basket_width):
        score += 1
        object_y = 0
        object_x = random.randint(0, width - object_size)

    # Reset the object if it falls past the bottom
    if object_y > height:
        object_y = 0
        object_x = random.randint(0, width - object_size)

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the basket
    pygame.draw.rect(screen, BLACK, (basket_x, basket_y, basket_width, basket_height))

    # Draw the falling object
    pygame.draw.rect(screen, RED, (object_x, object_y, object_size, object_size))

    # Draw the score
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()