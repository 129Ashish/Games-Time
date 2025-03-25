import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock, Paper, Scissors")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load fonts
font = pygame.font.SysFont("Arial", 30)

# Game variables
choices = ["Rock", "Paper", "Scissors"]
player_choice = None
computer_choice = None
result = ""

# Function to display text
def display_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Rock
                player_choice = "Rock"
            elif event.key == pygame.K_p:  # Paper
                player_choice = "Paper"
            elif event.key == pygame.K_s:  # Scissors
                player_choice = "Scissors"

            if player_choice:
                computer_choice = random.choice(choices)
                if player_choice == computer_choice:
                    result = "It's a Tie!"
                elif (player_choice == "Rock" and computer_choice == "Scissors") or \
                     (player_choice == "Paper" and computer_choice == "Rock") or \
                     (player_choice == "Scissors" and computer_choice == "Paper"):
                    result = "You Win!"
                else:
                    result = "You Lose!"

    # Fill the screen with white
    screen.fill(WHITE)

    # Display choices and result
    display_text("Press R for Rock", 50, 50)
    display_text("Press P for Paper", 50, 100)
    display_text("Press S for Scissors", 50, 150)
    if player_choice and computer_choice:
        display_text(f"Your Choice: {player_choice}", 50, 200)
        display_text(f"Computer Choice: {computer_choice}", 50, 230)
        display_text(result, 50, 260)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()