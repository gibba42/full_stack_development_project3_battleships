from random import randint

LETTERS = ["A", "B", "C", "D", "E", "F"]
NUM_SHIPS = 3

board = []

for x in range(6):
    board.append(["~"] * 6)

def print_board(board):
    # Print column headers
    print("  A B C D E F")

    # Print each row with a row number
    for i, row in enumerate(board, start=1):
        print(f"{i} " + " ".join(row))

def place_ships(num_ships):
    # Generate three, unique ship placements:
    ships = set()
    while len(ships) < num_ships:
        r = randint(0, 6 - 1)
        c = randint(0, 6 - 1)
        ships.add((r, c))
    return ships

ships = place_ships(NUM_SHIPS)

# For testing, remove before deploying
print("Ships:", ships)

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
    print("Welcome to Battleship! The computer has hidden three ships.")
    print("\nYou have 10 turns to guess where they are.\nIf you hit a ship, the cell will be replaced with an X.")
    print("\nf you miss, the cell will be replaced with an O.\nGood luck!")
    print_board(board)

    turns_used = 0
    max_turns = 10
    hits = set()

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

        # Increase turn counter on valid guess:
        turns_used += 1

        if (guess_row, guess_col) in ships:
            print("Hit!")
            board[guess_row][guess_col] = "X"
            hits.add((guess_row, guess_col))

            if len(hits) == NUM_SHIPS:
                print("You hit all the ships. You win!")
                print_board(board)
                return
            
        else:
            print("Miss!")
            board[guess_row][guess_col] = "O"

        print_board(board)

    else:
        for (r, c) in ships:
            if (r, c) not in hits and board[r][c] == "~":
                board[r][c] = "S"
        print("\nGame over! You ran out of turns.")
        print("\nHere are the remaining ships:")
        print_board(board)

game()