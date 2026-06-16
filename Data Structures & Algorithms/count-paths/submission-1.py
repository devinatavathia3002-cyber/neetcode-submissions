class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n
        
        # directions = [(0, 1), (1, 0)]
        
        # def dfs(r, c):
        #     if 0 <= r < ROWS and 0 <= c < COLS:
        #         if r == (m - 1) and c == (n - 1):
        #             return 1
                
        #         total = 0
        #         for cord in directions:
        #             x, y = cord
        #             newR = x + r
        #             newC = y + c
        #             total += dfs(newR, newC)
        #         return total
                
        #     else:    
        #         return 0

        # return dfs(0, 0)
        
        # dp solution
        
        dp = [[0] * n for _ in range(m)]
        dp[ROWS - 1][COLS - 1] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                total = 0
                if r + 1 < ROWS:
                    total += dp[r + 1][c]
                if c + 1 < COLS:
                    total += dp[r][c + 1]
                dp[r][c] = total if r != ROWS - 1 else 1

        return dp[0][0]
        
        
        # oldRow = [1] * (n + 1)

        # while m > 1:
        #     newRow = [0] * (n + 1)
        #     for i in range(n - 1, -1, -1):
        #         newRow[i] = oldRow[i] + newRow[i + 1]
        #     oldRow = newRow
        #     m -= 1
        
        # return oldRow[0]
