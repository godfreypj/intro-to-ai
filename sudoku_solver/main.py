"""
Module: main
Description: main py file, kicks off the program by reading in the given text file
argument. We also keep track of initial values because those are immutable.
The puzzle is then passed to both solvers. The result is passed back and
displayed for the user.
"""
import sys
from board import Board

if len(sys.argv) < 2:
    print("Please provide a Sudoku puzzle file as an argument.")
    sys.exit(1)

PUZZLE_FILE = sys.argv[1]

try:
    with open(PUZZLE_FILE, "r", encoding="utf-8") as file:
        board = Board(PUZZLE_FILE)

    # Check assignment legality and print puzzle content
    board.display()
    if board.update_board(4, 2, "A"):
        print("Legal move!")
        board.display()
    print("Not a legal move")
    board.display()

    if board.goal_test():
        print("puzzle solved!")
    print("not done yet...")

except FileNotFoundError:
    print("File not found:", PUZZLE_FILE)
    sys.exit(1)

# Process the puzzle_content and solve the Sudoku puzzle
# ...
