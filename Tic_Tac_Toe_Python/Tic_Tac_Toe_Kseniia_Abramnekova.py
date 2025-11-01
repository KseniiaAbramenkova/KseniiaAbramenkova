import pygame
import sys
import random
import time

pygame.init()

# Screen parameters
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
CELL_SIZE = WIDTH // BOARD_COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)  # Brown color for the winner text
LIGHT_GRAY = (211, 211, 211)  # Light gray background
BORDER_COLOR = WHITE
X_COLOR = (128, 0, 0)  # Maroon color for X
O_COLOR = BLACK  # Black color for O
BLUE = (0, 0, 255)  # Blue color for menu text
BUTTON_COLOR = (0, 100, 0)  # Dark green color for buttons
BUTTON_TEXT_COLOR = (255, 255, 255)  # White color for button text

# Game values
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]  # Game board as a 2D list
player = 1  # Current player: 1 = X, 2 = O
game_over_flag = False  # Flag to check if the game is over
mode = None  # Game mode: single-player or multiplayer
player1_score = 0  # Player 1 score
player2_score = 0  # Player 2 score
total_games = 0  # Total games played

# Screen creation
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(LIGHT_GRAY)

# Function to draw grid lines on the game board
def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BORDER_COLOR, (0, CELL_SIZE * i), (WIDTH, CELL_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, BORDER_COLOR, (CELL_SIZE * i, 0), (CELL_SIZE * i, HEIGHT), LINE_WIDTH)

# Function to draw an X on the board
def draw_x(row, col):
    center_x = col * CELL_SIZE + CELL_SIZE // 2
    center_y = row * CELL_SIZE + CELL_SIZE // 2
    offset = CELL_SIZE // 4
    pygame.draw.line(screen, X_COLOR, (center_x - offset, center_y - offset), 
                     (center_x + offset, center_y + offset), LINE_WIDTH)
    pygame.draw.line(screen, X_COLOR, (center_x - offset, center_y + offset), 
                     (center_x + offset, center_y - offset), LINE_WIDTH)

# Function to draw an O on the board
def draw_o(row, col):
    center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
    pygame.draw.circle(screen, O_COLOR, center, CELL_SIZE // 4, LINE_WIDTH)

# Function to display the winner message
def display_winner(text):
    font = pygame.font.Font(None, 50)
    message = font.render(text, True, BROWN)
    text_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    # Draw a white border around the text
    pygame.draw.rect(screen, WHITE, text_rect.inflate(20, 20), border_radius=10)
    screen.blit(message, text_rect)
    pygame.display.flip()

# Function to display the current score
def display_score():
    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Player 1: {player1_score}  Player 2: {player2_score}  Total Games: {total_games}", True, BLACK)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT - 40))

# Function to draw the restart button
def draw_restart_button():
    font = pygame.font.Font(None, 40)  
    restart_text = font.render("Restart Game", True, BUTTON_TEXT_COLOR)
    button_rect = pygame.Rect(WIDTH // 2 - restart_text.get_width() // 2, HEIGHT - 120, restart_text.get_width() + 20, 50)  # Reduced height

    pygame.draw.rect(screen, BUTTON_COLOR, button_rect, border_radius=10)
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT - 110))
    return button_rect

# Function to draw the "Back to Menu" button
def draw_back_to_menu_button():
    font = pygame.font.Font(None, 40)
    menu_text = font.render("Back to Menu", True, BUTTON_TEXT_COLOR)
    button_rect = pygame.Rect(WIDTH // 2 - menu_text.get_width() // 2, HEIGHT - 60, menu_text.get_width() + 20, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect, border_radius=10)
    screen.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT - 50))
    return button_rect

# Menu to choose the game mode
def draw_menu():
    screen.fill(LIGHT_GRAY)
    font = pygame.font.Font(None, 60)
    title = font.render("Select Mode", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    font = pygame.font.Font(None, 50)
    single_player = font.render("Play vs Computer", True, BLUE)
    multiplayer = font.render("Play vs Player", True, BLUE)

    # Define clickable areas
    single_player_rect = pygame.Rect(WIDTH // 2 - single_player.get_width() // 2, 200, single_player.get_width(), single_player.get_height())
    multiplayer_rect = pygame.Rect(WIDTH // 2 - multiplayer.get_width() // 2, 300, multiplayer.get_width(), multiplayer.get_height())

    screen.blit(single_player, (WIDTH // 2 - single_player.get_width() // 2, 200))
    screen.blit(multiplayer, (WIDTH // 2 - multiplayer.get_width() // 2, 300))
    pygame.display.flip()

    return single_player_rect, multiplayer_rect

# Function to check the winner
def check_winner():
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

# Function to check if the board is full
def is_full():
    for row in board:
        if None in row:
            return False
    return True

# Function to restart the game
def restart_game():
    global board, player, game_over_flag
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 1
    game_over_flag = False
    screen.fill(LIGHT_GRAY)
    draw_lines()

# Function to reset player scores
def reset_scores():
    global player1_score, player2_score, total_games
    player1_score = 0
    player2_score = 0
    total_games = 0

# Function to check for winning or blocking moves
def check_win_or_block(player):
    for row in range(BOARD_ROWS):
        # Check rows
        if board[row].count(player) == 2 and board[row].count(None) == 1:
            return row, board[row].index(None)
    for col in range(BOARD_COLS):
        # Check columns
        column = [board[row][col] for row in range(BOARD_ROWS)]
        if column.count(player) == 2 and column.count(None) == 1:
            return column.index(None), col
    # Check main diagonal
    diag1 = [board[i][i] for i in range(BOARD_ROWS)]
    if diag1.count(player) == 2 and diag1.count(None) == 1:
        return diag1.index(None), diag1.index(None)
    # Check secondary diagonal
    diag2 = [board[i][BOARD_COLS - i - 1] for i in range(BOARD_ROWS)]
    if diag2.count(player) == 2 and diag2.count(None) == 1:
        return diag2.index(None), BOARD_COLS - diag2.index(None) - 1
    return None

def simple_computer_move():
    #easy mode - random position
    empty_cells = [(row, col) for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if board[row][col] is None]
    row, col = random.choice(empty_cells)
    board[row][col] = 2
    draw_o(row, col)

def strategic_computer_move():
    # diificult mode - use strategy to biuld line or block another player
    move = check_win_or_block(2)
    if move:
        row, col = move
    else:
        move = check_win_or_block(1)
        if move:
            row, col = move
        else:
            empty_cells = [(row, col) for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if board[row][col] is None]
            row, col = random.choice(empty_cells)
    board[row][col] = 2
    draw_o(row, col)

def computer_move():
    if difficulty == "simple":
        simple_computer_move()
    elif difficulty == "hard":
        strategic_computer_move()

def draw_single_player_menu():
    # menu to chose difficulty
    screen.fill(LIGHT_GRAY)
    font = pygame.font.Font(None, 60)
    title = font.render("Select Difficulty", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    font = pygame.font.Font(None, 50)
    simple_mode = font.render("Simple", True, BLUE)
    hard_mode = font.render("Hard", True, BLUE)

    simple_mode_rect = pygame.Rect(WIDTH // 2 - simple_mode.get_width() // 2, 200, simple_mode.get_width(), simple_mode.get_height())
    hard_mode_rect = pygame.Rect(WIDTH // 2 - hard_mode.get_width() // 2, 300, hard_mode.get_width(), hard_mode.get_height())

    screen.blit(simple_mode, (WIDTH // 2 - simple_mode.get_width() // 2, 200))
    screen.blit(hard_mode, (WIDTH // 2 - hard_mode.get_width() // 2, 300))
    pygame.display.flip()

    return simple_mode_rect, hard_mode_rect

difficulty = None

# Main loop
running = True
while running:
    if mode is None:
        single_player_rect, multiplayer_rect = draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if single_player_rect.collidepoint(pos):
                    difficulty_menu = True
                    while difficulty_menu:
                        simple_mode_rect, hard_mode_rect = draw_single_player_menu()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                difficulty_menu = False
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()
                                if simple_mode_rect.collidepoint(pos):
                                    difficulty = "simple"
                                    difficulty_menu = False
                                    mode = "single"
                                    restart_game()
                                elif hard_mode_rect.collidepoint(pos):
                                    difficulty = "hard"
                                    difficulty_menu = False
                                    mode = "single"
                                    restart_game()
                elif multiplayer_rect.collidepoint(pos):
                    mode = "multi"
                    restart_game()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over_flag:
                x, y = event.pos
                row, col = y // CELL_SIZE, x // CELL_SIZE
                if board[row][col] is None:
                    if player == 1:
                        board[row][col] = 1
                        draw_x(row, col)
                    elif player == 2 and mode == "multi":
                        board[row][col] = 2
                        draw_o(row, col)
                    pygame.display.flip()

                    winner = check_winner()
                    if winner:
                        if winner == 1:
                            player1_score += 1
                        elif winner == 2:
                            player2_score += 1
                        total_games += 1
                        display_winner(f"Player {'X' if winner == 1 else 'O'} wins!")
                        game_over_flag = True
                    elif is_full():
                        total_games += 1
                        display_winner("It's a Draw!")
                        game_over_flag = True
                    else:
                        player = 3 - player  # Change player

            elif event.type == pygame.MOUSEBUTTONDOWN and game_over_flag:
                pos = pygame.mouse.get_pos()
                restart_button_rect = draw_restart_button()
                back_to_menu_button_rect = draw_back_to_menu_button()  # brawing bottom "Back to Menu"

                # buttoms at the end of the game
                if restart_button_rect.collidepoint(pos):
                    restart_game()
                elif back_to_menu_button_rect.collidepoint(pos):
                    mode = None  #back to menu
                    reset_scores()
                    screen.fill(LIGHT_GRAY)

        
        display_score()  # Display score at the bottom

        if mode == "single" and player == 2 and not game_over_flag:
            time.sleep(0.5)
            computer_move()
            pygame.display.flip()

            winner = check_winner()
            if winner:
                if winner == 1:
                    player1_score += 1
                elif winner == 2:
                    player2_score += 1
                total_games += 1
                display_winner(f"Player {'X' if winner == 1 else 'O'} wins!")
                game_over_flag = True
            elif is_full():
                total_games += 1
                display_winner("It's a Draw!")
                game_over_flag = True
            else:
                player = 1

        if game_over_flag:
            restart_button_rect = draw_restart_button()
            back_to_menu_button_rect = draw_back_to_menu_button()

    pygame.display.flip()

pygame.quit()
sys.exit()