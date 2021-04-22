# -------------------------------------------------------------------------------------
#   Imports:
# -------------------------------------------------------------------------------------
import pygame
from common_val import WINDOW_HEIGHT, WINDOW_WIDTH, SQUARE_SIZE, WHITE
from gamelogic import GameLogic
from minimax_alg import minimax

# -------------------------------------------------------------------------------------
#   Common variables:
# -------------------------------------------------------------------------------------
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('AI Draughts')
depth = 3

# -------------------------------------------------------------------------------------
#   main():
# -------------------------------------------------------------------------------------


def main():
    run = True
    # Init the clock for the game.
    clock = pygame.time.Clock()
    # Create object of GameLogic from pygame.
    game = GameLogic(window)

    while run:
        # Setting game FPS.
        clock.tick(60)

        # White discs are played by AI, it starts the game.
        if game.turn == WHITE:
            value, new_board = minimax(
                game.get_board(), depth, float('-inf'), float('inf'), WHITE)
            game.get_AI_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the cursor
                cursor_pos = pygame.mouse.get_pos()
                row, col = int(
                    cursor_pos[1] / SQUARE_SIZE), int(cursor_pos[0] / SQUARE_SIZE)
                # Validate selected disc.
                game.validate_disc(row, col)

        game.refresh_board()

    pygame.quit()


main()
