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
        # meat and potatoes as they sayyy
        curr = self.root
        def dfs(curr, j):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if c in curr.children:
                        curr = curr.children[c]
                    else:
                        return False
            return curr.endOfWord
        
        return dfs(curr, 0)
        
