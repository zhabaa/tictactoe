import sys
from settings import *
import pygame


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("tictactoe")
screen.fill(COLORS["BG_COLOR"])

board = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]
player = "X"


def draw_board():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(
            screen,
            COLORS["LINE_COLOR"],
            (0, CELL_SIZE * i),
            (WIDTH, CELL_SIZE * i),
            LINE_WIDTH,
        )

        pygame.draw.line(
            screen,
            COLORS["LINE_COLOR"],
            (CELL_SIZE * i, 0),
            (CELL_SIZE * i, HEIGHT),
            LINE_WIDTH,
        )


def winner_screen(winner: str, draw: bool = False):
    font = pygame.font.Font(None, 100)

    msg = "Ничья" if draw else f"Победил игрок {winner}"
        
    text = font.render(msg, True, COLORS["CROSS_COLOR"])
    
    screen.fill(COLORS["BG_COLOR"])
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    pygame.display.update()
    
    screen_flag = True
    
    while screen_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                screen_flag = False

    reset_game()

def draw_figures():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):

            if board[i][j] == "O":
                pygame.draw.circle(
                    screen,
                    COLORS["CIRCLE_COLOR"],
                    (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2),
                    CIRCLE_RADIUS,
                    LINE_WIDTH,
                )

            elif board[i][j] == "X":
                pygame.draw.line(
                    screen,
                    COLORS["CROSS_COLOR"],
                    (j * CELL_SIZE + SPACE, i * CELL_SIZE + CELL_SIZE - SPACE),
                    (j * CELL_SIZE + CELL_SIZE - SPACE, i * CELL_SIZE + SPACE),
                    CROSS_WIDTH,
                )

                pygame.draw.line(
                    screen,
                    COLORS["CROSS_COLOR"],
                    (j * CELL_SIZE + SPACE, i * CELL_SIZE + SPACE),
                    (
                        j * CELL_SIZE + CELL_SIZE - SPACE,
                        i * CELL_SIZE + CELL_SIZE - SPACE,
                    ),
                    CROSS_WIDTH,
                )


def check_winner():
    for i in range(GRID_SIZE):
        if board[i][0] == board[i][1] == board[i][2] is not None:
            return board[i][0]

    for j in range(GRID_SIZE):
        if board[0][j] == board[1][j] == board[2][j] is not None:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] is not None:
        return board[0][2]

    return None


def reset_game():
    global board, player
    board = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]
    player = "X"
    screen.fill(COLORS["BG_COLOR"])
    draw_board()


def game_cycle():
    global player, board    

    draw_board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                row = mouse_y // CELL_SIZE
                col = mouse_x // CELL_SIZE

                if board[row][col] is None:
                    board[row][col] = player

                    player = "O" if player == "X" else "X"

                    screen.fill(COLORS["BG_COLOR"])

                    draw_board()
                    draw_figures()
                    
                    winner = check_winner()

                    if winner:
                        winner_screen(winner)

                    if all(all(cell is not None for cell in row) for row in board):
                        winner_screen('=', draw=True)
                                                
        pygame.display.flip()


if __name__ == "__main__":
    game_cycle()

# Писечка доработано фифти фифти так ендскрин добавил