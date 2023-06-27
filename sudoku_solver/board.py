"""
Module: Board
Description: A module to represent the 4x4 Super Sudoku board.
It contains getters and setters for the board and initial_values.
It contains a function to update the board and to display the board
"""

from utils.successor import is_assignment_legal


class Board:
    "Super Sudoku board object"

    def __init__(self, puzzle_file):
        with open(puzzle_file, "r", encoding="utf-8") as file:
            # Read in the argument
            puzzle_content = file.readlines()

        # Convert puzzle_content to a 2D list (board) and create initial_values data structure
        self.puzzle = []
        self.initial_values = []
        for line in puzzle_content:
            row = [char for char in line.strip() if char != " "]
            self.puzzle.append(row)
            initial_row = [char != "-" for char in row]
            self.initial_values.append(initial_row)

    def get_initial_values(self):
        "Initial values of the puzzle are immutable, lets keep track of them"
        return self.initial_values

    def get_puzzle(self):
        "Returns the current state of the puzzle"
        return self.puzzle

    def update_board(self, row, col, value):
        "Update the board with the given value"
        if self.is_assignment_legal(row, col, value):
            self.puzzle[row][col] = value
            return True
        return False

    def goal_test(self):
        "Check if the board is in a complete state"
        for row in self.puzzle:
            for value in row:
                if value == "-":
                    return False
        return True

    def display(self):
        "Display the current state of the board"
        for row in self.puzzle:
            print(" ".join(row))

    is_assignment_legal = is_assignment_legal
