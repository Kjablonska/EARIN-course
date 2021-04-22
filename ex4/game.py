import pygame

from board import Board
from common_val import BLACK, WHITE, BLUE, SQUARE_SIZE


class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
        self.win = win

    # Updates board.
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)


        disc = self.board.get_disc(row, col)
        if disc != 0 and disc.color == self.turn:
            self.selected = disc
            self.valid_moves = self.board.get_valid_moves(disc)
            return True

        return False

    def _move(self, row, col):
        disc = self.board.get_disc(row, col)

        if self.selected and disc == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)

            self.change_turn()

        else:
            return False

        return True

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK


    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def get_board(self):
        return self.board

    # When AI makes a move, the new board is returned and turn is changed.
    def ai_move(self, board):
        self.board = board
        self.change_turn()