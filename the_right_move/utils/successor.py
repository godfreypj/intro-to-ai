"""
Module: Successor
Description: The successor function will make our legal placement and 
return the calculation. It's made up of several utility functions.
"""

# pylint: disable=import-error
from utils.points import scores


def is_placement_legal(word, starting_square):
    """Returns true or false if a given word is a legal move"""

    # Checks if the word is at least 2 & no more than 7 letters long
    if len(word) < 2 or len(word) > 7:
        return False

    # Checks if the word covers the center square
    if starting_square + len(word) - 1 == 7:
        return False

    return True


double_letter_squares = {2, 10}


def calculator(word, starting_square):
    "Given a board with a word on it, return the score"
    letter_scores = [scores.get(letter.upper(), 0) for letter in word]

    for index, letter in enumerate(word):
        if starting_square in double_letter_squares:
            letter_scores[index] *= 2
        starting_square += 1

    # Calculate the total score using the built-in sum() function
    total_points = sum(letter_scores)

    if len(word) == 7:
        total_points += 50

    return total_points
