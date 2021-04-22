# -------------------------------------------------------------------------------------
#   Imports:
# -------------------------------------------------------------------------------------
import pygame
from common_val import WINDOW_HEIGHT, WINDOW_WIDTH, SQUARE_SIZE, WHITE
from gamelogic import GameLogic
from minimax_alg import minimax

# -------------------------------------------------------------------------------------
#   Common variable:
# -------------------------------------------------------------------------------------
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('AI Draughts')
depth = 3

# -------------------------------------------------------------------------------------
#   main():
# -------------------------------------------------------------------------------------
def main():
    run = True
    clock = pygame.time.Clock()                                     # init the clock for the game
    game = GameLogic(window)                                             # create object of GameLogic from pygame

    while run:
        clock.tick(60)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), depth, WHITE, float('-inf'), float('inf'))
            game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = pygame.mouse.get_pos()                 # get the position of the cursor
                row, col = int(cursor_pos[1] / SQUARE_SIZE), int(cursor_pos[0] / SQUARE_SIZE)
                game.select_disc(row, col)

        game.refresh_board()

    pygame.quit()



main()
