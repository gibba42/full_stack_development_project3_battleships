from random import randint

board = []

for x in range(6):
    board.append(["~"] * 6)

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board[0]) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

def game():
    for turn in range(6):
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        guess_row -= 1
        guess_col -= 1

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk the battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 6) or (guess_col < 0 or guess_col > 6):
                print("Please enter a guess between 0 and 5.")

            else:
                print("Miss!")
                board[guess_row][guess_col] = "O"
                print("Turn ") + turn
        print_board(board)

game()