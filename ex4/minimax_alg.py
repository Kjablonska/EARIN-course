from copy import deepcopy
import pygame

GREEN = (199,231,207)
BLACK = (51,55,69)

# Used for finding thebest move based on the current board and disc position.
# max_player variable is used to define whether we want to maximize or minimize the move.
# depth variable defined how much turns we want to get checked.
def minimax(position, depth, max_player, alpha, beta, game):
    # Case: we evaluated all the turnes we specified and no one has won the game yet.
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    # We want to maximize the move.
    if max_player:
        maxEval = float('-inf') # Initial state of maxEval, set to lowest possible value.
        best_move = None
        # This assumes that BLACK is our AI.
        # For every move we need to evaluate the move (caluclate reault of other player's moves.)
        for move in get_all_moves(position, GREEN, game):
            # minimax returns maxEval and best_move, we want here only yhe maxEval value.
            evaluation = minimax(move, depth-1, False, alpha, beta, game)[0]
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break

            # Select the best move.
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move

    # We want to minimize the move.
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth-1, True, alpha, beta, game)[0]
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move



def get_all_moves(board, color, game):
    moves = []
    all_pieces = board.get_all_pieces(color)

    for p in all_pieces:
        valid_moves = board.get_valid_moves(p)

        # items => (row, col): [pieces] => if we move the piece to the position (row, col) we will skip the [pieces]
        for move, skip in valid_moves.items():
            # Deepcopy allows for copying content of the object without the reference to it.
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_disc(p.row, p.col)
            # Takes piece, move and temp_board, make the move and returns the resulting board.
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])

    if skip:    # If in this move we skiped any piece, we need to remove it from the board.
        board.remove(skip)

    return board

