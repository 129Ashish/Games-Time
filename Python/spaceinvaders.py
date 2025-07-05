import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load images
player_image = pygame.Surface((50, 30))
player_image.fill(GREEN)
alien_image = pygame.Surface((40, 30))
alien_image.fill(RED)
bullet_image = pygame.Surface((5, 10))
bullet_image.fill(WHITE)

# Player settings
player_x = width // 2
player_y = height - 50
player_speed = 7

# Bullet settings
bullets = []
bullet_speed = -10

# Alien settings
aliens = []
alien_speed = 2
alien_spawn_time = 1000  # milliseconds
pygame.time.set_timer(pygame.USEREVENT, alien_spawn_time)

# Game loop control
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            # Spawn a new alien
            alien_x = random.randint(0, width - 40)
            aliens.append(pygame.Rect(alien_x, 0, 40, 30))

    # Get the keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - 50:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        # Shoot a bullet
        bullet_rect = pygame.Rect(player_x + 22, player_y, 5, 10)
        bullets.append(bullet_rect)

    # Move bullets
    for bullet in bullets[:]:
        bullet.y += bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Move aliens
    for alien in aliens[:]:
        alien.y += alien_speed
        if alien.y > height:
            aliens.remove(alien)

    # Check for collisions
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)
                break

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw player
    screen.blit(player_image, (player_x, player_y))

    # Draw bullets
    for bullet in bullets:
        screen.blit(bullet_image, (bullet.x, bullet.y))

    # Draw aliens
    for alien in aliens:
        screen.blit(alien_image, (alien.x, alien.y))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()