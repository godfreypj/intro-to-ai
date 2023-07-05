# Overview

### This program will solve a 4 x 4 “Super” Sudoku puzzle.

<hr>

#### The Sudoku puzzle is defined as:

- The environment:

  - A 4x4 cells make up a quadrant, the board is 4x4 quadrants

- The set:

  - Any set of 16 unique characters

- The initial state:

  - Each section of 4x4 cells has an initial clue value of 4-10; any smaller and its unsolvable and any larger it’s too easy. The initial state is stored as the initial values cannot be changed.

- The goal:

  - All cells are filled in such that no row, column, or quadrant contains any duplicate characters of the given set.

  <hr>

#### The program shall:

- Read a Super Sudoku puzzle from a text file. The user should be able to browse the file system to select this file.
- The initial puzzle - following the rules as stated above - consists of a text file where each character is represented by itself or a `-` (dash mark): filled or empty. New lines indicate the start of a new row.
- Solve the puzzle using 2 separate agents:
  1. Uninformed agent solving the puzzle from left-to-right & top-to-bottom.
  2. A CSP agent using Minimum Remaining Value Hueristic:
     1. variable assignments are in order of _increasing_ possible values
     2. possible values are determined by comparing the row, column and quadrant in common with the given variable to the domain to find available characters.
- Keep track of the relative effectiveness of both agents:
  - count of total variable assignements
  - running time to solve

<hr><hr>

## Quick Start

Requirements:

- python > v3

Running:

- Navigate to the `sudoku_solver` directory. Run: `python main.y <puzzle>`
