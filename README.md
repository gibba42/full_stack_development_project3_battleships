# Full Stack Development Project 3

## Python Battleship Game

This project is a simple command line Battleship game. 
Languages used: Python. 

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

### Target Audience

### User Stories

## Features:

The site aims to fullfil the above user stories by providing the following features:

## Bugs

| Title | Description | Fix | Status |
|-------|-------------|-----|--------|
| Guesses incorrectly being flagged as invalid | Even when the user enters a valid guess, it is being flagged as invalid. | In progress | Unresolved |
| Win condition set incorrectly | The win condition of the player guessing the ship's row and column was not set properly for its column, meaning that players did not have to guess the column correctly to win. | Updated "if guess_row == ship_row and guess_col" to include "== ship_col" at the end.| Resolved |

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

## Future Improvements
