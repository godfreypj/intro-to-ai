"""
Module: successor
Description: checks whether the given value is legal, ie the variable
is assigned such that no row, column, or quadrant contains any duplicate 
characters of the given set."""


def is_assignment_legal(self, row, col, value):
    "Given the board state, returns true if given value is legal"

    # Check if cell contains an initial value
    if self.initial_values[row][col]:
        return False

    # Convert the value to uppercase
    value = value.upper()

    # Check row
    for board_col, row_value in enumerate(self.puzzle[row]):
        if board_col != col and str(row_value).upper() == value:
            return False

    # Check column
    for board_row, board_values in enumerate(self.puzzle):
        if board_row != row and str(board_values[col]).upper() == value:
            return False

    # Check quadrant
    quadrant_size = int(len(self.puzzle) ** 0.5)
    start_row = (row // quadrant_size) * quadrant_size
    start_col = (col // quadrant_size) * quadrant_size
    for quadrant_row in range(start_row, start_row + quadrant_size):
        for quadrant_col in range(start_col, start_col + quadrant_size):
            if (quadrant_row != row or quadrant_col != col) and str(
                self.puzzle[quadrant_row][quadrant_col]
            ).upper() == value:
                return False

    return True
