class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        # recursive implementation
        # def recurse(r, c):
        #     if r == ROWS - 1 and c == COLS - 1:
        #         return grid[r][c]
        #     if 0 <= r < ROWS and 0 <= c < COLS:
        #         down = grid[r][c] + recurse(r + 1, c)
        #         right = grid[r][c] + recurse(r, c + 1)

        #     else:
        #         return float('inf')
        #     return min(down, right)

        # return recurse(0, 0)

        # dp solution
        # n = cols, m = rows
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        dp[ROWS - 1][COLS - 1] = grid[ROWS - 1][COLS - 1]

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1: 
                    continue
                down, right = float('inf'), float('inf')
                if r < ROWS - 1:
                    down = dp[r + 1][c]
                if c < COLS - 1:
                    right = dp[r][c + 1]
                dp[r][c] = grid[r][c] + min(down, right)

        return dp[0][0]                    