"""
Module: main
Description: main py file, kicks off the program by reading in the given text file
argument. We also keep track of initial values because those are immutable.
The puzzle is then passed to both solvers. The result is passed back and
displayed for the user.
"""
import sys
from utils.successor import is_assignment_legal

if len(sys.argv) < 2:
    print("Please provide a Sudoku puzzle file as an argument.")
    sys.exit(1)

PUZZLE_FILE = sys.argv[1]

try:
    with open(PUZZLE_FILE, "r", encoding="utf-8") as file:
        # Read in the argument
        puzzle_content = file.readlines()

    # Convert puzzle_content to a 2D list (board) and create initial_values data structure
    board = []
    initial_values = []
    for line in puzzle_content:
        row = [char for char in line.strip() if char != " "]
        board.append(row)
        initial_row = [char != "-" for char in row]
        initial_values.append(initial_row)

    # Check assignment legality and print puzzle content
    print(is_assignment_legal(board, initial_values, 4, 0, "3"))
    print(board)

except FileNotFoundError:
    print("File not found:", PUZZLE_FILE)
    sys.exit(1)

# Process the puzzle_content and solve the Sudoku puzzle
# ...
