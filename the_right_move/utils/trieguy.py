"""
Module: TrieGuy
Description: It's called TrieGuy because trueguy.py rhymes and its funny.
This is a trie tree, used to search our scrabble dictionary.
"""


class TrieNode:
    "Instantiate our children and bool flag"

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class TrieGuy:
    "Instantiate our root"

    def __init__(self):
        self.root = TrieNode()

    def build_from_list(self, dictionary):
        "Loads up the tree with our words"
        for word in dictionary:
            self.insert(word)

    def insert(self, word):
        "Inserts our scrabble dictionary into the tree"
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        "Searches the tree for a given word"
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
