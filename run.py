"""Project 3 - Battleship game.

A simple version of the game Battleship.
3 ships have been hidden on a 6 X 6 grid.
Players have 12 guesses to find them.
The program will validate guesses for valid formatting.
The program will show the results on the grid after each guess.
If the player hits all three ships, they win.
If the player fails to hit all three ships after 12 guesses, they lose.
Players can leave the game at any time by entering "EXIT" as a guess.
"""

from random import randint

try:  # Optional, rich for better formatting
    from rich.console import Console
    from rich.table import Table

    RICH_AVAILABLE = True
    console = Console()
except ImportError:
    RICH_AVAILABLE = False
    console = None

LETTERS = ["A", "B", "C", "D", "E", "F"]
NUM_SHIPS = 3

board = []

for x in range(6):
    board.append(["~"] * 6)


def print_board(board):
    if RICH_AVAILABLE:
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column(" ")
        for letter in LETTERS:
            table.add_column(letter)

        for i, row in enumerate(board, start=1):
            styled_row = []
            for cell in row:
                if cell == "X":
                    styled_row.append("[bold red]X[/]")
                elif cell == "O":
                    styled_row.append("[blue]O[/]")
                elif cell == "S":
                    styled_row.append("[yellow]S[/]")
                else:
                    styled_row.append("~")
            table.add_row(str(i), *styled_row)

        console.print(table)
        return

    # Fallback: plain text board
    print("  " + " ".join(LETTERS))
    for i, row in enumerate(board, start=1):
        print(f"{i} " + " ".join(row))



def place_ships(num_ships):
    """Places 3 ships on the grid at random.

    Ships cannot overlap.
    """
    # Generate three, unique ship placements:
    ships = set()
    while len(ships) < num_ships:
        r = randint(0, 6 - 1)
        c = randint(0, 6 - 1)
        ships.add((r, c))
    return ships


ships = place_ships(NUM_SHIPS)


def get_guess():
    """Ask the player to guess a square, and validate it.

    Also includes the logic for 'special' guesses such as:
    "EXIT" which leaves the game
    "SONAR" which reveals one remaining ship
    """
    guess = input("Guess a square (e.g. A1): \n").strip().upper()

    if guess == "EXIT":
        return "EXIT"

    if guess == "SONAR":
        return "SONAR"

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
    """Run the game.

    Explain the rules of the game, and then start a turn.
    Count and display the number of turns used.
    Handle the win / loss logic.
    """
    print("Welcome to Battleship!\nThe computer has hidden three ships.")
    print("You have 12 turns to guess where they are.")
    print("If you hit a ship, the cell will be replaced with an X.")
    print("If you miss, the cell will be replaced with an O.\nGood luck!")
    print("Hint: SONAR can help you find ships.")
    print("You can enter 'EXIT' as a guess to leave.")
    print_board(board)

    turns_used = 0
    max_turns = 12
    hits = set()
    sonar_used = False

    while turns_used < max_turns:
        print(f"\nTurn {turns_used + 1} of {max_turns}")

        guess = get_guess()
        if guess is None:
            continue  # invalid input doesn't cost a turn

        if guess == "EXIT":
            print("You exited the game.")
            return

        """
        SONAR easter egg guess
        If the player types SONAR, it will reveal the location of a ship.
        SONAR can only be used once per game.
        """
        if guess == "SONAR":
            if sonar_used:
                print("You have already used SONAR this game.")
                continue  # Doesn't cost a turn

            sonar_used = True
            # Find a remaining ship
            remaining_ships = ships - hits
            r, c = next(iter(remaining_ships))
            print(f"There is a ship in {LETTERS[c]}{r + 1}")

            continue  # Doesn't cost a turn

        guess_row, guess_col = guess

        # Duplicate guess check (doesn't cost a turn)
        if board[guess_row][guess_col] == "O":
            print("You already guessed that square. Try a different one.")
            continue

        if (guess_row, guess_col) in ships:
            print("Hit! Guess again.")
            board[guess_row][guess_col] = "X"
            hits.add((guess_row, guess_col))

            if len(hits) == NUM_SHIPS:
                print("You hit all the ships. You win!")
                print_board(board)
                return

        else:
            print("Miss!")
            board[guess_row][guess_col] = "O"
            turns_used += 1

        print_board(board)

    else:
        for (r, c) in ships:
            if (r, c) not in hits and board[r][c] == "~":
                board[r][c] = "S"
        print("\nGame over! You ran out of turns.")
        print("\nHere are the remaining ships:")
        print_board(board)


game()
