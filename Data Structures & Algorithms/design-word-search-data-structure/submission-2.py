class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(curr, index):
            for i in range(index, len(word)):
                letter = word[i]
                if letter == '.':
                    for c in curr.children:
                        if dfs(curr.children[c], i + 1):
                            return True
                    return False
                else:
                    if letter not in curr.children:
                        return False
                    curr = curr.children[letter]
            return curr.endOfWord
        
        return dfs(curr, 0)
        
