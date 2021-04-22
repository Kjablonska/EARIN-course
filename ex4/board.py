# -------------------------------------------------------------------------------------
#   Imports:
# -------------------------------------------------------------------------------------
import pygame
from common_val import RED, ROWS, COLS, WHITE, SQUARE_SIZE, BEIGE, BLACK
from disc import Disc


def display_square(win):
    win.fill(RED)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, BEIGE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def display_possible_moves(win, moves):
    for move in moves:
        row, col = move
        pygame.draw.circle(win, BLACK, (col * SQUARE_SIZE + int(SQUARE_SIZE / 2), row * SQUARE_SIZE + int(SQUARE_SIZE / 2)), 25)
        pygame.draw.circle(win, BEIGE, (col * SQUARE_SIZE + int(SQUARE_SIZE / 2), row * SQUARE_SIZE + int(SQUARE_SIZE / 2)), 20)


class Board:
    # Constructor
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.white_pieces = self.black_pieces = 12
        self.white_kings = self.black_kings = 0
        self.initialize()

    # Returns result of the current board.
    # If result is positive => green is winning.
    def evaluate(self):
        return self.white_pieces - self.black_pieces
        # Way to prioritize becoming a king.
        # + (self.green_kings * 0.5 - self.black_kings * 0.5)

    # Returns all pieces of a specified color.
    def get_discs_by_color(self, color):
        discs = []
        for row in self.board:
            for piece in row:
                # If at the position there is no piece, is is filled with 0, else there is stored Disc object.
                if piece != 0 and piece.color == color:
                    discs.append(piece)

        return discs

    # Evaluates if there is a winner based on the number of each color pieces on the board.
    def winner(self):
        if self.black_pieces <= 0:
            return BLACK
        elif self.white_pieces <= 0:
            return WHITE

        return None

    def make_move(self, disc, row, col):
        self.board[disc.row][disc.col], self.board[row][col] = self.board[row][col], self.board[disc.row][disc.col]     # swaping disc
        disc.move(row, col)

        if row == ROWS - 1 or row == 0:
            disc.change_to_king()
            if disc.color == WHITE:
                self.white_kings = self.white_kings + 1
                return

            self.black_kings = self.black_kings + 1

    def get_disc(self, row, col):
        return self.board[row][col]

    def initialize(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Disc(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Disc(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def display_discs(self, win):
        display_square(win)
        for row in range(ROWS):
            for col in range(COLS):
                disc = self.board[row][col]

                if disc != 0:
                    disc.display(win)

    def remove(self, discs):
        for disc in discs:
            self.board[disc.row][disc.col] = 0
            if disc != 0:
                if disc.color == BLACK:
                    self.black_pieces -= 1
                if disc.color == WHITE:
                    self.white_pieces -= 1

    def get_possible_moves(self, disc):
        valid_moves = {}
        left_dir = disc.col - 1
        right_dir = disc.col + 1
        row = disc.row

        if disc.color == BLACK or disc.king:
            valid_moves.update(self._find_move_on_left(row - 1, max(row - 3, -1), -1, disc.color, left_dir))
            valid_moves.update(self._find_move_on_right(row - 1, max(row - 3, -1), -1, disc.color, right_dir))

        if disc.color == WHITE or disc.king:
            valid_moves.update(self._find_move_on_left(row + 1, min(row + 3, ROWS), 1, disc.color, left_dir))
            valid_moves.update(self._find_move_on_right(row + 1, min(row + 3, ROWS), 1, disc.color, right_dir))

        return valid_moves

    def _find_move_on_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            curr = self.board[r][left]
            if curr == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, -1)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._find_move_on_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._find_move_on_right(r + step, row, step, color, left + 1, skipped=last))
                break

            elif curr.color == color:
                break
            else:
                last = [curr]

            left -= 1

        return moves

    def _find_move_on_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            curr = self.board[r][right]
            if curr == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3, -1)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._find_move_on_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._find_move_on_right(r + step, row, step, color, right + 1, skipped=last))
                break

            elif curr.color == color:
                break
            else:
                last = [curr]

            right += 1

        return moves

