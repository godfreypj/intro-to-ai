"""
Module: The Board
Description: The Scrabble board to be solved. This is immutable and always
the same for every instance of our Agent. In fact, it's not even a whole
scrabble board because why waste the memory? The starting rack is 7 tiles,
so the board is just the inner 7 Cells of a standard Scrabble Board
"""


class ScrabbleBoard:
    "Obj representation of the inner 7 tiles of a Scrabble board"

    def __init__(self):
        self.board = [["X" for _ in range(7)] for _ in range(7)]

    def __iter__(self):
        return iter(self.board)

    def get_cell(self, row, col):
        "Return the contents of a given cell(row,col)"
        return self.board[row][col]

    def set_cell(self, row, col, value):
        "Set the contents of a given cell(row,col) with a given value"
        self.board[row][col] = value

    def display(self):
        "Returns a nicely formatted version of the current board state"
        for row in self.board:
            for cell in row:
                print(f"{cell:2}", end="")
            print()
