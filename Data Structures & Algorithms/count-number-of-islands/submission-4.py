class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # dfs traversal 
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        output = 0

        def dfs(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1":
                grid[r][c] = "0"
                for cord in directions:
                    x, y = cord
                    newR = x + r
                    newC = y + c
                    dfs(newR, newC)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    output += 1

        return output