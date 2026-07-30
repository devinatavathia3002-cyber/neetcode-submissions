class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        directions = [(0, 1), (1,0), (-1, 0), (0, -1)]

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        mins = 0
        while q:
            mins += 1
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                for dir in directions:
                    x, y = dir
                    newR = x + row
                    newC = y + col
                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and grid[newR][newC] == 1:
                        q.append((newR, newC))
                        grid[newR][newC] = 2

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return mins - 1 if mins > 0 else 0