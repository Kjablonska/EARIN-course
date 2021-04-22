# -------------------------------------------------------------------------------------
#   Imports:
# -------------------------------------------------------------------------------------
import pygame
from common_val import RED, ROWS, COLS, WHITE, SQUARE_SIZE, BEIGE, BLACK
from disc import Disc

# -------------------------------------------------------------------------------------
#   Class representing logic of the board.
#   Class reponsibilities:
#       - desplaying the current board,
#       - displaying the possible moves on the board,
#       - getting all disc of a given color,
#       - calculating the score of the board,
#       - initializing a board
#       - finding possible moves
#       - finding a winner
# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------
#   Static methods:
# -------------------------------------------------------------------------------------
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
    # If result is positive => player with white discs is winning.
    def calculate_result(self):
        return self.white_pieces - self.black_pieces

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

    # Get disc from a specified board position.
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

    # Method for removing jumped_over discs.
    def remove(self, discs):
        for disc in discs:
            self.board[disc.row][disc.col] = 0
            if disc != 0:
                if disc.color == BLACK:
                    self.black_pieces -= 1
                if disc.color == WHITE:
                    self.white_pieces -= 1


    # Method for finding all possible moves.
    # There are possible cases:
    # 1. There is no disc at the diagonal position => the player can move there.
    # 2. There is a disc of the same color at the diagonal position => the player can not move there.
    # 3. There is a disc of different color at the diagonal position => the player can jump over it if the next diagonall position is empty.
    # 4. Double jumps
    # 5. The disc is a King => can move in each direction diagonally.
    def get_possible_moves(self, disc):
        valid_moves = {}
        row = disc.row

        if disc.color == BLACK or disc.king:
            valid_moves.update(self._find_all_jumps(row - 1, max(row - 3, -1), -1, disc.color, disc.col - 1, "left"))
            valid_moves.update(self._find_all_jumps(row - 1, max(row - 3, -1), -1, disc.color, disc.col + 1, "right"))

        if disc.color == WHITE or disc.king:
            valid_moves.update(self._find_all_jumps(row + 1, min(row + 3, ROWS), 1, disc.color, disc.col - 1, "left"))
            valid_moves.update(self._find_all_jumps(row + 1, min(row + 3, ROWS), 1, disc.color, disc.col + 1, "right"))

        return valid_moves

    def _find_all_jumps(self, start, stop, step, color, diag, direct, jumped_over=[]):
        moves = {}
        jump = []

        for row in range(start, stop, step):
            # Checking board boundaries.
            if direct == "right":
                if diag >= COLS:
                    break
            elif direct == "left":
                if diag < 0:                                # Outside of the board.
                    break

            curr = self.board[row][diag]
            if curr == 0:                                    # No disc at the diagonal-left position.
                if jumped_over and not jump:                 # Already jumped over some disc but can not do more jumps.
                    break
                elif jumped_over:                            # Double jump. Combine positions to which the player can go.
                    moves[(row, diag)] = jump + jumped_over
                else:
                    moves[(row, diag)] = jump

                if jump:
                    if step == -1:
                        row = max(row-3, -1)
                    else:
                        row = min(row+3, ROWS)

                    #   Checking if there is a possibiliy of double/tripple jump.
                    moves.update(self._find_all_jumps(row + step, row, step, color, diag - 1, "left", jumped_over=jump))
                    moves.update(self._find_all_jumps(row + step, row, step, color, diag + 1, "right", jumped_over=jump))
                break

            elif curr.color == color:   #   Disc at the diagonal-left position is at the same color as the currently selected disc => the player can not jump over it.
                break
            else:                       #   Disc at the diagonal-left position is of a different color => the player can jump over it.
                jump = [curr]

            if direct == "right":
                diag += 1
            elif direct == "left":
                diag -= 1

        return moves
