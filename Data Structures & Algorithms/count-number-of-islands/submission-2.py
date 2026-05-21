class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        # visited = set()

        rows, cols = len(grid), len(grid[0])
        
        def checkVal(r, c, q):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                print((r, c))
                q.append([r, c])
                grid[r][c] = "0"
        
        def bfs(r, c):
            q = deque()
            q.append([r, c])

            while q: 
                for i in range(len(q)):
                    r, c = q.popleft()

                    checkVal(r + 1, c, q)
                    checkVal(r - 1, c, q)
                    checkVal(r, c + 1, q)
                    checkVal(r, c - 1, q)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1


        return islands