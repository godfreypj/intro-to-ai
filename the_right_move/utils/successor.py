"""
Module: Successor
Description: The successor function will make our legal placement and 
return the calculation. It's made up of several utility functions.
"""

# pylint: disable=import-error
from utils.trieguy import TrieGuy
from utils.points import scores


def is_placement_legal(word, starting_square):
    """Returns true or false if a given word is a legal move"""

    # Starting square must be less than or equal to the center
    if starting_square > 7:
        return False

    # Calculate the length of the word
    word_length = len(word)

    # Determine the index of the center square (element 6) relative to the word's starting square
    center_index = 6 - starting_square

    # Check if the center square is within the bounds of the word's length
    if center_index < 0 or center_index >= word_length:
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


def estimate_score(word):
    "Given a rack with a word on it, return the estimated score"
    letter_scores = [scores.get(letter.upper(), 0) for letter in word]

    # Double the letter with the highest score
    max_score = max(letter_scores)
    estimated_points = sum(letter_scores) + max_score

    # Add 50 for using 7 letters
    if len(word) > 6 and "_" not in word:
        estimated_points += 50

    return estimated_points


def generate_anagrams(rack, dictionary):
    """Takes our rack and the scrabble dictionary and returns a list
    of valid anagrams"""

    trie = TrieGuy()
    trie.build_from_list(dictionary)

    max_score = estimate_score(rack)

    def backtrack(letters, path):
        word = "".join(path)
        if len(word) > 1 and trie.search(word):
            score = estimate_score(word)
            if score >= max_score * 0.8:
                anagrams.append((word))

        for i, char in enumerate(letters):
            if char == "_":
                for common_char in "AEIOULNRDBCGMFHPSVWYJQKZ":
                    path.append(common_char)
                    backtrack(letters[:i] + letters[i + 1 :], path)
                    path.pop()
            else:
                path.append(char)
                backtrack(letters[:i] + letters[i + 1 :], path)
                path.pop()

    anagrams = []
    backtrack(rack, [])
    return anagrams


def find_best_move(word):
    "Given a word, return the optimal move (score, starting square)"

    # If the word is less than 4 char, it must start on the center square
    if len(word) < 4:
        starting_square = 5
        max_square_score = calculator(word, starting_square)
        return (max_square_score, starting_square)

    # Find the letter with the highest score
    max_score = 0
    highest_scoring_letter_index = None
    for i, letter in enumerate(word):
        score = scores.get(letter.upper())
        if score > max_score:
            max_score = score
            highest_scoring_letter_index = i

    # Find the double letter square that provides the highest score
    max_square_score = 0
    optimal_starting_square = None
    for i in [2, 10]:
        # Check if placing the highest-scoring letter on this square is legal
        start_index = i - highest_scoring_letter_index
        if is_placement_legal(word, start_index):
            # Calculate the score of this move
            square_score = calculator(word, start_index)
            if square_score > max_square_score:
                max_square_score = square_score
                optimal_starting_square = start_index

    return (max_square_score, optimal_starting_square)
