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

# For testing, remove before deploying
print(ship_row)
print(ship_col)

def get_guess():
    guess = input("Guess a square (e.g. A1): ").strip().upper()

    # Must be exactly 2 characters
    if len(guess) != 2:
        print("Please enter a guess like A1.")
        return None

    char1, char2 = guess[0], guess[1]

    # Determine which is letter and which is number
    if char1.isalpha() and char2.isdigit():
        col_char = char1
        row_char = char2
    elif char1.isdigit() and char2.isalpha():
        row_char = char1
        col_char = char2
    else:
        print("Guess must contain one letter and one number (e.g. A1).")
        return None

    # Validate column
    if col_char not in ["A", "B", "C", "D", "E", "F"]:
        print("Column must be between A and F.")
        return None

    # Validate row
    row_num = int(row_char)
    if row_num < 1 or row_num > 6:
        print("Row must be between 1 and 6.")
        return None

    # Convert to 0-based indices
    guess_row = row_num - 1
    guess_col = ["A", "B", "C", "D", "E", "F"].index(col_char)

    return guess_row, guess_col

def game():
    print_board(board)

    for turn in range(6):
        guess = get_guess()
        # If a guess is invalid, don't count the turn
        if guess is None:
            continue

        guess_row, guess_col = guess

        if guess_row == ship_row and guess_col == ship_col:
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