import pygame

from board import Board, display_possible_moves
from common_val import BLACK, WHITE


class GameLogic:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
        self.win = win

    # Updates board.
    def refresh_board(self):
        self.board.display_discs(self.win)
        display_possible_moves(self.win, self.valid_moves)
        pygame.display.update()

    def restart_game(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

    def select_disc(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select_disc(row, col)

        disc = self.board.get_disc(row, col)
        if disc != 0 and disc.color == self.turn:
            self.selected = disc
            self.valid_moves = self.board.get_possible_moves(disc)
            return True

        return False

    def _move(self, row, col):
        disc = self.board.get_disc(row, col)

        if self.selected and disc == 0 and (row, col) in self.valid_moves:
            self.board.make_move(self.selected, row, col)
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



    def get_board(self):
        return self.board

    # When AI makes a move, the new board is returned and turn is changed.
    def ai_move(self, board):
        self.board = board
        self.change_turn()
