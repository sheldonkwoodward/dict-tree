# sheldon woodward
# 3/29/18

"""DictTree Class"""


class DictTree:
    def __init__(self, depth=0):
        """A search tree for verifying words are valid.

        depth (int):
            The depth of the tree. Typically not altered and used internally.
        """
        self.characters = {}
        self.depth = depth
        self.valid = False

    def add_word(self, word):
        """Add a word to the DictTree dictionary.

        word (str):
            The word to be added.
        """
        if self.depth < len(word):
            if word[self.depth] not in self.characters:
                self.characters[word[self.depth]] = DictTree(self.depth + 1)
            self.characters[word[self.depth]].add_word(word)
        else:
            self.valid = True

    def is_word(self, word):
        """Verify a word exists in the dictionary.

        word (str):
            The word to be verified.
        """
        if self.depth < len(word):
            if word[self.depth] not in self.characters:
                return False
            return self.characters[word[self.depth]].is_word(word)
        else:
            return self.valid
