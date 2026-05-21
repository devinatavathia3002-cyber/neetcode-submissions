class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows 
                or c >= cols or board[r][c] == 'X'
                or board[r][c] == 'S'):

                return
            
            board[r][c] = 'S'

            for num in directions:
                x, y = num
                dfs(r + x, c + y)
        

        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
                else:
                    continue