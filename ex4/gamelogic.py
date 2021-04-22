# -------------------------------------------------------------------------------------
#   Imports:
# -------------------------------------------------------------------------------------
import pygame
from board import Board, display_possible_moves
from common_val import BLACK, WHITE

# -------------------------------------------------------------------------------------
#   Class representing logic of the game.
#   Class reponsibilities:
#       - refreshing the board,
#       - restarting game state,
#       - algorithm for selecting the disc to make a move,
#       - making a move - removing jumped_over discs,
#       - changing a turn
# -------------------------------------------------------------------------------------


class GameLogic:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
        self.win = win

    # Method for validation of selected disc.
    # In case the self.selected is not None, meaning that the player already selected a disc to move, do_move method is called.
    # Otherwise, the (row, col) position is validated and self.selected is set to (row, col).
    def validate_disc(self, row, col):
        # Player already selected a disc, (row, col) is a postition to which the player wants to move it.
        if self.selected:
            self.do_move(row, col)

        else:
            disc = self.board.get_disc(row, col)
            if disc != 0 and disc.color == self.turn:
                self.selected = disc
                self.valid_moves = self.board.get_possible_moves(disc)
                # Selected disc is valid = can be moved to some position.
                return True

        return False

    def do_move(self, row, col):
        # Check if disc can be moved to the position (row, col)
        valid_move = self._move(row, col)
        # Case: the selected disc is not valid - can not be moved.
        if not valid_move:
            # Setting selected to None & calling the method again.
            self.selected = None
            self.validate_disc(row, col)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    #   When AI makes a move, the new board is returned and turn is changed.
    def get_AI_move(self, board):
        self.board = board
        self.change_turn()

    # Updates board.
    def refresh_board(self):
        self.board.display_discs(self.win)
        display_possible_moves(self.win, self.valid_moves)
        pygame.display.update()

    # Reset GameLogic class state.
    def restart_game(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

    def get_board(self):
        return self.board

    # Method for validation if we can make a move to the position (row, col)
    def _move(self, row, col):
        disc = self.board.get_disc(row, col)

        # Checking if position is valid.
        if self.selected and disc == 0 and (row, col) in self.valid_moves:
            self.board.make_move(self.selected, row, col)
            jumped_over = self.valid_moves[(row, col)]
            if jumped_over:
                self.board.delete_jumped_over(jumped_over)

            self.change_turn()

        else:
            return False

        return True
