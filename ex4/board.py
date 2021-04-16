import pygame
from common_val import RED, ROWS, COLS, GREEN, SQUARE_SIZE, WHITE, BLACK
from disc import Disc


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.green_piece = self.black_piece = 12
        self.green_kings = self.black_kings = 0
        self.create_board()

    def draw_square(self, win):
        win.fill(RED)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Returns result of the current board.
    # If result is positive => green is winning.
    def evaluate(self):
        return self.green_piece - self.black_piece
        # Way to prioritize priortize becoming a king.
        # + (self.green_kings * 0.5 - self.black_kings * 0.5)

    # Returns all pieces of a specified color.
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                # If at the possition there is no piece, is is filled with 0, else there is stored Disc object.
                if piece != 0 and piece.color == color:
                    pieces.append(piece)

        return pieces

    # Evaluates if there is a winner based on the number of each color pieces on the board.
    def winner(self):
        if self.black_piece <= 0:
            return BLACK
        elif self.green_piece <= 0:
            return GREEN

        return None

    def move(self, disc, row, col):
        self.board[disc.row][disc.col], self.board[row][col] = self.board[row][col], self.board[disc.row][disc.col]     # swaping disc
        disc.move(row, col)

        if row == ROWS - 1 or row == 0:
            disc.change_to_king()
            if disc.color == GREEN:
                self.green_kings = self.green_kings + 1
            else:
                self.black_kings = self.black_kings + 1

    def get_disc(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Disc(row, col, GREEN))
                    elif row > 4:
                        self.board[row].append(Disc(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_square(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]

                if piece != 0:
                    piece.draw(win)

    def remove(self, disces):
        for disc in disces:
            self.board[disc.row][disc.col] = 0
            if disc != 0:
                if disc.color == BLACK:
                    self.black_piece -= 1
                if disc.color == GREEN:
                    self.green_piece -= 1

    def get_valid_moves(self, disc):
        valid_moves = {}
        left_dir = disc.col - 1
        right_dir = disc.col + 1
        row = disc.row

        if disc.color == BLACK or disc.king:
            valid_moves.update(self._traverse_left(row - 1, max(row-3, -1), -1, disc.color, left_dir))
            valid_moves.update(self._traverse_right(row - 1, max(row-3, -1), -1, disc.color, right_dir))

        if disc.color == GREEN or disc.king:
            valid_moves.update(self._traverse_left(row + 1, min(row+3, ROWS), 1, disc.color, left_dir))
            valid_moves.update(self._traverse_right(row + 1, min(row+3, ROWS), 1, disc.color, right_dir))

        return valid_moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
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
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r + step, row, step, color, left-1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left+1, skipped=last))
                break

            elif curr.color == color:
                break
            else:
                last = [curr]

            left -= 1

        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
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
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)

                    moves.update(self._traverse_left(r + step, row, step, color, right-1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right+1, skipped=last))
                break

            elif curr.color == color:
                break
            else:
                last = [curr]

            right += 1

        return moves


# def get_board(self):
#     return self.board

# # When AI makes a move, the new board is returned and turn is changed.
# def ai_move(self, board):
#     self.board = board
#     self.change_turn()