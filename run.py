from random import randint

LETTERS = ["A", "B", "C", "D", "E", "F"]

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
    if col_char not in LETTERS:
        print("Column must be between A and F.")
        return None

    # Validate row
    row_num = int(row_char)
    if row_num < 1 or row_num > 6:
        print("Row must be between 1 and 6.")
        return None

    # Convert to 0-based indices
    guess_row = row_num - 1
    guess_col = LETTERS.index(col_char)

    return guess_row, guess_col

def game():
    print_board(board)

    turns_used = 0
    max_turns = 6

    while turns_used < max_turns:
        print(f"\nTurn {turns_used + 1} of {max_turns}")

        guess = get_guess()
        if guess is None:
            continue  # invalid input doesn't cost a turn

        guess_row, guess_col = guess

        # Duplicate guess check (doesn't cost a turn)
        if board[guess_row][guess_col] == "O":
            print("You already guessed that square. Try a different one.")
            continue

        # Only now do we count the turn (valid + new guess)
        turns_used += 1

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk the battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)
            break
        else:
            print("Miss!")
            board[guess_row][guess_col] = "O"

        print_board(board)

    else:
        print("\nGame over! You ran out of turns.")
        print(f"The ship was at {LETTERS[ship_col]}{ship_row + 1}")

game()