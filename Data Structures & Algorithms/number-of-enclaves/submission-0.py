class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        q = deque()

        def bfs():
            while q:
                r, c = q.popleft()
                grid[r][c] = 0

                for dir in directions:
                    x, y = dir
                    new_r, new_c = x + r, c + y
                    if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and grid[new_r][new_c] == 1:
                        q.append((new_r, new_c))
                    

        #top
        for i in range(COLS):
            if grid[0][i] == 1:
                q.append((0, i))
                bfs()
        #left
        for i in range(ROWS):
            if grid[i][0] == 1:
                q.append((i, 0))
                bfs()
        #right
        for i in range(ROWS):
            if grid[i][COLS - 1] == 1:
                q.append((i, COLS - 1))
                bfs()
        #bottom
        for i in range(COLS):
            if grid[ROWS - 1][i] == 1:
                q.append((ROWS - 1, i))
                bfs()
        
        # step 2, iterate again, this time updating res
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if grid[r][c] == 1:
                    res += 1

        return res
