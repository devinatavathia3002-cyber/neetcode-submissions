class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # can solve with dfs or bfs
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ct = 0

        def dfs(r, c):
            if grid[r][c] == '0':
                return
            else:
                grid[r][c] = '0'
                for dir in directions:
                    x, y = dir
                    newR, newC = x + r, c + y
                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and grid[newR][newC] == '1':
                        dfs(newR, newC)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    ct += 1
        return ct

