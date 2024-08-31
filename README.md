# Sudoku Game - Built from Scratch (Currently implementing pygames for UI)
## Overview
This project is a fully functioning Sudoku game implemented in Python. The game generates a random Sudoku puzzle using backtracking and ensures that the puzzle has only one unique solution also using naive backtracking. The user can solve the puzzle through console input, and the game provides feedback on the validity of the moves and whether the puzzle has been successfully completed.

## Features
Random Sudoku Board Generation: The game generates a Sudoku board using a random backtracking algorithm to place numbers on the grid.
Unique Solution Guarantee: The game uses naive backtracking to ensure that the generated puzzle has only one solution.
User Input: The player can input numbers to solve the puzzle. The game checks the validity of the move (e.g., ensuring the number isn't already in the row, column, or 3x3 grid).
Win Detection: The game detects when the puzzle is successfully solved and declares the user as the winner.
Customizable Difficulty: The user is prompted to type in either easy medium or hard to declare difficulty type
Color Output: The game uses colored output (through the color class) to differentiate between user-placed numbers and the initial board setup.
