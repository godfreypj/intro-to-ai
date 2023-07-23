# Overview

## The 'Right' Move

### This program will take a 'rack' and return the best first move in Scrabble

<hr>

### Quick Start:

- python > v3
- Navigate to the `the_right_move` directory and run `python main.py <rack.txt>`
- Example: `python main.py racks/rack_1.txt`

### Overview:

The goal of this app is to develop an `agent` to find the optimal **initial** move of a Scrabble game, given the following inputs:

- An empty Scrabble board.
  - Assume the agent knows how the premium squares work & locations.
- The complete SOWPODS word list, containing all 267,751 legal words.
- A collection of 7 tiles in the agent’s rack.
  - At most 2 may be wildcard tiles.
  - `rack` is represented by one line of a flat text file, uppcase letters used to represent A-Z and an `_` underscore character to represent a `wildcard`

We should be outputting the `rack` (starting 7), the `board` the `points` total, and the `elapsed_time` it took to get the answer back to the user.

### Board:

- The board is 13 `squares` in order to minimize complexity; the rules state the first move must cover the middle square and with a max word size of 7 `tiles` the board only needs to be 13 elements
- Included is a `set_cell` function to place the word, and `display` to show the state of the board

### Agent:

- The Agent is responsible for arriving at the goal. It instantiates the `board` the `rack` and also contains a `display` function for displaying the rack.
- The `solve` functions runs through the `successor` module and solves the board:
  - `generate_anagrams` instantiates the `TrieGuy` which is a prefix-tree that holds the official scrabble dictionary. In this data structure all words with common roots share common nodes. This significantly reduces the search time to find a legal word.
  - A blank tile (`_`) can be any letter but some letters are better than others. The order of letters chosen is weighted as 60% score and 40% commonality in the english language.
  - As anagrams are generated the function uses `estimate_score` to compare the estimated maximum score of the rack to the estimated score of a given anagram; if the word is at least 40% of `max_score` it is added to the `anagrams`. This eliminates the need to `set_cell` and actually calculate the score for each potential word & significantly reduces the `anagrams` list
  - The final `anagrams` list is then iterated over and the `find_best_move` function decides where to place it using these rules:
    - If the word is less than 4 characters, it must start on the center tile
    - Put the highest scoring letter on the double letter tile such that a legal move is produced
  - The scores resulting from `find_best_move` are compared and the highest scoring move is chosen
  - Results are displayed to the user

### Main

- `main` kicks off the application by reading in a `racks` file that is a set of 7 scrabble letters. Each set is separated by a new line.
- Each `rack` is accompanied by an agent who is instantiated and the `best_move` is found.
