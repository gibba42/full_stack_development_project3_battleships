from random import randint

board = []

for x in range(6):
    board.append(["~"] * 6)

def print_board(board):
    # Print column headers
    print("  A B C D E F")

    # Print each row with a row number
    for i, row in enumerate(board, start=1):
        print(f"{i} " + " ".join(row))

def random_row(board):
    return randint(0, len(board[0]) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

def get_guess():
    row_input = input("Guess row (1-6): ").strip()
    col_input = input("Guess column (A-F): ").strip().upper()

    # Validate row is a number between 1 and 6
    # Validates row is a number first:
    if not row_input.isdigit():
        print("Row must be a number between 1 and 6.")
        return None
    
    # Then validates that it is between 1 and 6:
    row_num = int(row_input)
    if row_num < 1 or row_num > 6:
        print("Please enter a number between 1 and 6.")
        return None
    
    # Validate column is a single letter between A and F
    if len(col_input) != 1 or col_input not in ["A, B, C, D, E, F"]:
        print("Please enter a column letter between A and F.")
        return None
    
    return guess_row, guess_col

def game():
    print_board(board)

    for turn in range(6):
        guess = get_guess()
        # If a guess is invalid, don't count the turn
        if guess is None:
            continue

        guess_row, guess_col = guess

        if guess_row == ship_row and guess_col:
            print("Congratulations! You sunk the battleship!")
            break
        else:
            if board[guess_row][guess_col] == "O":
                print("You already guessed that square.")
            else:
                print("Miss!")
                board[guess_row][guess_col] = "O"

        print_board(board)

game()