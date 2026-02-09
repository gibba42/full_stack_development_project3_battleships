# Import random to allow the computer to randomly place ships
from random import randint

board = []

"""
Sets the board to 6 X 6. 
Sets the cells to '~' for water.
Will change this later to allow the user to set the size.
"""
for x in range(6):
    board.append(["~"] * 6)

def print_board(board):
    for row in board:
        print((" ").join(row))

# Game start message
print("Let's play Battleship!")
print_board(board)

"""
Randomly places ships.
Might change this later so that ships can be multiple cells long.
"""
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Allows the user 9 guesses
for turn in range(9):
    print ("Turn"), turn
    guess_row = int(input("Guess Row:")) # Asks user to guess a row
    guess_col = int(input("Guess Col:")) #Asks user to guess a column
    # Might change this to ask in one go, this is clunky

    # Checks if user guessed a cell with a ship in it
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        # Checks if guess was on the board. Will change this so that users cannot make invalid guesses.
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            # Checks if guess was on a 'hit' cell
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    if turn == 8:
        print("Game Over")
    turn =+ 1
    print_board(board)