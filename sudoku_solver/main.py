"""
Module: main
Description: main py file, kicks off the program by reading in the given text file
argument. We also keep track of initial values because those are immutable.
The puzzle is then passed to both solvers. The result is passed back and
displayed for the user.
"""
import sys
from board import Board
from uninformed_agent import UninformedAgent

sys.setrecursionlimit(100000)

if len(sys.argv) < 2:
    print("Please provide a Sudoku puzzle file as an argument.")
    sys.exit(1)

PUZZLE_FILE = sys.argv[1]

try:
    with open(PUZZLE_FILE, "r", encoding="utf-8") as file:
        board = Board(PUZZLE_FILE)

    try:
        # Check assignment legality and print puzzle content
        print("==__== ... Dumb Agent attempt to solve ... ==__==\n")
        print("Board: \n")
        board.display()
        print("Set: \n")
        print(board.get_variable_set())
        sys.stdout.write("\r            \n")
        un_agent = UninformedAgent(board)
        if un_agent.solve():
            board.display()
            print("Solved!")
        else:
            print("Unsolvable")
            board.display()
    except RecursionError:
        # Clear the blinking cursor
        sys.stdout.write("\r            \n")
        print("Recursion error occurred")
        print("Current state of the board:")
        board.display()

except FileNotFoundError:
    print("File not found:", PUZZLE_FILE)
    sys.exit(1)

# Process the puzzle_content and solve the Sudoku puzzle
# ...
