class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited, output = set(), set()

        root = TrieNode()
        for word in words:
            root.addWord(word)

        def dfs(r, c, node, word):
            char = board[r][c]
            word += char

            # nextNode = node.children[char]

            if len(output) == len(words):
                return
            if node.endOfWord:
                output.add(word)
            
            for cord in directions:
                x, y = cord
                newR, newC = x + r, y + c
                if 0 <= newR < ROWS and 0 <= newC < COLS and (newR, newC) not in visited and board[newR][newC] in node.children:
                    visited.add((newR, newC))
                    dfs(newR, newC, node.children[board[newR][newC]], word)
                    visited.remove((newR, newC))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    visited.add((r, c))
                    dfs(r, c, root.children[board[r][c]], "")
                    visited.remove((r, c))

        return list(output)