"""
Module: Agent that will solve for the best initial move in a game of scrabble.
Given the Board and a Rack the agent will provide the result and statistics
"""
import scrabble_board
from utils.successor import generate_anagrams
import utils.successor as successor
from data.dictionary import dictionary


class Agent(scrabble_board.ScrabbleBoard):
    "The Right Move Agent"

    def __init__(self, rack):
        super().__init__()
        self.board = scrabble_board.ScrabbleBoard()
        self.rack = rack

    def solve(self):
        "Solve"

        # Generate our anagram list
        anagrams = generate_anagrams(self.rack, dictionary)

        # Initialize variables to store the best move information
        best_score = 0
        best_starting_square = None
        best_word = None

        # Determine best move from our anagrams
        for word in anagrams:
            # Get the score and optimal starting square for the current word
            score, starting_square = successor.find_best_move(word)

            # Check if the current word's score is higher than the best score found so far
            if score > best_score:
                best_score = score
                best_starting_square = starting_square
                best_word = word

        # Make the move
        square = best_starting_square
        for letter in best_word:
            self.board.set_cell(square, letter)
            square += 1
        # Return score
        return best_score

    def display(self):
        "Print out the state of the board and the rack"
        super().display()
        self.display_rack()

    def display_rack(self):
        "Print out the state of the rack"
        rack_str = " ".join(f"[{tile}]" for tile in self.rack)
        print("\nRACK:")
        print(" ╔" + "═" * (len(rack_str) + 2) + "╗")
        print(" ║" + rack_str.center(len(rack_str) + 2) + "║")
        print(" ╚" + "═" * (len(rack_str) + 2) + "╝")
