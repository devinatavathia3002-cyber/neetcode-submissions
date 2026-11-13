from collections import deque
class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        dist = -1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r, c))
        
        if len(q) == (ROWS * COLS) or not q:
            return -1
        # multi-source bfs
        while q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dir in directions:
                    x, y = dir
                    new_r, new_c = x + r, y + c
                    if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and grid[new_r][new_c] == 0:
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = 1
            dist += 1

        return dist