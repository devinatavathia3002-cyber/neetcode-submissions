class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row, col, index):

            if index >= len(word):
                return True
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            
            if board[row][col] != word[index]:
                return False
            
            board[row][col] = '#'
            
            found = (dfs(row + 1, col, index + 1) or
                    dfs(row - 1, col, index + 1) or
                    dfs(row, col + 1, index + 1) or
                    dfs(row, col - 1, index + 1))
            
            board[row][col] = word[index]
            return found
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
        
