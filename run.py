"""
Import the random module to generate random numbers.
Used to allow the computer to place ships.
"""

import random 

def create_board(size):
    """
    Creates a square game board.
    Each cell is set to '~' to represent water.
    """
    return [['~'] * size for _ in range(size)]

def print_board(board):
    """
    Prints the game board to the console. 
    Each row is printed on a new line. 
    """
    for row in board:
        print(' '.join(row))
    print()

def place_ships(board, num_ships):
    """
    Randomly places a given number of ships on the board.
    Ships are represented by 'S'.
    Ensures ships cannot overlap.
    """
    ships = 0
    while ships < num_ships:
        x, y = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
        if board[x][y] == '~':
            board[x][y] = 'S'
            ships += 1
    
def get_user_guess():
    """
    Asks the user to enter a row and column.
    Repeats until a valid input is
    """
    while True:
        guess = input("Enter your guess (row and column, e.g. 2 3): ").split()
        if len(guess) == 2 and guess[0].isdigit() and guess[1].isdigit():
            return int(guess[0]), int(guess[1])
        else:
            print("Invalid input. Please enter two numbers separated by a space.")
