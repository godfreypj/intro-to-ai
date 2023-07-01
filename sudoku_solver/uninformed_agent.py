"""
Module: uninformed agent
Description: the agent that attempts to solve the puzzle by starting with the first
empty cell and progressing from left to right, top to bottom. This is considered
the default variable selector
"""


class UninformedAgent:
    """Uninformed Agent for solving Sudoku puzzles using backtracking."""

    def __init__(self, board):
        self.board = board
        self.action_count = 0

    def solve(self):
        "Solves the Sudoku puzzle using backtracking."
        return self.dfs(0, 0)

    def dfs(self, row, col):
        "Recursive backtracking algorithm to solve the puzzle."
        if self.board.goal_test():
            return True

        next_row = row
        next_col = col + 1
        if next_col == len(self.board.puzzle):
            next_row += 1
            next_col = 0

        if self.board.initial_values[row][col]:
            return self.dfs(next_row, next_col)

        for value in self.board.variable_set:
            if self.board.is_assignment_legal(row, col, value):
                self.action_count += 1
                self.board.update_board(row, col, value)
                if self.dfs(next_row, next_col):
                    return True
                self.board.update_board(row, col, "-")
        return False
