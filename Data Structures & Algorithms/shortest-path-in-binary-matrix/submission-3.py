class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        q = deque()
        q.append((0, 0))
        count = 1

        while q:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                grid[row][col] = 1
                if row == ROWS - 1 and col == COLS - 1:
                    return count
                else:
                    for dir in directions:
                        x, y = dir
                        newR, newC = row + x, col + y
                        if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and grid[newR][newC] == 0:
                            q.append((newR, newC))
            count += 1

        return -1