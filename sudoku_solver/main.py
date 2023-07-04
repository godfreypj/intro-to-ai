"""
Module: main
Description: main py file, kicks off the program by reading in the given text file
argument. We also keep track of initial values because those are immutable.
The puzzle is then passed to both solvers. The result is passed back and
displayed for the user.
"""
import sys
import time
from board import Board
from informed_agent import InformedAgent
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
        # Give user some feedback; time and actions taken
        print("==__== ... Agent attempt to solve ... ==__==\n")
        print("Board: \n")
        board.display()
        print("\nSet: \n")
        print(board.get_variable_set())
        sys.stdout.write("\r            \n")
        # un_agent = UninformedAgent(board)
        agent = InformedAgent(board)
        start_time = time.time()
        if agent.solve():
            board.display()
            print("Solved!")
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            print(f"Action count: {agent.action_count}")
        else:
            print("Unsolvable")
            board.display()

    except RecursionError:
        sys.stdout.write("\r            \n")
        print("Recursion error occurred")
        print("Current state of the board:")
        board.display()

except FileNotFoundError:
    print("File not found:", PUZZLE_FILE)
    sys.exit(1)
