from helpers import *
from Main import *
import copy
import random

def get_legal_moves(board):
    cols = len(board[0])
    moves = [col for col in range(cols) if board[0][col] == " "]
    return moves

def move_priority(move, board_state, move_wins):
    cols = len(board_state[0])
    return move_wins[move], -abs(move - cols // 2)

def make_move(board, column, player):
    rows = len(board)
    for row in range(rows-1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = player
            return True
    return False

def rollout(board, current_player):
    while True:
        winner = check_winner(board)
        if winner is not None:
            return winner

        legal_moves = get_legal_moves(board)
        if not legal_moves:
            return "D"

        move = random.choice(legal_moves)
        make_move(board, move, current_player)
        current_player = "O" if current_player == "X" else "X"

def check_winner(board):
    rows = len(board)
    cols = len(board[0])

    # Horizontal
    for r in range(rows):
        for c in range(cols - WIN_CONDITION + 1):
            line = board[r][c:c+WIN_CONDITION]
            if line[0] != " " and all(cell == line[0] for cell in line):
                return line[0]

    # Vertical
    for c in range(cols):
        for r in range(rows - WIN_CONDITION + 1):
            line = [board[r+i][c] for i in range(WIN_CONDITION)]
            if line[0] != " " and all(cell == line[0] for cell in line):
                return line[0]

    # Diagonal I
    for r in range(rows - WIN_CONDITION + 1):
        for c in range(cols - WIN_CONDITION + 1):
            line = [board[r+i][c+i] for i in range(WIN_CONDITION)]
            if line[0] != " " and all(cell == line[0] for cell in line):
                return line[0]

    # Diagonal II
    for r in range(rows - WIN_CONDITION + 1):
        for c in range(WIN_CONDITION - 1, cols):
            line = [board[r+i][c-i] for i in range(WIN_CONDITION)]
            if line[0] != " " and all(cell == line[0] for cell in line):
                return line[0]


    if all(board[0][c] != " " for c in range(cols)):
        return "D"

    return None


def solve_monte_carlo(board_state, player_to_move, max_simulations):
    legal_moves = get_legal_moves(board_state)
    if not legal_moves:
        print("Draw!")
        return

    move_wins = {move: 0 for move in legal_moves}

    for move in legal_moves:
        wins = 0
        for _ in range(max_simulations):
            temp_board = copy.deepcopy(board_state)
            make_move(temp_board, move, player_to_move)

            result = rollout(temp_board, "O" if player_to_move == "X" else "X")
            if result == player_to_move:
                wins += 1
        move_wins[move] = wins / max_simulations

    best_move = max(move_wins, key = lambda m: move_priority(m, board_state, move_wins))
    make_move(board_state, best_move, player_to_move)

    next_player = "O" if player_to_move == "X" else "X"

    print_board(board_state, next_player)