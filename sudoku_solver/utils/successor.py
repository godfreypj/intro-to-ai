"""
Module: successor
Description: checks whether the given value is legal, ie the variable
is assigned such that no row, column, or quadrant contains any duplicate 
characters of the given set."""


def is_assignment_legal(board, initial_values, row, col, value):
    "Given the board state, returns true if given value is legal"

    # Check if cell contains an initial value
    if initial_values[row][col]:
        return False

    value = value.upper()  # Convert the value to uppercase

    # Check row
    for board_col, row_value in enumerate(board[row]):
        if board_col != col and str(row_value).upper() == value:
            return False

    # Check column
    for board_row, board_values in enumerate(board):
        if board_row != row and str(board_values[col]).upper() == value:
            return False

    # Check quadrant (fixed 4x4 size)
    start_row = (row // 4) * 4
    start_col = (col // 4) * 4
    for r in range(start_row, start_row + 4):
        for c in range(start_col, start_col + 4):
            if (r != row or c != col) and str(board[r][c]).upper() == value:
                return False

    return True
