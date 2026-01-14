def print_board(board, to_move):
    cols = len(board[0])
    for row in board:
        print("|" + "".join(row) + "|")
    print("|" + "".join(str(i) for i in range(cols)) + "|")
    print(f"To move: {to_move}")
    print("Your move?")