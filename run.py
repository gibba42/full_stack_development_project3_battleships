from random import randint

board = []

for x in range(6):
    board.append(["~"] * 6)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)