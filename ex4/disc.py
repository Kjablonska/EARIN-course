# -------------------------------------------------------------------------------------
#   Imports:
# -------------------------------------------------------------------------------------
import pygame
from common_val import SQUARE_SIZE, KING, WHITE

# -------------------------------------------------------------------------------------
#   Class representing logic of the disc.
#   Class reponsibilities:
#       - chaning disc to 'king',
#       - displaying discs
# -------------------------------------------------------------------------------------

class Disc:
    # -------------------------------------------------------------------------------------
    #   Magic methods:
    # -------------------------------------------------------------------------------------
    def __init__(self, row, col, color):
        self.row, self.col, self.color, self.king = row, col, color, False
        self.coord_x, self.coord_y = 0, 0
        self.calculate_coord()

    def __repr__(self):
        if self.color == WHITE:
            return 'W'
        return 'B'

    def change_to_king(self):
        self.king = True

    def calculate_coord(self):
        self.coord_x, self.coord_y = SQUARE_SIZE * self.col + int(SQUARE_SIZE / 2), SQUARE_SIZE * self.row + int(SQUARE_SIZE / 2)

    def move(self, row, col):
        self.row, self.col = row, col
        self.calculate_coord()

    def display(self, win):
        pygame.draw.circle(win, self.color, (self.coord_x, self.coord_y), int(SQUARE_SIZE / 2) - 10)
        if self.king:
            win.blit(KING, (self.coord_x - int(KING.get_width() / 2), self.coord_y - int(KING.get_height() / 2)))


