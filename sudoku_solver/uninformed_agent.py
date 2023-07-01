class UninformedAgent:
    """Uninformed Agent for solving Sudoku puzzles using backtracking."""

    def __init__(self, board):
        self.board = board
        self.size = len(board.get_puzzle())
        self.quadrant_size = int(self.size**0.5)

    def solve(self):
        """Solves the Sudoku puzzle using backtracking."""
        return self.backtrack_solver()

    def backtrack_solver(self):
        """Recursive backtracking algorithm to solve the puzzle."""
        if self.is_solution_found():
            return True

        row, col = self.select_unassigned_variable()
        if row == -1 and col == -1:
            return False

        for num in range(1, self.size + 1):
            num = str(num)
            if self.board.is_assignment_legal(row, col, num):
                self.board.update_board(row, col, num)

                if self.backtrack_solver():
                    return True

                self.board.update_board(row, col, "-")

        return False

    def is_solution_found(self):
        """Check if a valid solution has been found."""
        for row in range(self.size):
            for col in range(self.size):
                if self.board.goal_test():
                    return False
        return True

    def select_unassigned_variable(self):
        """Selects the next unassigned variable (cell) in the puzzle."""
        for row in range(self.size):
            for col in range(self.size):
                if self.board.get_puzzle()[row][col] == "-":
                    return row, col

        return -1, -1
