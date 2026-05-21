class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        output = 0

        def dfs(count, r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0
            return (dfs(count, r + 1, c) +
                    dfs(count, r - 1, c) +
                    dfs(count, r, c + 1) +
                    dfs(count, r, c - 1) + 1)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(0, r, c)
                    output = max(output, area)

        return output