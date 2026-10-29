class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        # first perform a dfs then a bfs

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        first_x, first_y = 0, 0
        q = deque()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            q.append((r, c))

            for dir in directions:
                x, y = dir
                new_r, new_c = x + r, y + c
                dfs(new_r, new_c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    first_x, first_y = r, c
                    break
        
        dfs(first_x, first_y)
        layer, steps = [], 0

        while q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dir in directions:
                    x, y = dir
                    new_r, new_c = x + r, y + c
                    if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS:
                        if grid[new_r][new_c] == 1:
                            return steps
                        if grid[new_r][new_c] == 0:
                            grid[new_r][new_c] = 2
                            layer.append((new_r, new_c))
            q = deque(layer)
            layer = []
            steps += 1
        

        # should never reach here but as a safety check...
        return -1


            


