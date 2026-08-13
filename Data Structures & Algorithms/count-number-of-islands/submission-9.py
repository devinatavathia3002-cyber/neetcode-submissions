class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # can solve with dfs or bfs
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ct = 0
        q = deque()

        def bfs(r, c):
            q.append((r, c))
            grid[r][c] = '0'
            while q:
                currR, currC = q.popleft()
                for dir in directions:
                    x, y = dir
                    newR, newC = currR + x, currC + y
                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and grid[newR][newC] == '1':
                        q.append((newR, newC))
                        grid[newR][newC] = '0'

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    ct += 1
        return ct

