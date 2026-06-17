class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        # with dfs (recursive)
        # def dfs(r, c):
        #     if 0 <= r < ROWS and 0 <= c < COLS:
        #         if obstacleGrid[r][c] == 1:
        #             return 0
        #         if r == ROWS - 1 and c == COLS - 1:
        #             return 1
                
        #         d = (1, 0)
        #         ri = (0, 1)

        #         return dfs(r + d[0], c + d[1]) + dfs(r + ri[0], c + ri[1])

        #     else:
        #         return 0
        
        # return dfs(0, 0)

        # with dp
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[ROWS - 1][COLS - 1] = 1

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r + 1][c]
                    dp[r][c] += dp[r][c + 1]

        return dp[0][0]

        # [0, 0, 0]
        # [0, 0, 0]
        # [0, 1, 0]

        #.     [3, 2, 1]
        #.     [1, 1, 1]
        # dp = [0, 0, 1]