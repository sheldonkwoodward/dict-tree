# sheldon woodward
# 3/29/18


class DictTree:
    def __init__(self, depth=0):
        """A search tree """
        self.characters = {}
        self.depth = depth
        self.valid = False

    def add_word(self, word):
        if self.depth < len(word):
            if word[self.depth] not in self.characters:
                self.characters[word[self.depth]] = DictTree(self.depth + 1)
            self.characters[word[self.depth]].add_word(word)
        else:
            self.valid = True

    def is_word(self, word):
        if self.depth < len(word):
            if word[self.depth] not in self.characters:
                return False
            return self.characters[word[self.depth]].is_word(word)
        else:
            return self.valid
