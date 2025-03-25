import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game variables
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'
game_over = False

# Function to draw the board
def draw_board():
    screen.fill(WHITE)
    for row in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, row * 100), (width, row * 100), 2)
        pygame.draw.line(screen, BLACK, (row * 100, 0), (row * 100, height), 2)

    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * 100 + 20, row * 100 + 20), (col * 100 + 80, row * 100 + 80), 2)
                pygame.draw.line(screen, RED, (col * 100 + 80, row * 100 + 20), (col * 100 + 20, row * 100 + 80), 2)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLUE, (col * 100 + 50, row * 100 + 50), 30, 2)

# Function to check for a win
def check_win():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

# Function to reset the game
def reset_game():
    global board, current_player, game_over
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            row = mouse_y // 100
            col = mouse_x // 100
            if board[row][col] == '':
                board[row][col] = current_player
                if check_win():
                    game_over = True
                current_player = 'O' if current_player == 'X' else 'X'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Press 'R' to reset the game
                reset_game()

    draw_board()
    pygame.display.flip()

    if game_over:
        font = pygame.font.SysFont("Arial", 30)
        text = font.render(f"{current_player} wins! Press R to restart.", True, BLACK)
        screen.blit(text, (20, height // 2 - 15))
        pygame.display.flip()

# Quit Pygame
pygame.quit()