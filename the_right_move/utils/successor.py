"""
Module: Successor
Description: The successor function will make our legal placement and 
return the calculation. It's made up of several utility functions.
"""


def is_placement_legal(word, starting_square):
    """Returns true or false if a given word is a legal move"""

    # Checks if the word is at least 2 & no more than 7 letters long
    if len(word) < 2 or len(word) > 7:
        return False

    # Checks if the word covers the center square
    if starting_square + len(word) - 1 == 7:
        return False

    return True
