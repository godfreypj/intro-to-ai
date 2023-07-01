"""
Module: Board
Description: A module to represent the 4x4 Super Sudoku board.
It contains getters and setters for the board and initial_values.
It contains a function to update the board and to display the board
"""

from utils.successor import is_assignment_legal


class Board:
    """Super Sudoku board object.
    Attributes: puzzle, initial_values, variables_set
    Functions: getters/setters, update_board, goal_test
    is_assignment_legal, display.
    """

    def __init__(self, puzzle_file):
        with open(puzzle_file, "r", encoding="utf-8") as file:
            # Read in the argument
            puzzle_content = file.readlines()

        self.puzzle = []
        self.initial_values = []
        self.variable_set = set()
        for line in puzzle_content:
            row = [char for char in line.strip() if char != " "]
            self.puzzle.append(row)
            initial_row = [char != "-" for char in row]
            self.initial_values.append(initial_row)
            for char in row:
                if char != "-":
                    self.variable_set.add(char)

    def get_initial_values(self):
        "Initial values of the puzzle are immutable, lets keep track of them"
        return self.initial_values

    def get_variable_set(self):
        "16 unique characters for this puzzle"
        return self.variable_set

    def get_puzzle(self):
        "Returns the current state of the puzzle"
        return self.puzzle

    def update_board(self, row, col, value):
        "Update the board with the given value"
        if value != "-" and not self.is_assignment_legal(row, col, value):
            return False
        self.puzzle[row][col] = value
        return True

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
