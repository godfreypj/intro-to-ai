"""
Module: Agent that will solve for the best initial move in a game of scrabble.
Given the Board and a Rack the agent will provide the result and statistics
"""
import scrabble_board


class Agent(scrabble_board.ScrabbleBoard):
    "The Right Move Agent"

    def __init__(self, rack):
        super().__init__()
        self.board = scrabble_board.ScrabbleBoard()
        self.rack = rack

    def solve(self):
        "TODO: Solve the problem"
        return

    def display(self):
        "Print out the state of the board and the rack"
        super().display()
        self.display_rack()

    def display_rack(self):
        "Print out the state of the rack"
        rack_str = ""
        for tile in self.rack:
            rack_str += f"{tile:2}"
        print(f"\nRACK: {rack_str}")
