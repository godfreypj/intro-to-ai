"""
Module: The Board
Description: The Scrabble board to be solved. This is immutable and always
the same for every instance of our Agent. In fact, it's not even a whole
scrabble board because why waste the memory? The starting rack is 7 tiles,
the first move can only be horizontal, so the board is just the middle 13
squares of a standard Scrabble Board
"""


class ScrabbleBoard:
    "Obj representation of the inner 13 horizontal squares of a Scrabble board"

    def __init__(self):
        self.board = ["X"] * 13

    def __iter__(self):
        return iter(self.board)

    def __len__(self):
        return len(self.board)

    def set_cell(self, square, value):
        "Set the contents of a given square with a given value"
        self.board[square] = value

    def display(self):
        "Returns a nicely formatted version of the current board state"
        print("BOARD:")
        print("┏" + "━━━" * len(self.board) + "┓")
        print("┃", end="")
        for cell in self.board:
            print(f" {cell} ", end="")
        print("┃")
        print("┗" + "━━━" * len(self.board) + "┛")
