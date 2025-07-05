import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Paddle settings
paddle_width = 100
paddle_height = 20
paddle_speed = 10

# Ball settings
ball_size = 15
ball_speed_x = 5
ball_speed_y = -5

# Create paddle
paddle_x = (width - paddle_width) // 2
paddle_y = height - paddle_height - 10

# Create ball
ball_x = width // 2
ball_y = height // 2

# Create bricks
brick_rows = 5
brick_cols = 10
brick_width = width // brick_cols
brick_height = 30
bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        bricks.append(pygame.Rect(col * brick_width, row * brick_height, brick_width, brick_height))

# Game loop control
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= width - ball_size:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddle
    if (paddle_y <= ball_y + ball_size <= paddle_y + paddle_height) and (paddle_x <= ball_x <= paddle_x + paddle_width):
        ball_speed_y = -ball_speed_y

    # Ball collision with bricks
    for brick in bricks[:]:
        if brick.collidepoint(ball_x + ball_size // 2, ball_y + ball_size // 2):
            ball_speed_y = -ball_speed_y
            bricks.remove(brick)

    # Check if the ball falls below the paddle
    if ball_y > height:
        running = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)

    # Draw paddle
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.ellipse(screen, RED, (ball_x, ball_y, ball_size, ball_size))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()