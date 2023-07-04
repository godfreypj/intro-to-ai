"""
Module: informed agent
Description: This CSP agent will use the MRV heuristic to reduce the size of the search space.
The order of cells assigned using this heuristic is in order of increasing number of possible 
values. The number of possible values for a given cell is determined by looking at the row,
column, and box that have that cell in common, and subtracting from the set size the number
of unique values that are already present. The range is 1 to the set size."""


class InformedAgent:
    """Informed Agent for solving Sudoku puzzles using backtracking and MRV heuristic."""

    def __init__(self, board):
        self.board = board
        self.action_count = 0

    def solve(self):
        """Solves the Sudoku puzzle using backtracking and MRV heuristic."""
        return self.dfs()

    def dfs(self):
        "Recursive backtracking algorithm to solve the puzzle with MRV heuristic."
        if self.board.goal_test():
            return True

        row, col = self.select_ideal_variable()
        possible_values = self.get_ideal_values(row, col)

        for value in possible_values:
            self.action_count += 1
            self.board.update_board(row, col, value)

            if self.dfs():
                return True

            self.board.update_board(row, col, "-")

        return False

    def select_ideal_variable(self):
        "Selects the next unassigned variable using the MRV heuristic."
        min_values = float("inf")
        selected_row, selected_col = -1, -1

        for row_index, row in enumerate(self.board.puzzle):
            for col_index, cell_value in enumerate(row):
                if cell_value == "-":
                    values = self.get_ideal_values(row_index, col_index)
                    if len(values) < min_values:
                        min_values = len(values)
                        selected_row, selected_col = row_index, col_index

        return selected_row, selected_col

    def get_ideal_values(self, row, col):
        "Gets the possible values for a given cell based on row, column, and box constraints."
        values = set(self.board.variable_set)
        values -= set(self.board.get_row(row))
        values -= set(self.board.get_column(col))
        values -= set(self.board.get_quadrant(row, col))
        return list(values)
