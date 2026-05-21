class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = {}

        def dfs(r, c, prev):
            if r >= ROWS or c >= COLS or r < 0 or c < 0:
                return 0
            curr = matrix[r][c]
            if curr > prev:
                if (r, c) in dp:
                    return dp[(r, c)]

            # how to get max from here
            if curr > prev:
                best = 0
                for coord in directions:
                    x, y = coord
                    best = max(best, dfs(x + r, y + c, matrix[r][c]) + 1)
                dp[(r, c)] = best
                return best
            
            return 0
                
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, -1)
        return max(dp.values())