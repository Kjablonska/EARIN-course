import pygame
from common_val import WINDOW_HEIGHT, WINDOW_WIDTH, SQUARE_SIZE, GREEN, WHITE

from game import Game
from minimax_alg import minimax

fps = 60
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('AI Draughts')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(window)

    while run:
        clock.tick(fps)

        if game.turn == GREEN:
            value, new_board = minimax(game.get_board(), 3, GREEN, float('-inf'), float('inf'), game)
            game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
