import pygame
from common_val import WHITE, BLACK, SQUARE_SIZE, KING

class Disc:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        self.coord_x = 0
        self.coord_y = 0
        self.calculate_coord()

    def calculate_coord(self):
        self.coord_x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.coord_y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def change_to_king(self):
        self.king = True

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.coord_x, self.coord_y), SQUARE_SIZE // 2 - 10)

        if self.king:
            win.blit(KING, (self.coord_x - KING.get_width() // 2, self.coord_y - KING.get_height() // 2))


    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_coord()

    def __repr__(self):
        return str(self.color)