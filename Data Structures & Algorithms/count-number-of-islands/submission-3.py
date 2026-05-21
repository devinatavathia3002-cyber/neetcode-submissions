class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        output = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if grid[r][c] == "1":
                grid[r][c] = "."

                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            
            else:
                return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    output += 1
        
        return output



        