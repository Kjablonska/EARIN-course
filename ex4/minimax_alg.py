# -------------------------------------------------------------------------------------
#   Imports:
# -------------------------------------------------------------------------------------
from copy import deepcopy
from common_val import BLACK, WHITE

# -------------------------------------------------------------------------------------
#   Implementation of minimax algorithm with alpha beta pruning:
#   board           -   value of the currently evaluated board.
#   depth           -   defined how much turns we want to get checked.
#   is_max_player   -   defines whether we want to maximize or minimize the move.
#   alpha           -   initialized to -infinity, keeps value of the maximum score
#   beta            -   initialized to +infinity, keeps value of the minimum score
#
#   Assumptions:
#   AI plays with white discs and it starts the game.
#
#   Minimax algorithm with alpha beta pruning description:
#   Alorithm is developed to find the result of all possible moves, meaning than for each potential move there is calculated difference between number of black and white moves.
#   In case when we want to maximize the move, the move resulting in the greatest difference (result) needs to be picked. Otherwise, the move resulting in the smallest difference is picked.
#
#   Alpha beta pruning is a way for minimax algorithm optimization.
#   The game tree is evaluated as long as there is a possibility of finding better move. For instance - for miximizing player, knowing that one branch will give better result than the other, there is no need for further evaluation of the "loosing" branch.
#
# -------------------------------------------------------------------------------------


def minimax(board, depth, alpha, beta, is_max_player):
    #   Case: we evaluated all the turns (speicified by depth variable) and no one has won the game yet.
    if depth == 0 or board.get_winner() != None:
        return board.calculate_result(), board

    # Maximize the move.
    if is_max_player:
        maximizing_move = None
        max_score = float('-inf')
        moves = find_possible_moves(board, BLACK)

        #   For each possible move there is a need to calcaulte the result of other player's moves.
        for move in moves:
            # minimax method returns max_score and maximizing_move, we want here only max_score value.
            score = minimax(move, depth-1, alpha, beta, False)[0]
            alpha = max(alpha, score)
            if beta <= alpha:  # No need to evaluate more moves since alpha is already greater than beta => current move is selected.
                break

            max_score = max(max_score, score)
            if max_score == score:
                maximizing_move = move

        return max_score, maximizing_move

    # Minimize the move.
    else:
        minimizing_move = None
        min_score = float('inf')
        moves = find_possible_moves(board, WHITE)

        for move in moves:
            score = minimax(move, depth-1, alpha, beta, True)[0]
            beta = min(beta, score)
            if beta <= alpha:  # No need to evaluate more moves.
                break
            min_score = min(min_score, score)
            if min_score == score:
                minimizing_move = move

        return min_score, minimizing_move


def find_possible_moves(board, color):
    possible_moves = []
    discs = board.get_discs_by_color(color)

    for disc in discs:
        valid_moves = board.get_possible_moves(disc)

        # items => (row, col): [pieces] => if we move the piece to the board (row, col) we will skip the [pieces]
        for move, jumped_over in valid_moves.items():

            # Deepcopy allows for copying content of the object without the reference to it.
            board_copy = deepcopy(board)
            disc_copy = board_copy.get_disc(disc.row, disc.col)

            # Takes disc, move and deepcopy of the board.
            # Make move and returns the resulting board.
            new_board = make_move(
                disc_copy, move[0], move[1], board_copy, jumped_over)
            possible_moves.append(new_board)

    return possible_moves


def make_move(disc, row, col, board, skipped):
    board.make_move(disc, row, col)

    if skipped:    # If in this move we skiped any disc, we need to remove it from the board.
        board.delete_jumped_over(skipped)

    return board
