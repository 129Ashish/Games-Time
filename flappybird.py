import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird Clone")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Load images
bird_image = pygame.Surface((34, 24))
bird_image.fill((255, 255, 0))  # Yellow bird
pipe_image = pygame.Surface((52, height))
pipe_image.fill((0, 255, 0))  # Green pipes

# Game variables
bird_x = 50
bird_y = height // 2
bird_velocity = 0
gravity = 0.5
flap_strength = -10
pipes = []
pipe_gap = 150
pipe_frequency = 1500  # milliseconds
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# Function to create pipes
def create_pipe():
    height_top = random.randint(50, height - pipe_gap - 50)
    height_bottom = height - height_top - pipe_gap
    pipes.append((width, height_top, height_bottom))

# Game loop control
running = True
pygame.time.set_timer(pygame.USEREVENT, pipe_frequency)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            create_pipe()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = flap_strength

    # Update bird position
    bird_velocity += gravity
    bird_y += bird_velocity

    # Move pipes
    for i in range(len(pipes)):
        pipes[i] = (pipes[i][0] - 5, pipes[i][1], pipes[i][2])

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe[0] > -52]

    # Check for collisions
    for pipe in pipes:
        if (bird_x + 34 > pipe[0] and bird_x < pipe[0] + 52):
            if bird_y < pipe[1] or bird_y + 24 > height - pipe[2]:
                running = False

    # Check if bird hits the ground or goes off-screen
    if bird_y > height or bird_y < 0:
        running = False

    # Update score
    for pipe in pipes:
        if pipe[0] + 52 < bird_x and not pipe[0] + 52 in [p[0] for p in pipes]:
            score += 1

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw pipes
    for pipe in pipes:
        screen.blit(pipe_image, (pipe[0], 0), (0, 0, 52, pipe[1]))  # Top pipe
        screen.blit(pipe_image, (pipe[0], height - pipe[2]), (0, 0, 52, pipe[2]))  # Bottom pipe

    # Draw bird
    screen.blit(bird_image, (bird_x, bird_y))

    # Draw score
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()