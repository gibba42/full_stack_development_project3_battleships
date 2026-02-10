# Full Stack Development Project 3

## Python Battleship Game

![Python Battleship Game](assets/images/battleship_banner.png)

This project is a simple command line Battleship game built in Python.

## Table of contents:
1. [**Live Site**](#live-site)
1. [**Project Purpose**](#project-purpose)
    * [***Target Audience***](#target-audience)
    * [***User Stories***](#user-stories)
1. [**Features**](#features)
1. [**Bugs**](#bugs)
1. [**Testing**](#testing)
    * [***Manual Testing***](#manual-testing)
    * [***Automated Testing***](#automated-testing)
1. [**Deployment**](#deployment)
    * [***Deployment Steps***](#deployment-steps)
1. [**Credits**](#credits)
1. [**Future Improvements**](#future-improvements)


## Live Site

## Project Purpose

The purpose of this project is to create an interative Python program that allows users to play a simple version of the "Battleship" game against a computer.

## Rules

The program will hide 3 ships randomly on a 6 X 6 grid. The player then has 12 turns to guess where they are. 

- Hits are marked as an "X" on the board. 
- Misses are marked with an "O". 
- The player must hit all three vessels to win. 
- There is a hint in the starting instructions to increase your odds.

### Target Audience

### User Stories

As 

## Features:

### Game board





## Bugs

| Title | Description | Fix | Status |
|-------|-------------|-----|--------|
| Guesses incorrectly being flagged as invalid | Even when the user enters a valid guess, it is being flagged as invalid. | Updated the get_guess function so that users can guess in a more intuitive "cell" system, i.e. A1 rather than row 1, column 1. Updated the validation rules so that validation occurs on 0 indexed versions of these guesses. | Resolved |
| Win condition set incorrectly | The win condition of the player guessing the ship's row and column was not set properly for its column, meaning that players did not have to guess the column correctly to win. | Updated "if guess_row == ship_row and guess_col" to include "== ship_col" at the end.| Resolved |
| Turn counter starts an infinite loop | The turn counter causes an infinite loop that will eventually crash the program. | The loop was caused because the turn counter was indented incorrectly. It was running when turns was less than the max amount allowed without allowing the turn counter to increase. The function is now properly indented. | Resolved |
| SONAR easter egg always reveals the exact location of a ship | The SONAR guess is intended to show the correct column of one ship, and the correct row of another. At the moment it shows the exact location of one ship instead. | Could not fix. Instead changed the feature so that it does show the exact location of a ship, but the player can only use it once per game. | Resolved, feature changed |

## Testing

The project has been thoroughly tested, both manually and using automated tests. 

### Manual Testing

| Feature | Action | Expected Result | Actual Result | Pass/Fail |
|------|------|------|------|------|



### Automated testing

## Deployment

This project was deployed using **GitHub Pages**.

### Deployment Steps
1. Push final code to GitHub repository
2. Navigate to **Settings → Pages**
3. Select the `main` branch as the source
4. Save and wait for deployment to complete
5. Access the live site via the provided URL

## Credits

Inspiration and help building the functions was taken from:

1. "Let's build a simple "Battleship" game from pyshine.com/Make-a-battleship-game/
2. "Python battleship program (2player or 1 player) from Stack Exchange user Dakota Vaughn on codereview.stackexhange.com

## Future Improvements

1. Make the ships different sizes (i.e. two consecutive cells long).
2. Make the SONAR easter egg reveal the row of one remaining ship, and the column of another.
3. Add a "Play again?" loop.
4. Let the player place ships, and let the computer try and guess their location. 
